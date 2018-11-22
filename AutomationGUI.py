#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListView, QCompleter, QGraphicsDropShadowEffect
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap, QIcon
from PyQt5.QtCore import QStringListModel, Qt, QTimer
import xmltodict
from pathlib import Path
from AutomationGUI_ui import *
import os
import sys
import csv

if sys.version_info[0] < 3:
    FileNotFoundError = IOError


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.debug = False

        # create a frameless window without titlebar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # gui layout related
        dropShadow = QGraphicsDropShadowEffect()
        dropShadow.setXOffset(1)
        dropShadow.setYOffset(1)
        dropShadow.setBlurRadius(6)
        self.tabWidget.setGraphicsEffect(dropShadow)

        self.bottombuttonsLayout.setAlignment(Qt.AlignRight)
        self.generalLayout.setAlignment(Qt.AlignTop)
        self.loggingTabLayout.setAlignment(Qt.AlignLeft)
        self.dtcTabLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.logmodeLayout.setAlignment(Qt.AlignTop)

        # use these strings for messages
        self.config_invalid = 'Invalid config file detected.'
        self.config_notfound = 'Config filse not found. Default config and profile loaded.'
        self.unsaved_changes = 'You have unsaved changes.'
        self.untitled_profile = 'Untitled Profile'
        self.default_profile_loaded = 'Default profile loaded.'
        self.profile_loaded_success = 'Profile loaded successfully.'
        self.profile_does_not_exist = 'Profile does not exist. Please load profile.'
        self.profile_notfound_config = 'No last profile defined in config.'
        self.profile_invalid = 'Invalid profile detected.'
        self.profile_invalid_version = 'Invalid profile version detected.'
        self.profile_save_fail = 'Saving Profile...Fail'
        self.profile_save_success = 'Saving Profile...Success!'
        self.add_signal_success = 'Signal added successfully.'
        self.add_signal_duplicate = 'Duplicate signal. Try again.'
        self.add_signal_notfound = 'Signal not found in variable pool.'
        self.add_dtcex_success = 'DTC exception added successfully.'
        self.variable_pool_loaded_success = 'Variable pool loaded successfully.'
        self.variable_pool_notfound = 'Variable pool file does not exist.'

        self.defaultProfile = True

        # set default xml config file path
        self.configFile = 'C:/DS_Config/config.xml'
        self.profileFile = 'C:/DS_Config/profile1.xml'

        self.configDict = {}
        self.profileDict = {}
        self.variablePool = []

        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)

        self.dtcExModel = QStandardItemModel()
        self.dtcExListView.setModel(self.dtcExModel)

        # signals and slots for menus, buttons, etc
        self.testCaseExcelEdit.textChanged.connect(self.unsavedChanges)
        self.callFunctionEdit.textChanged.connect(self.unsavedChanges)
        self.csvReportEdit.textChanged.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)
        self.reloadVariablePoolBtn.clicked.connect(self.loadVariablePool)

        self.logRadioBtn0.clicked.connect(self.unsavedChanges)
        self.logRadioBtn1.clicked.connect(self.unsavedChanges)
        self.logRadioBtn2.clicked.connect(self.unsavedChanges)

        self.browseTestCaseExcelBtn.clicked.connect(self.browseTestCaseExcel)
        self.browseCallFunctionBtn.clicked.connect(self.browseCallFunction)
        self.browseCsvReportBtn.clicked.connect(self.browseCsvReport)
        self.browseVariablePoolBtn.clicked.connect(self.browseVariablePool)

        self.openTestCaseExcelFolderBtn.clicked.connect(self.openTestCaseExcelFolder)
        self.openCallFunctionFolderButton.clicked.connect(self.openCallFunctionFolder)
        self.openCsvReportFolderButton.clicked.connect(self.openCsvReportFolder)
        self.openVarPoolFolderButton.clicked.connect(self.openVarPoolFolder)

        self.addSignalBtn.clicked.connect(self.addSignal)
        self.addSignalEdit.returnPressed.connect(self.addSignal)
        self.removeSignalBtn.clicked.connect(self.removeSignal)

        self.addDtcExBtn.clicked.connect(self.addDtcEx)
        self.addDtcExEdit.returnPressed.connect(self.addDtcEx)
        self.removeDtcExBtn.clicked.connect(self.removeDtcEx)

        self.actionLoad.triggered.connect(self.browseProfile)
        self.actionNew.triggered.connect(self.newProfile)
        self.actionSave.triggered.connect(self.saveProfile)
        self.actionSaveAs.triggered.connect(self.saveAsProfile)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
        self.actionOpenConfigFolder.triggered.connect(self.openConfigFolder)
        self.showDebugCheckBox.clicked.connect(self.toggleDebug)

        self.logRadioBtn0.clicked.connect(self.hideAddSignal)
        self.logRadioBtn1.clicked.connect(self.hideAddSignal)
        self.logRadioBtn2.clicked.connect(self.showAddSignal)

        self.dtcExCheckBox.clicked.connect(self.dtcExToggle)

        # widgets initial settings
        self.tabWidget.setCurrentIndex(0)
        self.logRadioBtn0.setChecked(True)
        self.dtcExCheckBox.setChecked(False)
        self.hideAddSignal()
        self.hideDtcException()
        self.loadConfig()
        self.changesSaved = True

        self.startTimer = QTimer()
        self.startTimer.timeout.connect(self.tick)

        if self.autorunCheckBox.isChecked():
            self.startTimer.start(1000)
            self.startTimerCount = self.autorunSpinBox.value()

    # def mousePressEvent(self, event):
    #     print(event.button())

    # def resizeEvent(self, event):
    #     self.tabWidget.setFixedHeight(self.height()-160)
    #     self.tabWidget.setFixedWidth(self.width()-40)
    #     self.gridLayout.width
    #     # QtGui.QMainWindow.resizeEvent(self, event)

    def dprint(self, msg):
        if self.debug:
            print(msg)

    def tick(self):
        if self.startTimerCount > 0:
            self.exitButton.setText('Continue ({})'.format(self.startTimerCount))
            self.dprint(self.startTimerCount)
            self.startTimerCount = self.startTimerCount - 1
        else:
            self.startTimer.stop()
            self.dprint('Timer stop')
            self.exitButton.setText('Continue')
            if self.autorunCheckBox.isChecked():
                self.exit()

    def toggleDebug(self):
        if self.showDebugCheckBox.isChecked():
            self.debug = True
            print('Debug ON')
        else:
            self.debug = False
            print('Debug OFF')

    def openCallFunctionFolder(self):
        callfunctionpath = Path(self.callFunctionEdit.text())
        if os.path.exists(str(callfunctionpath)):
            os.startfile(str(callfunctionpath))

    def openCsvReportFolder(self):
        csvreportpath = Path(self.csvReportEdit.text())
        if os.path.exists(str(csvreportpath)):
            os.startfile(str(csvreportpath))

    def openVarPoolFolder(self):
        varpoolpath = Path(self.variablePoolEdit.text())
        dirname = os.path.dirname(str(varpoolpath))
        if os.path.exists(str(dirname)):
            os.startfile(str(dirname))
            os.startfile(str(varpoolpath))

    def openTestCaseExcelFolder(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirname = os.path.dirname(str(testCaseExcelPath))
        if os.path.exists(str(dirname)):
            os.startfile(str(dirname))
            os.startfile(str(testCaseExcelPath))

    def openConfigFolder(self):
        configfolder = os.path.dirname(str(self.configFile))
        # param = 'explorer "{}"'.format(configFolder)
        # subprocess.Popen(param)
        if os.path.exists(configfolder):
            os.startfile(configfolder)

    def hideAddSignal(self):
        self.addSignalGroupBox.hide()

    def showAddSignal(self):
        self.addSignalGroupBox.show()

    def dtcExToggle(self):
        if self.dtcExCheckBox.isChecked():
            self.showDtcException()
        else:
            self.hideDtcException()

    def hideDtcException(self):
        self.dtcExGroupBox.hide()

    def showDtcException(self):
        self.dtcExGroupBox.show()

    def unsavedChanges(self):
        self.changesSaved = False
        self.statusbar.showMessage(self.unsaved_changes)

    def newProfile(self):
        self.setDefaultProfile()
        self.profileFile = ''
        self.setTitle(self.untitled_profile)
        self.updateGuiFromProfileDict()
        self.statusbar.showMessage(self.default_profile_loaded)

    def browseProfile(self):
        profilefolder = os.path.dirname(str(self.profileFile))
        filePath, fileType = QFileDialog.getOpenFileName(
            self,
            "Open Profile",
            profilefolder,
            "XML Files (*.xml);;All Files (*)"
        )

        if filePath:
            self.profileFile = Path(filePath)
            self.loadProfile()
            self.saveConfig()

    def browseTestCaseExcel(self):
        self.browseFile(
            self.testCaseExcelEdit,
            'Select Test Case Excel File',
            'Excel Files (*.xlsx; *.xlsm)'
        )

    def browseCallFunction(self):
        self.browseFolder(self.callFunctionEdit, 'Select Call Function Directory')

    def browseCsvReport(self):
        self.browseFolder(self.csvReportEdit, 'Select CSV Report Directory')

    def browseVariablePool(self):
        self.browseFile(self.variablePoolEdit, 'Open Variable Pool', 'CSV Files (*.csv)')

    def browseFile(self, editBox, titleDialog, fileType):
        folder = str(os.path.dirname(editBox.text()))

        filePath, fileType = QFileDialog.getOpenFileName(
            self,
            titleDialog,
            folder,
            "{};;All Files (*)".format(fileType)
        )

        if filePath:
            editBox.setText(str(Path(filePath)))

    def browseFolder(self, editBox, titleDialog):
        folder = editBox.text()
        folderPath = QFileDialog.getExistingDirectory(self, "Select CSV Report Directory", folder)
        if len(str(folderPath)):
            editBox.setText(str(Path(folderPath)))

    def newConfig(self):
        self.setDefaultConfigDict()

    def saveProfile(self):
        configfolder = os.path.dirname(str(self.configFile))
        if self.defaultProfile:
            filePath, fileType = QFileDialog.getSaveFileName(
                self,
                "Save Profile As",
                configfolder,
                "XML Files (*.xml);;All Files (*)"
            )
            if filePath:
                self.profileFile = Path(filePath)

        # save config file as well
        self.saveConfig()

        # updates the profile dict before unparsing to xml
        self.updateProfileDictFromGui()

        # save the profile from profile dict
        try:
            with open(str(self.profileFile), 'wb') as f:
                self.dprint(str(self.profileFile))
                f.write(bytearray(xmltodict.unparse(self.profileDict, pretty=True), encoding='utf-8'))
                self.setTitle(self.profileFile)
                self.defaultProfile = False
                self.changesSaved = True
                self.statusbar.showMessage(self.profile_save_success)
        except FileNotFoundError:
            self.statusbar.showMessage(self.profile_save_fail)

        # update and check all paths exist, prompt accordingly
        callpath = self.callFunctionEdit.text()
        if callpath != '':
            self.checkFolderExist(callpath)

        csvpath = self.csvReportEdit.text()
        if csvpath != '':
            self.csvReportEdit.setText(csvpath)

        varpoolpath = self.variablePoolEdit.text()
        if varpoolpath != '':
            self.checkVarPoolExist(varpoolpath)

    def saveAsProfile(self):
        profilefolder = os.path.dirname(str(self.profileFile))
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Save Profile As",
            profilefolder,
            "XML Files (*.xml);;All Files (*)"
        )

        if filePath:
            self.profileFile = Path(filePath)
            self.saveProfile()

    # updates the profile dict
    def updateProfileDictFromGui(self):
        # generate the log mode number based on checkboxes
        logMode = (self.logRadioBtn0.isChecked() + self.logRadioBtn1.isChecked()*2 + self.logRadioBtn2.isChecked()*3) - 1

        # update signal list
        signalList = []
        for i in range(0, self.addSignalModel.rowCount()):
            signalList.append(self.addSignalModel.item(i, 0).text())

        # update dtc exception list
        dtcExList = []
        for i in range(0, self.dtcExModel.rowCount()):
            dtcExList.append(self.dtcExModel.item(i, 0).text())

        self.setProfileDict(
            testcaseexcel=self.testCaseExcelEdit.text(),
            callfolder=self.callFunctionEdit.text(),
            csvfolder=self.csvReportEdit.text(),
            varpoolpath=self.variablePoolEdit.text(),
            fullmessages=self.fullMessagesCheckbox.isChecked(),
            includeversion=self.versionCheckBox.isChecked(),
            logmode=logMode,
            signallist=signalList,
            dtcenable=self.dtcExCheckBox.isChecked(),
            dtcexlist=dtcExList
        )

    def addSignal(self):
        signal = self.addSignalEdit.text()
        try:
            self.variablePool.index(signal)
            # check for duplicate signal
            if self.addSignalModel.findItems(signal):
                self.statusbar.showMessage(self.add_signal_duplicate)
            else:
                self.addSignalModel.appendRow(QStandardItem(self.addSignalEdit.text()))
                self.addSignalEdit.clear()
                self.addSignalEdit.setFocus()
                self.statusbar.showMessage(self.add_signal_success)
        except ValueError:
            self.statusbar.showMessage(self.add_signal_notfound)

    def removeSignal(self):
        self.addSignalModel.removeRow(self.addSignalListView.currentIndex().row())

    def addDtcEx(self):
        self.dtcExModel.appendRow(QStandardItem(self.addDtcExEdit.text()))
        self.addDtcExEdit.clear()
        self.addDtcExEdit.setFocus()
        self.statusbar.showMessage(self.add_dtcex_success)

    def removeDtcEx(self):
        self.dtcExModel.removeRow(self.dtcExListView.currentIndex().row())

    def saveConfig(self):
        # update the config dict
        self.setConfigDict(
            lastprofile=str(self.profileFile),
            width=self.width(),
            height=self.height(),
            autorun=self.autorunCheckBox.isChecked(),
            autoruntimer=self.autorunSpinBox.value()
        )

        # if config folder not found, create one
        dirname = os.path.dirname(str(self.configFile))

        if not os.path.exists(dirname):
            os.mkdir(dirname)

        try:
            with open(str(self.configFile), 'wb') as f:
                f.write(bytearray(xmltodict.unparse(self.configDict, pretty=True), encoding='utf-8'))
        except FileNotFoundError:
            self.statusbar.showMessage(self.config_notfound)

    def loadProfile(self):
        try:
            with open(str(self.profileFile), 'rb') as f:
                self.profileDict = xmltodict.parse(f.read())
                try:
                    profileversion = self.profileDict['Profile']['@version']
                    varpoolfile = self.profileDict['Profile']['VariablePoolPath']
                    if profileversion == '1.0':

                        # updates the gui after loading a valid profile
                        self.defaultProfile = False
                        self.updateGuiFromProfileDict()
                        if os.path.exists(varpoolfile):
                            self.loadVariablePool()
                        self.setTitle(self.profileFile)
                        self.statusbar.showMessage(self.profile_loaded_success)
                    else:
                        self.statusbar.showMessage(self.profile_invalid_version)
                except:
                    self.statusbar.showMessage(self.profile_invalid)
        except FileNotFoundError:
            self.newProfile()
            self.statusbar.showMessage(self.profile_does_not_exist)

    def checkFolderExist(self, path):
        basename = os.path.basename(str(path))
        if not os.path.exists(path):
            msgReply = QMessageBox.question(
                self,
                'Create Folder',
                '\'' + basename + '\'' + ' folder was not found. Would you like to create it?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if msgReply == QMessageBox.Yes:
                os.mkdir(path)

    def checkVarPoolExist(self, path):
        basename = os.path.basename(str(path))
        if not os.path.exists(path):
            msgReply = QMessageBox.question(
                self,
                'Not Found',
                '\'' + basename + '\'' + ' file was not found. Would you like to browse for one?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if msgReply == QMessageBox.Yes:
                self.browseVariablePool()

    # use the profile dictionary to update the gui
    def updateGuiFromProfileDict(self):
        try:
            testcasepath = self.profileDict['Profile']['TestCaseExcel']
            if testcasepath:
                self.testCaseExcelEdit.setText(testcasepath)
        except:
            self.testCaseExcelEdit = ''
        try:
            callpath = self.profileDict['Profile']['CallFunctionFolder']
            if callpath:
                self.callFunctionEdit.setText(callpath)
                self.checkFolderExist(callpath)
        except:
            self.callFunctionEdit.setText('')

        try:
            csvpath = self.profileDict['Profile']['CSVReportFolder']
            if csvpath:
                self.csvReportEdit.setText(csvpath)
                self.checkFolderExist(csvpath)
        except:
            self.csvReportEdit.setText('')


        try:
            varpoolpath = self.profileDict['Profile']['VariablePoolPath']
            self.variablePoolEdit.setText(varpoolpath)
            self.checkVarPoolExist(varpoolpath)
        except:
            self.variablePoolEdit.setText('')

        try:
            fullmessagescheckbox = self.profileDict['Profile']['FullMessages']['@enable']
            self.fullMessagesCheckbox.setChecked(eval(fullmessagescheckbox))
        except:
            self.fullMessagesCheckbox.setChecked(False)

        try:
            versioncheckbox = self.profileDict['Profile']['Version']['@include']
            self.versionCheckBox.setChecked(eval(versioncheckbox))
        except:
            self.versionCheckBox.setChecked(False)

        self.addSignalModel.clear()
        try:
            templist = self.profileDict['Profile']['Log']['Signal']
            signalList = []
            # if temp is a list we iterate and add, else we append a single element
            if isinstance(templist, list):
                signalList.extend(x for x in templist)
            else:
                signalList.append(templist)

            for s in signalList:
                self.addSignalModel.appendRow(QStandardItem(str(s)))
        except:
            self.dprint('Signal list is empty')

        self.dtcExModel.clear()

        # if temp is a list we iterate and add, else we append a single element
        try:
            exceptlist = self.profileDict['Profile']['DTC']['Except']
            dtcExList = []
            if isinstance(exceptlist, list):
                dtcExList.extend(x for x in exceptlist)
            else:
                dtcExList.append(exceptlist)

            # add rows into qt list widget
            for s in dtcExList:
                self.dtcExModel.appendRow(QStandardItem(str(s)))
        except:
            self.dprint('DTCs exception list is empty')

    def loadConfig(self):
        try:
            with open(str(self.configFile), 'rb') as f:
                self.configDict = xmltodict.parse(f.read())

                try:
                    configversion = self.configDict['Config']['@version']
                    if configversion == '1.0':
                        try:
                            width = self.configDict['Config']['Width']
                            height = self.configDict['Config']['Height']
                            self.resize(int(width), int(height))
                        except:
                            self.dprint('Width and height values not saved')

                        try:
                            profilepath = self.configDict['Config']['LastProfile']
                            self.profileFile = Path(profilepath)
                            if os.path.exists(str(self.profileFile)):
                                self.loadProfile()
                        except:  # profile not found
                            self.statusbar.showMessage(self.profile_notfound_config)

                        try:
                            autorun = self.configDict['Config']['Autorun']
                            self.autorunCheckBox.setChecked(eval(autorun))
                        except:
                            self.dprint('Autorun setting not saved')

                        try:
                            autoruntimer = self.configDict['Config']['AutorunTimer']
                            self.autorunSpinBox.setValue(eval(autoruntimer))
                        except:
                            self.dprint('Autorun timer setting not saved')

                except:  # key error
                    self.statusbar.showMessage(self.config_invalid)
        except FileNotFoundError:
            self.statusbar.showMessage(self.config_notfound)
            self.setDefaultConfigDict()
            self.setDefaultProfile()
            self.setTitle(self.untitled_profile)

    # load the variable pool from csv file and extract variable names only
    def loadVariablePool(self):
        varpoolfile = Path(self.variablePoolEdit.text())
        if len(str(varpoolfile)) > 1:
            try:
                with open(str(varpoolfile)) as f:
                    self.variablePool = []
                    self.variablePool.extend(row['VariableName'] for row in csv.DictReader(f))

                    model = QStringListModel()
                    model.setStringList(self.variablePool)
                    completer = QCompleter()
                    completer.setModel(model)
                    completer.setCaseSensitivity(0)
                    self.addSignalEdit.setCompleter(completer)
                    self.statusbar.showMessage(self.variable_pool_loaded_success)
            except FileNotFoundError:
                self.statusbar.showMessage(self.variable_pool_notfound)

    def setTitle(self, profilePath):
        self.setWindowTitle('[' + str(profilePath) + '] - AutomationDesk GUI')

    def setProfileDict(
            self,
            testcaseexcel='',
            callfolder='',
            csvfolder='',
            varpoolpath='',
            includeversion='False',
            fullmessages='False',
            logmode='0',
            signallist=[],
            dtcenable='False',
            dtcexlist=[]
    ):

        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'TestCaseExcel': testcaseexcel,
                'CallFunctionFolder': callfolder,
                'CSVReportFolder': csvfolder,
                'VariablePoolPath': varpoolpath,
                'Version': {'@include': includeversion},
                'FullMessages': {'@enable': fullmessages},
                'Log': {
                    '@mode': logmode,
                    'Signal': signallist
                },
                'DTC': {
                    '@enable': dtcenable,
                    'Except': dtcexlist
                }
            }
        }

    def setDefaultProfile(self):
        self.defaultProfile = True
        # load default profile if no params are given
        self.setProfileDict()

    def setConfigDict(
            self, lastprofile='',
            width=800,
            height=480,
            autorun=True,
            autoruntimer=10
    ):
        self.configDict = {
            'Config': {
                '@version': '1.0',
                'LastProfile': lastprofile,
                'Width': width,
                'Height': height,
                'Autorun': autorun,
                'AutorunTimer': autoruntimer
            }
        }

    def setDefaultConfigDict(self):
        self.unsavedChanges()
        # load default config if no params are given
        self.setConfigDict()

    def exit(self):
        if not self.changesSaved:
            msgReply = QMessageBox.question(
                self,
                'Save Changes',
                'Would you like to save before exit?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if msgReply == QMessageBox.Yes:
                self.saveProfile()
                self.dprint('File saved')

        self.saveConfig()
        self.updateProfileDictFromGui()
        self.close()

    def about(self):
        about = QMessageBox()
        about.setWindowIcon(QIcon(':/logo/graphics/karmalogo_48dp.png'))
        about.setWindowTitle('About')
        about.setText('Version 1.12\nAuthor: Vu Le')
        about.setInformativeText('Copyright (C) 2018\nKarma Automotive')
        about.setIconPixmap(QPixmap(':/logo/graphics/karmalogo_48dp.png'))
        about.exec_()

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    # return the profile dict to caller such as AutomationDesk
    return form.profileDict


if __name__ == '__main__':
    main()
