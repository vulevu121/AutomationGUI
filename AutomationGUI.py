#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import xmltodict
from pathlib import Path
from AutomationGUI_ui import *
import os
import sys
import strings

if sys.version_info[0] < 3:
    FileNotFoundError = IOError

debug = False
def debugprint(msg):
    if debug:
        print(msg)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


        # create a frameless window without titlebar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # set default xml config file path
        self.configFile = 'C:/DS_Config/config.xml'
        self.profileFile = 'C:/DS_Config/profile1.xml'

        self.configDict = {}
        self.profileDict = {}
        self.variablePoolDict = {}
        self.updateVariablePool = False  # update variable pool in AutomationDesk
        self.defaultProfile = True  # false when a profile is loaded

        # Qt item models
        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)

        self.dtcExModel = QStandardItemModel()
        self.dtcExListView.setModel(self.dtcExModel)

        # toolbar


        # general tab
        self.browseTestCaseExcelBtn.clicked.connect(self.browseTestCaseExcel)
        self.browseCallFunctionBtn.clicked.connect(self.browseCallFunction)
        self.browseCsvReportBtn.clicked.connect(self.browseCsvReport)
        self.browseVariablePoolBtn.clicked.connect(self.browseVariablePool)

        self.openTestCaseExcelFolderBtn.clicked.connect(self.openTestCaseExcelFolder)
        self.openCallFunctionFolderButton.clicked.connect(self.openCallFunctionFolder)
        self.openVarPoolFolderButton.clicked.connect(self.openVarPoolFolder)

        self.testCaseExcelEdit.textChanged.connect(self.unsavedChanges)
        self.callFunctionEdit.textChanged.connect(self.unsavedChanges)
        self.csvReportEdit.textChanged.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)
        self.variablePoolEdit.textChanged.connect(self.unsavedChanges)
        self.reloadVariablePoolBtn.clicked.connect(self.loadVariablePool)

        self.toolButton.setPopupMode(QToolButton.InstantPopup)
        menu = QMenu()
        openCsvReportFolderButton = QAction(QIcon(':/icon/graphics/baseline_open_in_browser_black_24dp.png'), 'Open Folder + File', self)
        openCsvReportFolderButton.triggered.connect(self.openCsvReportFolder)
        menu.addAction(openCsvReportFolderButton)

        useTestCasePathButton = QAction(QIcon(':/icon/graphics/baseline_folder_black_24dp.png'), 'Use Test Case Path', self)
        useTestCasePathButton.triggered.connect(self.useTestCasePath)
        menu.addAction(useTestCasePathButton)

        self.toolButton.setMenu(menu)

        # logging tab
        self.addSignalBtn.clicked.connect(self.addSignal)
        self.addSignalEdit.returnPressed.connect(self.addSignal)
        self.removeSignalBtn.clicked.connect(self.removeSignal)

        self.logRadioBtn0.clicked.connect(self.hideAddSignal)
        self.logRadioBtn1.clicked.connect(self.hideAddSignal)
        self.logRadioBtn2.clicked.connect(self.showAddSignal)
        self.dtcExCheckBox.clicked.connect(self.dtcExToggle)

        self.logRadioBtn0.clicked.connect(self.unsavedChanges)
        self.logRadioBtn1.clicked.connect(self.unsavedChanges)
        self.logRadioBtn2.clicked.connect(self.unsavedChanges)

        # dtc tab
        self.addDtcExBtn.clicked.connect(self.addDtcEx)
        self.addDtcExEdit.returnPressed.connect(self.addDtcEx)
        self.removeDtcExBtn.clicked.connect(self.removeDtcEx)

        # settings tab
        self.updateVariablePoolCheckBox.clicked.connect(self.toggleUpdateVariablePool)

        # file menu
        self.actionLoad.triggered.connect(self.browseProfile)
        self.actionNew.triggered.connect(self.newProfile)
        self.actionSave.triggered.connect(self.saveProfile)
        self.actionSaveAs.triggered.connect(self.saveAsProfile)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
        self.actionConfigFolder.triggered.connect(self.openConfigFolder)
        self.showDebugCheckBox.clicked.connect(self.toggleDebug)

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
        self.settingsVerticalLayoutRight.setAlignment(Qt.AlignTop)
        self.settingsVerticalLayoutLeft.setAlignment(Qt.AlignTop)

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



    def tick(self):
        if self.startTimerCount > 0:
            self.exitButton.setText('Continue ({})'.format(self.startTimerCount))
            debugprint(self.startTimerCount)
            self.startTimerCount = self.startTimerCount - 1
        else:
            self.startTimer.stop()
            debugprint('Timer stop')
            self.exitButton.setText('Continue')
            if self.autorunCheckBox.isChecked():
                self.exit()

    def toggleDebug(self):
        debug = self.showDebugCheckBox.isChecked()
        print('ShowDebug={}'.format(debug))

    def toggleUpdateVariablePool(self):
        self.updateVariablePool = self.updateVariablePoolCheckBox.isChecked()
        debugprint('UpdateVariablePool={}'.format(self.updateVariablePool))

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

    def useTestCasePath(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirname = os.path.dirname(str(testCaseExcelPath))
        self.csvReportEdit.setText(str(dirname) + '\\Logs')

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
        self.statusbar.showMessage(strings.UNSAVED_CHANGES)

    def newProfile(self):
        self.setDefaultProfile()
        self.profileFile = ''
        self.setTitle(strings.PROFILE_UNTITLED)
        self.updateGuiFromProfileDict()
        self.statusbar.showMessage(strings.PROFILE_DEFAULT_LOADED)

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
        self.browseFile(self.variablePoolEdit, 'Open Variable Pool', 'TXT Files (*.txt)')

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
                debugprint(str(self.profileFile))
                f.write(bytearray(xmltodict.unparse(self.profileDict, pretty=True), encoding='utf-8'))
                self.setTitle(self.profileFile)
                self.defaultProfile = False
                self.changesSaved = True
                self.statusbar.showMessage(strings.PROFILE_SAVE_OK)
        except FileNotFoundError:
            self.statusbar.showMessage(strings.PROFILE_SAVE_FAIL)

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
            callfuncdebug=self.callFunctionDebugCheckbox.isChecked(),
            includeversion=self.versionCheckBox.isChecked(),
            logmode=logMode,
            signallist=signalList,
            dtcenable=self.dtcExCheckBox.isChecked(),
            dtcexlist=dtcExList,
            updatevp=self.updateVariablePool
        )

    def addSignal(self):
        signal = self.addSignalEdit.text()

        try:
            variablePoolKeys = list(self.variablePoolDict)

            try:
                foundInVp = variablePoolKeys.index(signal) >= 0
            except:
                foundInVp = False

            foundInModel = self.addSignalModel.findItems(signal)

            if foundInModel:
                self.statusbar.showMessage(strings.SIGNAL_ADD_DUPLICATE)

            if foundInVp and not foundInModel:
                self.addSignalModel.appendRow(QStandardItem(self.addSignalEdit.text()))
                self.addSignalEdit.clear()
                self.addSignalEdit.setFocus()
                self.statusbar.showMessage(strings.SIGNAL_ADD_OK)
        except:
            self.statusbar.showMessage(strings.SIGNAL_NOTFOUND)

    def removeSignal(self):
        self.addSignalModel.removeRow(self.addSignalListView.currentIndex().row())

    def addDtcEx(self):
        self.dtcExModel.appendRow(QStandardItem(self.addDtcExEdit.text()))
        self.addDtcExEdit.clear()
        self.addDtcExEdit.setFocus()
        self.statusbar.showMessage(strings.DTCEX_ADD_OK)


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
            self.statusbar.showMessage(strings.CONFIG_NOTFOUND)

    def loadProfile(self):
        if os.path.exists(str(self.profileFile)):
            with open(str(self.profileFile), 'rb') as f:
                try:
                    self.profileDict = xmltodict.parse(f.read())
                except:
                    debugprint('Unable to parse profile XML file.')

                profileValid = True

                try:
                    profileversion = self.profileDict['Profile']['@version']
                    if profileversion == '1.0':
                        profileValid &= True
                    else:
                        debugprint('Invalid profile version.')
                except:
                    debugprint('No profile version defined.')

                try:
                    varpoolfile = self.profileDict['Profile']['VariablePoolPath']
                    if not os.path.exists(str(varpoolfile)):
                        self.statusbar.showMessage(strings.VARIABLE_POOL_NOTFOUND)
                    profileValid &= True
                except:
                    debugprint('No variable pool file defined in profile.')
                    self.statusbar.showMessage(strings.CONFIG_VARIABLE_POOL_DEFINED)

                if profileValid:
                    # updates the gui after loading a valid profile
                    self.defaultProfile = False
                    self.updateGuiFromProfileDict()
                    if os.path.exists(str(varpoolfile)):
                        self.loadVariablePool()
                    self.setTitle(self.profileFile)
                    self.statusbar.showMessage(strings.PROFILE_LOADED_OK)
                else:
                    self.statusbar.showMessage(strings.PROFILE_INVALID)

        else:
            self.newProfile()
            self.statusbar.showMessage(strings.PROFILE_NOTFOUND)

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
            callfunctiondebug = self.profileDict['Profile']['CallFunctionDebug']['@enable']
            self.callFunctionDebugCheckbox.setChecked(eval(callfunctiondebug))
        except:
            self.callFunctionDebugCheckBox.setChecked(False)

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
            debugprint('Signal list is empty')

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
            debugprint('DTCs exception list is empty')

    def loadConfig(self):
        if os.path.exists(str(self.configFile)):
            with open(str(self.configFile), 'rb') as f:
                configValid = True

                try:
                    self.configDict = xmltodict.parse(f.read())
                    configValid &= True
                except:
                    debugprint('Unable to parse XML config file')

                try:
                    configversion = self.configDict['Config']['@version']
                    if configversion == '1.0':
                        configValid &= True
                except:
                    debugprint('Version was not found in config file.')

                try:
                    width = self.configDict['Config']['Width']
                    height = self.configDict['Config']['Height']
                    self.resize(int(width), int(height))
                except:
                    debugprint('Window width or height is missing in config.')


                try:
                    profilepath = self.configDict['Config']['LastProfile']
                    self.profileFile = Path(profilepath)
                    if os.path.exists(profilepath):
                        self.loadProfile()
                except:
                    self.statusbar.showMessage(strings.CONFIG_PROFILE_NOTFOUND)
                    debugprint('Last profile not found in config.')



                try:
                    autorun = self.configDict['Config']['Autorun']
                    self.autorunCheckBox.setChecked(eval(autorun))
                except:
                    debugprint('Autorun setting not found in config.')

                try:
                    autoruntimer = self.configDict['Config']['AutorunTimer']
                    self.autorunSpinBox.setValue(eval(autoruntimer))
                except:
                    debugprint('Autorun time not found in config.')

                if not configValid:
                    self.statusbar.showMessage(strings.CONFIG_INVALID)
        else:
            self.statusbar.showMessage(strings.CONFIG_NOTFOUND)
            self.setDefaultConfigDict()
            self.setDefaultProfile()
            self.setTitle(strings.PROFILE_UNTITLED)

    # load the variable pool from csv file and extract variable names only
    def loadVariablePool(self):
        varpoolfile = Path(self.variablePoolEdit.text())
        if os.path.exists(str(varpoolfile)):
            try:
                with open(str(varpoolfile)) as f:
                    # self.variablePool.extend(row['VariableName'] for row in csv.DictReader(f))
                    self.variablePoolDict = eval(f.read())

                    variablePoolKeys = list(self.variablePoolDict)

                    model = QStringListModel()
                    model.setStringList(variablePoolKeys)
                    completer = QCompleter()
                    completer.setModel(model)
                    completer.setCaseSensitivity(0)
                    self.addSignalEdit.setCompleter(completer)
                    self.statusbar.showMessage(strings.VARIABLE_POOL_LOADED_OK)
            except FileNotFoundError:
                self.statusbar.showMessage(strings.VARIABLE_POOL_NOTFOUND)

    def setTitle(self, profilePath):
        self.setWindowTitle('[' + str(profilePath) + '] - AutomationDesk GUI')

    def setProfileDict(
            self,
            testcaseexcel='',
            callfolder='',
            csvfolder='',
            varpoolpath='',
            includeversion='False',
            callfuncdebug='False',
            logmode='0',
            signallist=[],
            dtcenable='False',
            dtcexlist=[],
            updatevp='False'
    ):

        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'TestCaseExcel': testcaseexcel,
                'CallFunctionFolder': callfolder,
                'CSVReportFolder': csvfolder,
                'VariablePoolPath': varpoolpath,
                'UpdateVariablePool': updatevp,
                'Version': {'@include': includeversion},
                'CallFunctionDebug': {'@enable': callfuncdebug},
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
        self.setConfigDict()  # load default config if no params are given

    def toolButtonPressed(self, a):
        print("Pressed tool button")


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
                debugprint('File saved')

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

    return form.profileDict, form.variablePoolDict  # return data to AutomationDesk


if __name__ == '__main__':
    main()
