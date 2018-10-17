#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListView, QCompleter, QGraphicsDropShadowEffect
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import QStringListModel
import xmltodict
from pathlib import Path
from xmlconfig import *
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

        # gui effects
        dropShadow = QGraphicsDropShadowEffect()
        dropShadow.setXOffset(1)
        dropShadow.setYOffset(1)
        dropShadow.setBlurRadius(6)
        self.tabWidget.setGraphicsEffect(dropShadow)

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
        self.configFile = Path('C:/DS_Config/config.xml')
        self.profileFile = Path('C:/DS_Config/profile1.xml')

        self.configDict = {}
        self.profileDict = {}
        self.variablePool = []

        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)

        self.dtcExModel = QStandardItemModel()
        self.dtcExListView.setModel(self.dtcExModel)

        # signals and slots for menus, buttons, etc
        self.callFunctionEdit.textChanged.connect(self.unsavedChanges)
        self.csvReportEdit.textChanged.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)
        self.reloadVariablePoolBtn.clicked.connect(self.loadVariablePool)

        self.logRadioBtn0.clicked.connect(self.unsavedChanges)
        self.logRadioBtn1.clicked.connect(self.unsavedChanges)
        self.logRadioBtn2.clicked.connect(self.unsavedChanges)

        self.browseCallFunctionBtn.clicked.connect(self.browseCallFunction)
        self.browseCsvReportBtn.clicked.connect(self.browseCsvReport)
        self.browseVariablePoolBtn.clicked.connect(self.browseVariablePool)

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

        self.logRadioBtn0.clicked.connect(self.hideAddSignal)
        self.logRadioBtn1.clicked.connect(self.hideAddSignal)
        self.logRadioBtn2.clicked.connect(self.showAddSignal)

        self.dtcExCheckBox.clicked.connect(self.dtcExToggle)

        # widgets initial settings
        self.logRadioBtn0.setChecked(True)
        self.dtcExCheckBox.setChecked(False)
        self.hideAddSignal()
        self.hideDtcException()
        self.loadConfig()
        self.changesSaved = True

    # def mousePressEvent(self, event):
    #     print(event.button())


    def openConfigFolder(self):
        configFolder = os.path.dirname(self.configFile)
        # param = 'explorer "{}"'.format(configFolder)
        # subprocess.Popen(param)
        os.startfile(configFolder)

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
        profilefolder = os.path.dirname(self.profileFile)
        filePath, fileType = QFileDialog.getOpenFileName(self, "Open Profile", profilefolder,"XML Files (*.xml);;All Files (*)")
        if filePath:
            self.profileFile = Path(filePath)
            self.loadProfile()
            self.saveConfig()

    def browseCallFunction(self):
        folderPath = QFileDialog.getExistingDirectory(self, "Select Call Function Directory", "")
        if folderPath:
            self.callFunctionEdit.setText(str(Path(folderPath)))

    def browseCsvReport(self):
        folderPath = QFileDialog.getExistingDirectory(self, "Select CSV Report Directory", "")
        if len(str(folderPath)):
            self.csvReportEdit.setText(str(Path(folderPath)))

    def browseVariablePool(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, "Open Variable Pool", "","CSV Files (*.csv);;All Files (*)")
        if filePath:
            self.variablePoolEdit.setText(str(Path(filePath)))

    def newConfig(self):
        self.setDefaultConfigDict()


    def saveProfile(self):
        configfolder = os.path.dirname(self.configFile)
        if self.defaultProfile:
            filePath, fileType = QFileDialog.getSaveFileName(self, "Save Profile As", configfolder,
                                                             "XML Files (*.xml);;All Files (*)")
            if filePath:
                self.profileFile = Path(filePath)

        # save config file as well
        self.saveConfig()

        # updates the profile dict before unparsing to xml
        self.updateProfileDict()

        # save the profile from profile dict
        try:
            with open(str(self.profileFile), 'wb') as f:
                if self.debug: print(str(self.profileFile))
                f.write(bytearray(xmltodict.unparse(self.profileDict, pretty=True), encoding='utf-8'))
                self.setTitle(self.profileFile)
                self.defaultProfile = False
                self.changesSaved = True
                self.statusbar.showMessage(self.profile_save_success)
        except FileNotFoundError:
            self.statusbar.showMessage(self.profile_save_fail)

        # check all paths exist, prompt accordingly
        try:
            callpath = self.profileDict['Profile']['CallFunctionFolder']
            self.callFunctionEdit.setText(callpath)
            self.checkFolderExist(callpath)
        except:
            self.callFunctionEdit.setText('')

        try:
            csvpath = self.profileDict['Profile']['CSVReportFolder']
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


    def saveAsProfile(self):
        profilefolder = os.path.dirname(self.profileFile)
        filePath, fileType = QFileDialog.getSaveFileName(self, "Save Profile As", profilefolder,"XML Files (*.xml);;All Files (*)")

        if filePath:
            self.profileFile = Path(filePath)
            self.saveProfile()

    # updates the profile dict
    def updateProfileDict(self):
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

        self.setProfileDict(callfolder=self.callFunctionEdit.text(),
                            csvfolder=self.csvReportEdit.text(),
                            varpoolpath=self.variablePoolEdit.text(),
                            includeversion=self.versionCheckBox.isChecked(),
                            logmode=logMode,
                            signallist=signalList,
                            dtcenable=self.dtcExCheckBox.isChecked(),
                            dtcexlist=dtcExList)

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
        self.configDict['Config']['LastProfile'] = str(self.profileFile)

        # if config folder not found, create one
        dirname = os.path.dirname(str(self.configFile))

        if not os.path.exists(dirname):
            os.mkdir(dirname)

        with open(str(self.configFile), 'wb') as f:
            f.write(bytearray(xmltodict.unparse(self.configDict, pretty=True), encoding='utf-8'))

    def loadProfile(self):
        try:
            with open(str(self.profileFile), 'rb') as f:
                self.profileDict = xmltodict.parse(f.read())
                try:
                    if self.profileDict['Profile']['@version'] == '1.0':
                        # updates the gui after loading a valid profile
                        self.defaultProfile = False
                        self.updateGuiFromProfileDict()
                        self.loadVariablePool()
                        self.setTitle(self.profileFile)
                        self.statusbar.showMessage(self.profile_loaded_success)
                except KeyError:
                    self.statusbar.showMessage(self.profile_invalid)
        except FileNotFoundError:
            self.newProfile()
            self.statusbar.showMessage(self.profile_does_not_exist)

    def checkFolderExist(self, path):
        basename = os.path.basename(path)
        if not os.path.exists(path):
            msgReply = QMessageBox.question(self,
                                            'Create Folder',
                                            '\'' + basename + '\'' + ' folder was not found. Would you like to create it?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if msgReply == QMessageBox.Yes:
                os.mkdir(path)

    def checkVarPoolExist(self, path):
        basename = os.path.basename(path)
        if not os.path.exists(path):
            msgReply = QMessageBox.question(self,
                                            'Not Found',
                                            '\'' + basename + '\'' + ' file was not found. Would you like to browse for one?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if msgReply == QMessageBox.Yes:
                self.browseVariablePool()

    # use the profile dictionary to update the gui
    def updateGuiFromProfileDict(self):
        try:
            callpath = self.profileDict['Profile']['CallFunctionFolder']
            self.callFunctionEdit.setText(callpath)
            self.checkFolderExist(callpath)
        except:
            self.callFunctionEdit.setText('')

        try:
            csvpath = self.profileDict['Profile']['CSVReportFolder']
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
            checkbox = self.profileDict['Profile']['Version']['@include']
            self.versionCheckBox.setChecked(eval(checkbox))
        except:
            self.versionCheckBox.setChecked(False)

        self.addSignalModel.clear()
        try:
            temp = self.profileDict['Profile']['Log']['Signal']
            signalList = []
            # if temp is a list we iterate and add, else we append a single element
            if isinstance(temp, list):
                signalList.extend(x for x in temp)
            else:
                signalList.append(temp)

            for s in signalList:
                self.addSignalModel.appendRow(QStandardItem(str(s)))
        except KeyError:
            # self.addSignalModel.clear()
            if self.debug: print('Signal list is empty')

        self.dtcExModel.clear()
        try:
            temp = self.profileDict['Profile']['DTC']['Except']
            dtcExList = []
            # if temp is a list we iterate and add, else we append a single element
            if isinstance(temp, list):
                dtcExList.extend(x for x in temp)
            else:
                dtcExList.append(temp)

            for s in dtcExList:
                self.dtcExModel.appendRow(QStandardItem(str(s)))
        except KeyError:
            # self.dtcExModel.clear()
            if self.debug: print('DTCs exception list is empty')

    def loadConfig(self):
        try:
            with open(str(self.configFile), 'rb') as f:
                self.configDict = xmltodict.parse(f.read())
                try:
                    if self.configDict['Config']['@version'] == '1.0':
                        try:
                            self.profileFile = Path(self.configDict['Config']['LastProfile'])
                            self.loadProfile()
                        except:
                            self.statusbar.showMessage(self.profile_notfound_config)
                except KeyError:
                    self.statusbar.showMessage(self.config_invalid)
        except FileNotFoundError:
            self.statusbar.showMessage(self.config_notfound)
            self.setDefaultConfigDict()
            self.setDefaultProfile()
            self.setTitle(self.untitled_profile)

    # load the variable pool from csv file and extract variable names only
    def loadVariablePool(self):
        variablePoolPath = Path(self.variablePoolEdit.text())
        if len(str(variablePoolPath)) > 1:
            try:
                with open(str(variablePoolPath)) as f:
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
        self.setWindowTitle('[' + str(profilePath) + '] - XMLConfig')


    def setProfileDict(self,
                       callfolder='',
                       csvfolder='',
                       varpoolpath='',
                       includeversion='False',
                       logmode='0',
                       signallist=[],
                       dtcenable='False',
                       dtcexlist=[]):

        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'CallFunctionFolder': callfolder,
                'CSVReportFolder': csvfolder,
                'VariablePoolPath': varpoolpath,
                'Version': {
                    '@include': includeversion
                },
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

    def setConfigDict(self, lastprofile=''):
        self.configDict = {
            'Config': {
                '@version': '1.0',
                'LastProfile': lastprofile
            }
        }

    def setDefaultConfigDict(self):
        self.unsavedChanges()
        # load default config if no params are given
        self.setConfigDict()

    def exit(self):
        if not self.changesSaved:
            msgReply = QMessageBox.question(self, 'Save Changes', 'Would you like to save before exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if msgReply == QMessageBox.Yes:
                self.saveProfile()
                if self.debug: print('File saved')

        self.saveConfig()
        self.updateProfileDict()
        self.close()

    def about(self):
        QMessageBox.about(self, 'About', 'Version 1.0\nAuthor: Vu Le')


def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    # return the profile dict to caller such as AutomationDesk
    return form.profileDict


if __name__ == '__main__':
    main()
