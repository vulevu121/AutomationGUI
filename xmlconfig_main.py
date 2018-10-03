#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
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
        self.debug = True

        # create a frameless window without titlebar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

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
        self.configPath = Path('C:/DS_Config/config.xml')
        self.profilePath = Path('')
        self.variablePoolPath = Path('')

        self.configDict = {}
        self.profileDict = {}
        self.variablePool = []

        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)

        self.dtcExModel = QStandardItemModel()
        self.dtcExListView.setModel(self.dtcExModel)

        # self.addSignalListView.clicked.connect(self.addSignalListViewChanged)

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

    def hideAddSignal(self):
        self.addSignalLabel.hide()
        self.addSignalListView.hide()
        self.addSignalBtn.hide()
        self.addSignalEdit.hide()
        self.removeSignalBtn.hide()

    def showAddSignal(self):
        self.addSignalLabel.show()
        self.addSignalListView.show()
        self.addSignalBtn.show()
        self.addSignalEdit.show()
        self.removeSignalBtn.show()

    def dtcExToggle(self):
        if self.dtcExCheckBox.isChecked():
            self.showDtcException()
        else:
            self.hideDtcException()

    def hideDtcException(self):
        self.dtcExListView.hide()
        self.addDtcExEdit.hide()
        self.addDtcExBtn.hide()
        self.removeDtcExBtn.hide()

    def showDtcException(self):
        self.dtcExListView.show()
        self.addDtcExEdit.show()
        self.addDtcExBtn.show()
        self.removeDtcExBtn.show()

    def addSignalListViewChanged(self):
        print(self.addSignalListView.currentIndex().row())

    def unsavedChanges(self):
        self.changesSaved = False
        self.statusbar.showMessage(self.unsaved_changes)

    def newProfile(self):
        self.setDefaultProfile()
        self.profilePath = ''
        self.setTitle(self.untitled_profile)
        self.updateGUI()
        self.statusbar.showMessage(self.default_profile_loaded)

    def browseProfile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, "Open Profile", "","XML Files (*.xml);;All Files (*)")
        if filePath:
            self.profilePath = Path(filePath)
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
        self.setDefaultConfig()
        self.unsavedChanges()

    def saveProfile(self):
        if self.defaultProfile:
            filePath, fileType = QFileDialog.getSaveFileName(self, "Save Profile As", "",
                                                             "XML Files (*.xml);;All Files (*)")
            if filePath:
                self.profilePath = Path(filePath)

        # save config file as well
        self.saveConfig()
        # updates the profile dict before unparsing to xml
        self.updateProfileDict()

        # save the profile from profile dict
        try:
            with open(str(self.profilePath), 'wb') as f:
                if self.debug: print(str(self.profilePath))
                f.write(bytearray(xmltodict.unparse(self.profileDict, pretty=True), encoding='utf-8'))
                self.setTitle(self.profilePath)
                self.defaultProfile = False
                self.changesSaved = True
                self.statusbar.showMessage(self.profile_save_success)
        except FileNotFoundError:
            self.statusbar.showMessage(self.profile_save_fail)

    def saveAsProfile(self):
        filePath, fileType = QFileDialog.getSaveFileName(self, "Save Profile As", "","XML Files (*.xml);;All Files (*)")

        if filePath:
            self.profilePath = Path(filePath)
            self.saveProfile()

    # updates the profile dict
    def updateProfileDict(self):
        # updates dictionary and convert to xml for saving
        # self.profileDict['Profile']['CallFunctionFolder'] = self.callFunctionEdit.text()
        # self.profileDict['Profile']['CSVReportFolder'] = self.csvReportEdit.text()
        # self.profileDict['Profile']['VariablePoolPath'] = self.variablePoolEdit.text()
        # self.profileDict['Profile']['IncludeVersion'] = self.versionCheckBox.isChecked()

        logMode = (self.logRadioBtn0.isChecked() + self.logRadioBtn1.isChecked()*2 + self.logRadioBtn2.isChecked()*3) - 1

        # update signal list
        signalList = []
        for i in range(0, self.addSignalModel.rowCount()):
            signalList.append(self.addSignalModel.item(i, 0).text())

        # self.profileDict['Profile']['Log'] = {
        #     '@mode': logMode,
        #     'Signal': signalList
        # }

        # update dtc exception list
        dtcExList = []
        for i in range(0, self.dtcExModel.rowCount()):
            dtcExList.append(self.dtcExModel.item(i, 0).text())

        # self.profileDict['Profile']['DTC'] = {
        #     '@enable': self.dtcExCheckBox.isChecked(),
        #     'Except': dtcExList
        # }
        
        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'CallFunctionFolder': self.callFunctionEdit.text(),
                'CSVReportFolder': self.csvReportEdit.text(),
                'VariablePoolPath': self.variablePoolEdit.text(),
                'IncludeVersion': self.versionCheckBox.isChecked(),
                'Log': {
                    '@mode': logMode,
                    'Signal': signalList
                },
                'DTC': {
                    '@enable': self.dtcExCheckBox.isChecked(),
                    'Except': dtcExList
                }
            }
        }

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
        self.configDict['Config']['LastProfile'] = str(self.profilePath)

        # if config folder not found, create one
        dirname = os.path.dirname(str(self.configPath))

        if not os.path.exists(dirname):
            os.mkdir(dirname)

        with open(str(self.configPath), 'wb') as f:
            f.write(bytearray(xmltodict.unparse(self.configDict, pretty=True), encoding='utf-8'))

    def loadProfile(self):
        try:
            with open(str(self.profilePath), 'rb') as f:
                self.profileDict = xmltodict.parse(f.read())
                try:
                    if self.profileDict['Profile']['@version'] == '1.0':
                        # updates the gui after loading a valid profile
                        self.defaultProfile = False
                        self.updateGUI()
                        self.loadVariablePool()
                        self.setTitle(self.profilePath)
                        self.statusbar.showMessage(self.profile_loaded_success)
                except KeyError:
                    self.statusbar.showMessage(self.profile_invalid)
        except FileNotFoundError:
            self.newProfile()
            self.statusbar.showMessage(self.profile_does_not_exist)

    # use the profile dictionary to update the gui
    def updateGUI(self):
        self.callFunctionEdit.setText(self.profileDict['Profile']['CallFunctionFolder'])
        self.csvReportEdit.setText(self.profileDict['Profile']['CSVReportFolder'])
        self.variablePoolEdit.setText(self.profileDict['Profile']['VariablePoolPath'])
        self.versionCheckBox.setChecked(eval(self.profileDict['Profile']['IncludeVersion']))

        # self.versionCheckBox.setChecked(self.profileDict['Profile']['IncludeVersion'])

        # def betaRelease():
        #     self.betaRadioBtn.setChecked(True)
        #
        # def rcRelease():
        #     self.rcRadioBtn.setChecked(True)
        #
        # def showRelease(arg):
        #     switcher = {
        #         'beta': betaRelease,
        #         'rc': rcRelease
        #     }
        #     switcher.get(arg)()
        #
        # showRelease(self.profileDict['Config']['release'])

        # def logMode0():
        #     self.logRadioBtn0.setChecked(True)
        #
        # def logMode1():
        #     self.logRadioBtn1.setChecked(True)
        #
        # def logMode2():
        #     self.logRadioBtn2.setChecked(True)
        #
        # def showLogMode(arg):
        #     switcher = {
        #         '0': logMode0,
        #         '1': logMode1,
        #         '2': logMode2
        #     }
        #     switcher.get(arg)()
        #
        # showLogMode(self.profileDict['Profile']['logMode'])

        self.addSignalModel.clear()
        try:
            signalList = self.profileDict['Profile']['Log']['Signal']
            print(signalList)
            # if signalList is a single string then we don't need to iterate
            if isinstance(signalList, str):
                self.addSignalModel.appendRow(QStandardItem(str(signalList)))
            # else if signalList is a list, then iterate
            elif isinstance(signalList, list):
                for s in signalList:
                    self.addSignalModel.appendRow(QStandardItem(str(s)))
        except KeyError:
            # self.addSignalModel.clear()
            if self.debug: print('Signal list is empty')

        self.dtcExModel.clear()
        try:
            dtcExList = self.profileDict['Profile']['DTC']['Except']
            # if dtcExList is a string then we don't need to iterate
            if isinstance(dtcExList, str):
                self.dtcExModel.appendRow(QStandardItem(dtcExList))
            # else if dtcExList is a list, then iterate
            elif isinstance(dtcExList, list):
                for d in dtcExList:
                    self.dtcExModel.appendRow(QStandardItem(str(d)))
        except KeyError:
            # self.dtcExModel.clear()
            if self.debug: print('DTCs exception list is empty')

    def loadConfig(self):
        try:
            with open(str(self.configPath), 'rb') as f:
                self.configDict = xmltodict.parse(f.read())
                try:
                    if self.configDict['Config']['@version'] == '1.0':
                        try:
                            self.profilePath = Path(self.configDict['Config']['LastProfile'])
                            self.loadProfile()
                        except KeyError:
                            self.statusbar.showMessage(self.profile_notfound_config)
                except KeyError:
                    self.statusbar.showMessage(self.config_invalid)
        except FileNotFoundError:
            self.statusbar.showMessage(self.config_notfound)
            self.setDefaultConfig()
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
                    self.statusbar.showMessage(self.variable_pool_loaded_success)
            except FileNotFoundError:
                self.statusbar.showMessage(self.variable_pool_notfound)

    def setTitle(self, profilePath):
        self.setWindowTitle('[' + str(profilePath) + '] - XMLConfig')

    def setDefaultProfile(self):
        self.defaultProfile = True
        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'CallFunctionFolder': '',
                'CSVReportFolder': '',
                'VariablePoolPath': '',
                'IncludeVersion': 'False',
                'Log': {
                    '@mode': '0'
                },
                'DTC': {
                    '@enable': 'False'
                }
            }
        }

    def setDefaultConfig(self):
        self.configDict = {
            'Config': {
                '@version': '1.0',
                'LastProfile': ''
            }
        }

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
    return form.profileDict


if __name__ == '__main__':
    main()
