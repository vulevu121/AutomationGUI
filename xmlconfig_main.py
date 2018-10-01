#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import xmltodict
from pathlib import Path
from xmlconfig import *
import sys
import csv

if sys.version_info[0] < 3:
    FileNotFoundError = IOError


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.debug = True

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.changesSaved = True

        # set default xml config file path
        self.configPath = Path('C:/DSConfig/config.xml')
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

    def mousePressEvent(self, event):
        print(event.button())

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
        self.statusbar.showMessage('You have unsaved changes.')

    def newProfile(self):
        self.setDefaultProfile()
        self.setWindowTitle('Untitled Profile - Unsaved')
        self.updateGui()
        self.statusbar.showMessage('Default profile loaded')

    def browseProfile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Profile", "","XML Files (*.xml);;All Files (*)")
        if len(str(filePath)) > 1:
            self.profilePath = Path(filePath)
            self.loadProfile()
            self.saveConfig()

    def browseCallFunction(self):
        folderPath = QFileDialog.getExistingDirectory(self, "Select Call Function Directory", "")
        if len(str(folderPath)) > 1:
            self.callFunctionEdit.setText(str(Path(folderPath)))

    def browseCsvReport(self):
        folderPath = QFileDialog.getExistingDirectory(self, "Select CSV Report Directory", "")
        if len(str(folderPath)):
            self.csvReportEdit.setText(str(Path(folderPath)))

    def browseVariablePool(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Variable Pool", "","TXT Files (*.txt);;All Files (*)")
        if len(str(filePath)) > 1:
            self.variablePoolEdit.setText(str(Path(filePath)))

    def newConfig(self):
        self.setDefaultConfig()
        self.setWindowTitle('Untitled Profile - Unsaved')
        self.unsavedChanges()

    def saveProfile(self):
        # updates dictionary and convert to xml for saving
        self.profileDict['profile']['callFunctionPath'] = self.callFunctionEdit.text()
        self.profileDict['profile']['csvPath'] = self.csvReportEdit.text()
        self.profileDict['profile']['variablePoolPath'] = self.variablePoolEdit.text()
        self.profileDict['profile']['includeVersion'] = self.versionCheckBox.isChecked()

        logMode = (self.logRadioBtn0.isChecked() + self.logRadioBtn1.isChecked()*2 + self.logRadioBtn2.isChecked()*3) - 1

        signalList = []
        for i in range(0, self.addSignalModel.rowCount()):
            signalList.append(self.addSignalModel.item(i, 0).text())

        self.profileDict['profile']['log'] = {
            '@mode': logMode,
            'signal': signalList
        }

        dtcExList = []
        for i in range(0, self.dtcExModel.rowCount()):
            dtcExList.append(self.dtcExModel.item(i, 0).text())

        self.profileDict['profile']['dtc'] = {
            '@enabled': self.dtcExCheckBox.isChecked(),
            'except': dtcExList
        }

        # save the profile from current dict
        with open(str(self.profilePath), 'wb') as f:
            f.write(bytearray(xmltodict.unparse(self.profileDict, pretty=True), encoding='utf-8'))

        self.setWindowTitle(str(self.profilePath))
        self.statusbar.showMessage('Saving...OK!')
        self.changesSaved = True

    def saveAsProfile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Profile As", "","XML Files (*.xml);;All Files (*)")
        if len(str(filePath)) > 1:
            self.profilePath = Path(filePath)
            self.saveProfile()
            self.saveConfig()

    def addSignal(self):
        signal = self.addSignalEdit.text()
        try:
            self.variablePool.index(signal)
            # check for duplicate signal
            if self.addSignalModel.findItems(signal):
                self.statusbar.showMessage('Duplicate signal')
            else:
                self.addSignalModel.appendRow(QStandardItem(self.addSignalEdit.text()))
                self.addSignalEdit.clear()
                self.addSignalEdit.setFocus()
                self.statusbar.showMessage('Signal added successfully')
        except ValueError:
            self.statusbar.showMessage('Signal not found in variable pool')

    def removeSignal(self):
        self.addSignalModel.removeRow(self.addSignalListView.currentIndex().row())

    def addDtcEx(self):
        self.dtcExModel.appendRow(QStandardItem(self.addDtcExEdit.text()))
        self.addDtcExEdit.clear()
        self.addDtcExEdit.setFocus()
        self.statusbar.showMessage('DTC exception added successfully')

    def removeDtcEx(self):
        self.dtcExModel.removeRow(self.dtcExListView.currentIndex().row())

    def saveConfig(self):
        self.configDict['config']['lastProfile'] = str(self.profilePath)
        try:
            with open(str(self.configPath), 'wb') as f:
                f.write(bytearray(xmltodict.unparse(self.configDict, pretty=True), encoding='utf-8'))
        except FileNotFoundError:
            self.statusbar.showMessage('Cannot open config file for saving.')

    def loadProfile(self):
        try:
            with open(str(self.profilePath), 'rb') as f:
                self.profileDict = xmltodict.parse(f.read())
                try:
                    if self.profileDict['profile']['@version'] == '1.0':
                        # updates the gui after loading a valid profile
                        self.loadVariablePool()
                        self.updateGui()
                        self.setWindowTitle(str(self.profilePath))
                        self.statusbar.showMessage('Profile loaded successfully')
                except KeyError:
                    self.statusbar.showMessage('Invalid profile detected')
        except FileNotFoundError:
            self.setWindowTitle('Profile does not exist. Please load profile.')
            self.statusbar.showMessage('Profile does not exist. Please load profile.')

    # use the profile dictionary to update the gui
    def updateGui(self):
        self.callFunctionEdit.setText(self.profileDict['profile']['callFunctionPath'])
        self.csvReportEdit.setText(self.profileDict['profile']['csvPath'])
        self.variablePoolEdit.setText(self.profileDict['profile']['variablePoolPath'])

        self.versionCheckBox.setChecked(eval(self.profileDict['profile']['includeVersion']))

        # self.versionCheckBox.setChecked(self.profileDict['profile']['includeVersion'])

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
        # showRelease(self.profileDict['config']['release'])

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
        # showLogMode(self.profileDict['profile']['logMode'])

        self.addSignalModel.clear()
        try:
            signalList = self.profileDict['profile']['log']['signal']
            # if signalList is a single string then we don't need to iterate
            if isinstance(signalList, str):
                self.addSignalModel.appendRow(QStandardItem(signalList))
            # else if signalList is a list, then iterate
            elif isinstance(signalList, list):
                for s in signalList:
                    self.addSignalModel.appendRow(QStandardItem(str(s)))
        except KeyError:
            if self.debug: print('Signal list is empty')

        self.dtcExModel.clear()
        try:
            dtcExList = self.profileDict['profile']['dtc']['except']
            # if dtcExList is a string then we don't need to iterate
            if isinstance(dtcExList, str):
                self.dtcExModel.appendRow(QStandardItem(dtcExList))
            # else if dtcExList is a list, then iterate
            elif isinstance(dtcExList, list):
                for d in dtcExList:
                    self.dtcExModel.appendRow(QStandardItem(str(d)))
        except KeyError:
            self.addSignalModel.clear()
            if self.debug: print('DTCs exception list is empty')

    def loadConfig(self):
        try:
            with open(str(self.configPath), 'rb') as f:
                self.configDict = xmltodict.parse(f.read())
                try:
                    if self.configDict['config']['@version'] == '1.0':
                        try:
                            self.profilePath = Path(self.configDict['config']['lastProfile'])
                            self.loadProfile()
                        except KeyError:
                            self.statusbar.showMessage('No last profile defined in config')
                except KeyError:
                    if self.debug: print('Invalid config file detected')
                    self.statusbar.showMessage('Invalid config file detected')
        except FileNotFoundError:
            self.setDefaultConfig()
            self.statusbar.showMessage('Config file does not exist')
            self.setWindowTitle('Config file does not exist')

    # load the variable pool from csv file and extract variable names only
    def loadVariablePool(self):
        variablePoolPath = Path(self.variablePoolEdit.text())
        if len(str(variablePoolPath)) > 1:
            try:
                with open(variablePoolPath) as f:
                    self.variablePool = []
                    self.variablePool.extend(row['VariableName'] for row in csv.DictReader(f))
                    self.statusbar.showMessage('Variable pool loaded successfully')
            except FileNotFoundError:
                self.statusbar.showMessage('Variable pool file does not exist.')

    def setDefaultProfile(self):
        self.profileDict = {
            'profile': {
                '@version': '1.0',
                'callFunctionPath': '',
                'csvPath': '',
                'variablePoolPath': '',
                'includeVersion': 'False',
                'log': {
                    '@mode': '0'
                },
                'dtc': {
                    '@enabled': 'False'
                }
            }
        }

    def setDefaultConfig(self):
        self.configDict = {
            'config': {
                '@version': '1.0',
                'lastProfile': ''
            }
        }

    def exit(self):
        if not self.changesSaved:
            msgReply = QMessageBox.question(self, 'Save Changes', 'Would you like to save before exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if msgReply == QMessageBox.Yes:
                self.saveProfile()
                if self.debug: print('File saved')
        self.close()

    def about(self):
        QMessageBox.about(self, 'About', 'Version 1.0\nAuthor: Vu Le')


def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
