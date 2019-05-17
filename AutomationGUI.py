#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 5/13/19 Changelog
# Added toolbar for polarion and dspace tabs
# Improved thread handling between gui and reading excel files
# Added polarion log view

# 5/9/19 Changelog
# Added Polarion service support
# Added hyperlink tracking for jiras, etc.

# 5/6/19 Changelog
# Added loading bar
# Added dSpace excel reading
# Added Polarion excel reading
# Added Polarion excel revision number
# Added threading for excel reading


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import xmltodict
from pathlib import Path
from AutomationGUI_ui import *
import os
import sys
import strings
import csv
import re
from datetime import datetime
from openpyxl import load_workbook
from collections import OrderedDict
import webbrowser
# from functools import partial # used for calling with args

# polarion related libs
from zeep import Client
from requests import Session
from zeep.transports import Transport
from lxml import etree
import copy
import time

if sys.version_info[0] < 3:
    FileNotFoundError = IOError

debug = False
version = 'v1.5.2'

def debugPrint(msg):
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
        # dict to hold data from all log files
        self.logDict = OrderedDict()
        # dict to hold data from polarion sheet
        self.runDict = OrderedDict()
        self.polarionDict = OrderedDict()
        self.polarionWs = None
        self.polarionWb = None
        self.variablePoolDict = {}
        self.updateVariablePool = False  # update variable pool in AutomationDesk
        self.defaultProfile = True  # false when a profile is loaded

        # progress bar
        self.progressBarTimer = QTimer()
        self.progressBarTimer.timeout.connect(self.progressBarAnimation)

        # Qt item models
        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)

        self.dtcExModel = QStandardItemModel()
        self.dtcExListView.setModel(self.dtcExModel)

        self.loadConfig()
        self.changesSaved = True

        # general tab
        self.browsePolarionExcelBtn.clicked.connect(self.browsePolarionExcel)
        self.browseTestCaseExcelBtn.clicked.connect(self.browseTestCaseExcel)
        self.browseCallFunctionBtn.clicked.connect(self.browseCallFunction)
        self.browseCsvReportBtn.clicked.connect(self.browseCsvReport)
        self.browseVariablePoolBtn.clicked.connect(self.browseVariablePool)

        self.polarionExcelEdit.textChanged.connect(self.unsavedChanges)
        self.polarionExcelEdit.textChanged.connect(self.usePolarionExcelFolderForLogs)
        self.testCaseExcelEdit.textChanged.connect(self.unsavedChanges)
        self.testCaseExcelEdit.textChanged.connect(self.useTestCaseFolderForLogs)
        self.callFunctionEdit.textChanged.connect(self.unsavedChanges)
        self.csvReportEdit.textChanged.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)
        self.variablePoolEdit.textChanged.connect(self.unsavedChanges)
        self.reloadVariablePoolBtn.clicked.connect(self.loadVariablePool)

        # polarion excel toolbutton
        self.polarionExcelMenu = QMenu()

        openPolarionExcelFileAction = QAction(QIcon(':/icon/excelBlackIcon'), 'Open Test Case File', self)
        openPolarionExcelFileAction.triggered.connect(self.openPolarionExcelFile)
        self.polarionExcelMenu.addAction(openPolarionExcelFileAction)


        openPolarionExcelFolderAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Open Test Case Folder', self)
        openPolarionExcelFolderAction.triggered.connect(self.openPolarionExcelFolder)
        self.polarionExcelMenu.addAction(openPolarionExcelFolderAction)

        self.polarionExcelToolButton.setMenu(self.polarionExcelMenu)

        # test case excel toolbutton
        testCaseExcelMenu = QMenu()

        openTestCaseExcelFileAction = QAction(QIcon(':/icon/excelBlackIcon'), 'Open Test Case File', self)
        openTestCaseExcelFileAction.triggered.connect(self.openTestCaseExcelFile)
        testCaseExcelMenu.addAction(openTestCaseExcelFileAction)

        openTestCaseExcelFolderAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Open Test Case Folder', self)
        openTestCaseExcelFolderAction.triggered.connect(self.openTestCaseExcelFolder)
        testCaseExcelMenu.addAction(openTestCaseExcelFolderAction)

        self.testCaseExcelToolButton.setMenu(testCaseExcelMenu)

        # csv report toolbutton
        csvReportFolderMenu = QMenu()

        openCsvReportFolderAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Open Report Folder', self)
        openCsvReportFolderAction.triggered.connect(self.openCsvReportFolder)
        csvReportFolderMenu.addAction(openCsvReportFolderAction)

        useTestCasePathAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Use {TestCaseFolder}\\Logs', self)
        useTestCasePathAction.triggered.connect(self.useTestCasePath)
        csvReportFolderMenu.addAction(useTestCasePathAction)

        self.csvReportFolderToolButton.setMenu(csvReportFolderMenu)

        # call function toolbutton
        callFunctionFolderMenu = QMenu()

        openCallFunctionFolderAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Open Call Function Folder', self)
        openCallFunctionFolderAction.triggered.connect(self.openCallFunctionFolder)
        callFunctionFolderMenu.addAction(openCallFunctionFolderAction)

        self.callFunctionFolderToolButton.setMenu(callFunctionFolderMenu)

        # variable pool toolbutton
        variablePoolMenu = QMenu()

        openVariablePoolFileAction = QAction(QIcon(':/icon/copyIcon'), 'Open Variable Pool File', self)
        openVariablePoolFileAction.triggered.connect(self.openVarPoolFile)
        variablePoolMenu.addAction(openVariablePoolFileAction)

        openVariablePoolFolderAction = QAction(QIcon(':/icon/folderOpenIcon'), 'Open Variable Pool Folder', self)
        openVariablePoolFolderAction.triggered.connect(self.openVarPoolFolder)
        variablePoolMenu.addAction(openVariablePoolFolderAction)

        self.variablePoolToolButton.setMenu(variablePoolMenu)

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

        # run list tab
        self.dSpaceReadExcelButton.clicked.connect(self.dSpaceReadExcelStart)
        self.runTableViewModel = QStandardItemModel()
        self.runTableView.setModel(self.runTableViewModel)

        self.copyButton.clicked.connect(self.copyRunList)
        self.runTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.runTableView.customContextMenuRequested.connect(self.runTableContextMenuEvent)

        # polarion tab
        self.polarionReadExcelButton.clicked.connect(self.polarionReadExcelStart)
        self.polarionTableViewModel = QStandardItemModel()
        self.polarionTableView.setModel(self.polarionTableViewModel)
        self.polarionTableView.clicked.connect(self.polarionTableViewClicked)

        self.polarionUpdatePassedButton.clicked.connect(lambda: self.polarionUpdateExcel('Passed'))
        self.polarionUpdateAllButton.clicked.connect(lambda: self.polarionUpdateExcel('All'))
        self.polarionSaveExcelButton.clicked.connect(self.polarionSaveExcel)
        self.polarionUpdateRevisionButton.clicked.connect(self.udpatePolarionRevision)
        self.updateHyperlinksButton.clicked.connect(self.updateHyperlinks)
        self.updateStepsButton.clicked.connect(self.updatePolarionSteps)

        # self.polarionTableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.polarionTableView.customContextMenuRequested.connect(self.polarionTableContextMenuEvent)

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

        self.tabWidget.setCurrentIndex(0)
        self.logRadioBtn0.setChecked(True)
        self.hideAddSignal()

        self.autorunCheckBox.clicked.connect(self.autoRunClicked)

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

    def progressBarAnimation(self):
        value = self.progressBar.value()
        self.progressBar.setValue(0 if value > 99 else value + 4)

    def showLoadingBar(self):
        self.progressBarTimer.start(40)

    def hideLoadingBar(self):
        self.progressBarTimer.stop()
        self.progressBar.setValue(0)

    def runTableContextMenuEvent(self, qpoint):
        menu = QMenu(self)

        modelIndex = self.runTableView.indexAt(qpoint)
        item = self.runTableViewModel.itemFromIndex(modelIndex)

        if modelIndex.column() == 0:
            copyAction = QAction(QIcon(':/icon/copyIcon'), 'Copy', self)
            copyAction.triggered.connect(self.copySelectionRunTable)
            menu.addAction(copyAction)

        if menu.actions().__len__() > 0:
            menu.popup(QCursor.pos())

    def polarionTableContextMenuEvent(self, qpoint):
        menu = QMenu(self)

        modelIndex = self.polarionTableView.indexAt(qpoint)
        item = self.polarionTableViewModel.itemFromIndex(modelIndex)

        if modelIndex.column() == 0:
            copyAction = QAction(QIcon(':/icon/copyIcon'), 'Copy', self)
            copyAction.triggered.connect(self.copySelectionPolarionTable)
            menu.addAction(copyAction)

        if modelIndex.column() == 5:
            hyperlink = item.text()
            if len(hyperlink) > 0:
                openLinkAction = QAction(QIcon(':/icon/linkIcon'), 'Open Hyperlink', self)
                openLinkAction.triggered.connect(lambda: self.openHyperlink(hyperlink))
                menu.addAction(openLinkAction)

        if menu.actions().__len__() > 0:
            menu.popup(QCursor.pos())

    def polarionTableViewClicked(self, qmodelindex):
        # QModelIndex
        row = qmodelindex.row()
        column = qmodelindex.column()
        if column == 0:
            item = self.polarionTableViewModel.item(row, column)
            testCaseId = item.text()
            checked = item.checkState() == 2
            # print(row, column, testCaseId, checked)
            self.polarionDict[testCaseId]['update'] = checked

    def copySelectionRunTable(self):
        if self.runTableView.model():
            selectionModel = self.runTableView.selectionModel()

            copyList = []

            for each in selectionModel.selectedIndexes():
                item = self.runTableViewModel.item(each.row(), each.column())
                copyList.append(item.text())

            copyString = '\n'.join(copyList)

            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(copyString, mode=cb.Clipboard)
        else:
            print("No model found")

    def copySelectionPolarionTable(self):
        if self.polarionTableView.model():
            selectionModel = self.polarionTableView.selectionModel()

            copyList = []

            for each in selectionModel.selectedIndexes():
                item = self.polarionTableViewModel.item(each.row(), each.column())
                copyList.append(item.text())

            copyString = '\n'.join(copyList)

            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(copyString, mode=cb.Clipboard)
        else:
            print("No model found")

    def openHyperlink(self, link):
        if len(link) > 0:
            linkSplit = link.split(',')

            for l in linkSplit:
                webbrowser.open_new_tab(l)

    def autoRunClicked(self):
        if self.autorunCheckBox.isChecked():
            self.startTimer.start(1000)
            self.startTimerCount = self.autorunSpinBox.value()
        else:
            self.startTimer.stop()
            self.autorunCheckBox.setText('Autorun')

    def tick(self):
        if self.startTimerCount > 0:
            self.autorunCheckBox.setText('Autorun in {}s'.format(self.startTimerCount))
            # self.exitButton.setText('Continue ({})'.format(self.startTimerCount))
            debugPrint(self.startTimerCount)
            self.startTimerCount = self.startTimerCount - 1
        else:
            self.startTimer.stop()
            debugPrint('Timer stop')
            self.autorunCheckBox.setText('Autorun')
            # self.exitButton.setText('Continue')
            if self.autorunCheckBox.isChecked():
                self.exit()

    def toggleDebug(self):
        debug = self.showDebugCheckBox.isChecked()
        print('ShowDebug={}'.format(debug))

    def toggleUpdateVariablePool(self):
        self.updateVariablePool = self.updateVariablePoolCheckBox.isChecked()
        debugPrint('UpdateVariablePool={}'.format(self.updateVariablePool))

    def openCallFunctionFolder(self):
        callFunctionPath = Path(self.callFunctionEdit.text())
        if os.path.exists(str(callFunctionPath)):
            os.startfile(str(callFunctionPath))

    def openCsvReportFolder(self):
        csvReportPath = Path(self.csvReportEdit.text())
        if os.path.exists(str(csvReportPath)):
            os.startfile(str(csvReportPath))

    def openVarPoolFolder(self):
        varPoolPath = Path(self.variablePoolEdit.text())
        dirName = os.path.dirname(str(varPoolPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(dirName))

    def openVarPoolFile(self):
        varPoolPath = Path(self.variablePoolEdit.text())
        dirName = os.path.dirname(str(varPoolPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(varPoolPath))

    def openPolarionExcelFolder(self):
        polarionExcelPath = Path(self.polarionExcelEdit.text())
        dirName = os.path.dirname(str(polarionExcelPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(dirName))

    def openPolarionExcelFile(self):
        polarionExcelPath = Path(self.polarionExcelEdit.text())
        dirName = os.path.dirname(str(polarionExcelPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(polarionExcelPath))

    def openTestCaseExcelFolder(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirName = os.path.dirname(str(testCaseExcelPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(dirName))

    def openTestCaseExcelFile(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirName = os.path.dirname(str(testCaseExcelPath))
        if os.path.exists(str(dirName)):
            os.startfile(str(testCaseExcelPath))

    def openConfigFolder(self):
        configFolder = os.path.dirname(str(self.configFile))
        # param = 'explorer "{}"'.format(configFolder)
        # subprocess.Popen(param)
        if os.path.exists(configFolder):
            os.startfile(configFolder)

    def useTestCasePath(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirName = os.path.dirname(str(testCaseExcelPath))
        newCsvReportFolder = os.path.join(dirName, 'Logs')
        self.csvReportEdit.setText(str(newCsvReportFolder))
        if not os.path.exists(newCsvReportFolder):
            os.mkdir(newCsvReportFolder)

    def useTestCaseFolderForLogs(self):
        testCaseExcelPath = Path(self.testCaseExcelEdit.text())
        dirName = os.path.dirname(str(testCaseExcelPath))
        newCsvReportFolder = os.path.join(dirName, 'Logs')

        if os.path.exists(dirName):
            msgReply = QMessageBox.question(
                self,
                'CSV Report Folder',
                'Use [' + str(newCsvReportFolder) + '] to store reports?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if msgReply == QMessageBox.Yes:
                newCsvReportFolder = os.path.join(dirName, 'Logs')
                self.csvReportEdit.setText(str(newCsvReportFolder))
                if not os.path.exists(newCsvReportFolder):
                    os.mkdir(newCsvReportFolder)

    def usePolarionExcelFolderForLogs(self):
        testCaseExcelPath = Path(self.polarionExcelEdit.text())
        dirName = os.path.dirname(str(testCaseExcelPath))
        newCsvReportFolder = os.path.join(dirName, 'Logs')

        if os.path.exists(dirName):
            msgReply = QMessageBox.question(
                self,
                'CSV Report Folder',
                'Use [' + str(newCsvReportFolder) + '] to store reports?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if msgReply == QMessageBox.Yes:
                newCsvReportFolder = os.path.join(dirName, 'Logs')
                self.csvReportEdit.setText(str(newCsvReportFolder))
                if not os.path.exists(newCsvReportFolder):
                    os.mkdir(newCsvReportFolder)

    def hideAddSignal(self):
        self.addSignalGroupBox.hide()

    def showAddSignal(self):
        self.addSignalGroupBox.show()

    def dtcExToggle(self):
        self.showDtcException(self.dtcExCheckBox.isChecked())

    def showDtcException(self, visible=True):
        if visible:
            self.dtcExGroupBox.show()
        else:
            self.dtcExGroupBox.hide()

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
        profileFolder = os.path.dirname(str(self.profileFile))
        filePath, fileType = QFileDialog.getOpenFileName(
            self,
            "Open Profile",
            profileFolder,
            "XML Files (*.xml);;All Files (*)"
        )

        if filePath:
            self.profileFile = Path(filePath)
            self.loadProfile()
            self.saveConfig()

    def browsePolarionExcel(self):
        self.browseFile(
            self.polarionExcelEdit,
            'Select Polarion TestCase Excel File',
            'Excel Files (*.xlsx)'
        )

    def browseTestCaseExcel(self):
        self.browseFile(
            self.testCaseExcelEdit,
            'Select Test Case Excel File',
            'Excel Files (*.xlsm)'
        )

    def browseCallFunction(self):
        self.browseFolder(self.callFunctionEdit, 'Select Call Function Directory')

    def browseCsvReport(self):
        self.browseFolder(self.csvReportEdit, 'Select CSV Report Directory')

    def browseVariablePool(self):
        self.browseFile(self.variablePoolEdit, 'Open Variable Pool', 'TXT Files (*.txt)')

    def browseFile(self, editBox, titleDialog, fileType):
        if len(editBox.text()) > 0:
            folder = str(os.path.dirname(editBox.text()))
        else:
            folder = ''

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
        configFolder = os.path.dirname(str(self.configFile))

        if self.defaultProfile:
            filePath, fileType = QFileDialog.getSaveFileName(
                self,
                "Save Profile As",
                configFolder,
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
                debugPrint(str(self.profileFile))
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
        profileFolder = os.path.dirname(str(self.profileFile))
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Save Profile As",
            profileFolder,
            "XML Files (*.xml);;All Files (*)"
        )

        if filePath:
            self.profileFile = Path(filePath)
            self.saveProfile()

    def updateProfileDictFromGui(self):
        """Updates the profile dict from GUI elements."""

        # generate the log mode number based on checkboxes
        logMode = (self.logRadioBtn0.isChecked() + self.logRadioBtn1.isChecked() * 2 + self.logRadioBtn2.isChecked() * 3) - 1

        # update signal list
        signalList = []
        for i in range(0, self.addSignalModel.rowCount()):
            signalList.append(self.addSignalModel.item(i, 0).text())

        # update dtc exception list
        dtcExList = []

        # update the the dtc exception list from the view
        for i in range(0, self.dtcExModel.rowCount()):
            dtcExList.append(self.dtcExModel.item(i, 0).text())

        # self.setProfileDict(
        #     testcaseexcel=self.testCaseExcelEdit.text(),
        #     callfolder=self.callFunctionEdit.text(),
        #     csvfolder=self.csvReportEdit.text(),
        #     varpoolpath=self.variablePoolEdit.text(),
        #     callfuncdebug=self.callFunctionDebugCheckbox.isChecked(),
        #     includeversion=self.versionCheckBox.isChecked(),
        #     logmode=logMode,
        #     signallist=signalList,
        #     dtcenable=self.dtcExCheckBox.isChecked(),
        #     dtcexlist=dtcExList,
        #     updatevp=self.updateVariablePool
        # )

        self.profileDict = {
            'Profile': {
                '@version': '1.0',
                'PolarionExcel': self.polarionExcelEdit.text(),
                'TestCaseExcel': self.testCaseExcelEdit.text(),
                'CallFunctionFolder': self.callFunctionEdit.text(),
                'CSVReportFolder': self.csvReportEdit.text(),
                'VariablePoolPath': self.variablePoolEdit.text(),
                'UpdateVariablePool': self.updateVariablePool,
                'Version': {'@include': self.versionCheckBox.isChecked()},
                'CallFunctionDebug': {'@enable': self.callFunctionDebugCheckbox.isChecked()},
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
        dirName = os.path.dirname(str(self.configFile))

        if not os.path.exists(dirName):
            os.mkdir(dirName)

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
                    debugPrint('Unable to parse profile XML file.')

                profileValid = True

                try:
                    profileversion = self.profileDict['Profile']['@version']
                    if profileversion == '1.0':
                        profileValid &= True
                    else:
                        debugPrint('Invalid profile version.')
                except:
                    debugPrint('No profile version defined.')

                try:
                    varpoolfile = self.profileDict['Profile']['VariablePoolPath']
                    if not os.path.exists(str(varpoolfile)):
                        self.statusbar.showMessage(strings.VARIABLE_POOL_NOTFOUND)
                    profileValid &= True
                except:
                    debugPrint('No variable pool file defined in profile.')
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

    class MyItemModel(QStandardItemModel):
        def __init__(self, data=None, header=None, parent=None):
            QStandardItemModel.__init__(self, parent)

            for i, d in enumerate(data):
                self.setItem(i, 0, QStandardItem(d))
                for j, p in enumerate(list(data[d].keys())):
                    item = QStandardItem(str(data[d][p]))
                    # item.setCheckable(True)
                    self.setItem(i, j + 1, item)

            self.setHorizontalHeaderLabels(header)


    # read all log files and extract data
    def getLogDict(self):
        csvReportFolder = self.csvReportEdit.text()

        # enumerate the log folder and determine the latest log files
        for fileName in os.listdir(csvReportFolder):
            if fileName.endswith('.csv'):
                filePath = os.path.join(csvReportFolder, fileName)
                lastModTime = datetime.fromtimestamp(os.path.getmtime(filePath))
                testCaseName = fileName.split('_')[2]

                passList = []
                testCaseVerdict = ''
                testComment = ''
                actualResult = []
                length = 0

                testCase = testCaseName.rstrip('.csv')

                try:
                    # if testcase exist in dict, then we update it with latest csv filepath and modified date
                    if lastModTime > self.logDict[testCase]['lastModTime']:
                        self.logDict[testCase]['filePath'] = filePath
                        self.logDict[testCase]['lastModTime'] = lastModTime
                except KeyError:
                    # create key-value pairs if test case does not exist in dict
                    self.logDict[testCase] = {'filePath': filePath,
                                         'lastModTime': lastModTime,
                                         'testCaseVerdict': testCaseVerdict,
                                         'testComment': testComment,
                                         'actualResult': actualResult,
                                         'passList': passList,
                                         'length': length}

        # grab the data from all latest log files
        for t in self.logDict:
            passList = []
            testCaseVerdict = ''
            testComment = ''
            actualResult = []

            with open(self.logDict[t]['filePath']) as csvFile:
                csvReader = csv.DictReader(csvFile)
                for row in csvReader:
                    passList.append(row['Step Verdict'])
                    actualResult.append(row['Actual Result'])
                    if len(row['Test Case Verdict']) > 0:
                        testCaseVerdict = row['Test Case Verdict']
                    if len(row['Test Comment']) > 0:
                        testComment = row['Test Comment']

            self.logDict[t]['testCaseVerdict'] = testCaseVerdict
            self.logDict[t]['testComment'] = testComment
            self.logDict[t]['actualResult'] = actualResult
            self.logDict[t]['passList'] = passList
            self.logDict[t]['length'] = len(passList)

    # read excel file and figure out which test cases need to rerun
    def dSpaceReadExcelStart(self):

        class dSpaceReadExcelThread(QThread):
            signal = pyqtSignal('PyQt_PyObject')

            def __init__(self, parent):
                QThread.__init__(self)
                self.runDict = None
                self.getLogDict = None
                self.logDict = None
                self.testCaseExcelFile = None

            def run(self):
                print('Reading dSpace excel...')

                # grab the active worksheet
                wb = load_workbook(self.testCaseExcelFile)
                ws = wb.active

                # grab the test case column
                testCaseColumn = ws['K']

                # less the header name and empty row, get only the test case names
                runList = [str(each.value) for each in testCaseColumn][2:]

                # remove empty or none entries
                while runList[-1] == 'None' or runList[-1] == '':
                    runList.pop()

                self.getLogDict()

                # grab the data from all latest log files
                for testCase in self.logDict:
                    passList = []
                    testCaseVerdict = ''
                    testComment = ''
                    actualResult = []

                    with open(self.logDict[testCase]['filePath']) as csvFile:
                        csvReader = csv.DictReader(csvFile)
                        for row in csvReader:
                            passList.append(row['Step Verdict'])
                            actualResult.append(row['Actual Result'])
                            if len(row['Test Case Verdict']) > 0:
                                testCaseVerdict = row['Test Case Verdict']
                            if len(row['Test Comment']) > 0:
                                testComment = row['Test Comment']

                    self.logDict[testCase]['testCaseVerdict'] = testCaseVerdict
                    self.logDict[testCase]['testComment'] = testComment
                    self.logDict[testCase]['actualResult'] = actualResult
                    self.logDict[testCase]['passList'] = passList
                    self.logDict[testCase]['length'] = len(passList)

                for t in runList:
                    self.runDict[t] = {'run': '', 'testCaseVerdict': ''}
                    try:
                        if self.logDict[t]['testCaseVerdict'] == 'Passed':
                            self.runDict[t]['run'] = 'No'
                        else:
                            self.runDict[t]['run'] = 'Yes'
                        self.runDict[t]['testCaseVerdict'] = self.logDict[t]['testCaseVerdict']
                    except KeyError as error:
                        print('KeyError:', str(error))
                        self.runDict[t]['run'] = 'Yes'
                        self.runDict[t]['testCaseVerdict'] = 'Not Found'

                self.signal.emit('Reading dSpace excel finished.')

        self.showLoadingBar()
        self.dSpaceReadExcelThreadObject = dSpaceReadExcelThread(self)
        self.dSpaceReadExcelThreadObject.runDict = self.runDict
        self.dSpaceReadExcelThreadObject.getLogDict = self.getLogDict
        self.dSpaceReadExcelThreadObject.logDict = self.logDict
        self.dSpaceReadExcelThreadObject.testCaseExcelFile = self.testCaseExcelEdit.text()
        self.dSpaceReadExcelThreadObject.signal.connect(self.updateRunTableViewModel)
        self.dSpaceReadExcelThreadObject.start()

    # update the model for the run table view
    def updateRunTableViewModel(self, msg):
        header = ['TestCase', 'TestCase Verdict', 'Rerun']
        model = self.runTableViewModel

        for i, d in enumerate(self.runDict):
            testCaseId = QStandardItem(d)
            model.setItem(i, 0, testCaseId)

            testCaseVerdict = self.runDict[d]['testCaseVerdict']
            testCaseVerdictItem = QStandardItem(testCaseVerdict)

            if testCaseVerdict == 'Passed':
                testCaseVerdictItem.setIcon(QIcon(':/icon/passedIcon'))
            elif testCaseVerdict == 'Deferred' or testCaseVerdict == 'Error':
                testCaseVerdictItem.setIcon(QIcon(':/icon/failedIcon'))

            model.setItem(i, 1, testCaseVerdictItem)

            runItem = QStandardItem(str(self.runDict[d]['run']))
            model.setItem(i, 2, runItem)

            # for j, p in enumerate(list(self.runDict[d].keys())):
            #     item = QStandardItem(str(self.runDict[d][p]))
            #     # item.setCheckable(True)
            #     model.setItem(i, j + 1, item)

        model.setHorizontalHeaderLabels(header)
        self.runTableView.resizeColumnsToContents()
        self.runTableView.setColumnWidth(0, 150)

        self.runTableView.setSortingEnabled(True)
        self.runTableView.sortByColumn(0, Qt.AscendingOrder)
        self.runTableView.setAlternatingRowColors(True)

        allTestCaseVerdicts = [self.logDict[x]['testCaseVerdict'] for x in self.logDict]

        passedTotal = allTestCaseVerdicts.count('Passed')
        deferredTotal = allTestCaseVerdicts.count('Deferred')
        errorTotal = allTestCaseVerdicts.count('Error')
        total = passedTotal + deferredTotal + errorTotal

        self.dSpaceOverviewLineEdit.setText(
            'Total Logs Found: {}    Passed: {}    Deferred: {}    Error: {}'.format(total, passedTotal,
                                                                                     deferredTotal, errorTotal))
        self.statusbar.showMessage(msg)
        self.hideLoadingBar()

    def copyRunList(self):
        """Copy the yes/no rerun list to clipboard."""
        selectionModel = self.runTableView.selectionModel()
        selectedIndexes = selectionModel.selectedIndexes()

        self.runTableView.selectColumn(2)

        if selectedIndexes.__len__() > 0:
            copyList = []

            for each in selectedIndexes:
                item = self.runTableViewModel.item(each.row(), each.column())
                copyList.append(item.text())

            copyString = '\n'.join(copyList)

            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(copyString, mode=cb.Clipboard)

            self.statusbar.showMessage('Copy Yes/No successful.')
        else:
            print('Nothing to copy.')

    def polarionReadExcelStart(self):
        """Read and process the polarion excel file in a thread."""
        class polarionReadExcelThread(QThread):
            finishedSignal = pyqtSignal('PyQt_PyObject')
            updatePolarionRevisionSignal = pyqtSignal('PyQt_PyObject')


            def __init__(self):
                QThread.__init__(self)
                self.polarionDict = None
                self.polarionWb = None
                self.polarionWs = None
                self.getLogDict = None
                self.polarionRevisionLineEdit = None

            def run(self):
                print('Reading Polarion excel...')
                # grab necessary columns to work from polarion excel file
                testCaseIdCol = self.polarionWs['A']  # test case names
                stepNumberCol = self.polarionWs['D']  # step numbers

                # get all testcase names and row start
                allSteps = [str(x.value).replace('.0','') for x in stepNumberCol]

                while (allSteps[-1] == 'None' or allSteps[-1] == ''):
                    allSteps.pop()

                # read revision number
                revisionWs = self.polarionWb['_polarion']
                polarionColA = [x.value for x in revisionWs['A']]
                revisionRow = polarionColA.index('testRunRevision') + 1

                revision = str(revisionWs.cell(row=revisionRow, column=2).value)

                self.updatePolarionRevisionSignal.emit(revision)

                startMarker = '1'
                endMarker = '1'

                for eachRow in testCaseIdCol:
                    if re.match('\w+-\w+', str(eachRow.value)) is not None:
                        testCase = str(eachRow.value)
                        # grab the start and end row for each test case
                        start = allSteps.index(startMarker, eachRow.row - 1) + 1
                        try:
                            end = allSteps.index(endMarker, start + 1)
                        except ValueError:
                            end = len(allSteps)

                        self.polarionDict[testCase] = OrderedDict()
                        self.polarionDict[testCase]['startRow'] = start
                        self.polarionDict[testCase]['endRow'] = end
                        self.polarionDict[testCase]['length'] = end - start + 1
                        self.polarionDict[testCase]['testCaseVerdict'] = ''
                        self.polarionDict[testCase]['hyperlinks'] = ''
                        self.polarionDict[testCase]['update'] = True

                self.getLogDict()
                self.finishedSignal.emit('Reading Polarion excel finished.')

        self.showLoadingBar()
        polarionExcel = self.polarionExcelEdit.text()
        self.loadPolarionWorkBook(polarionExcel)
        self.polarionDict.clear()
        self.polarionTableViewModel.clear()
        self.polarionTableView.model().clear()
        self.polarionReadExcelThreadObject = polarionReadExcelThread()
        self.polarionReadExcelThreadObject.polarionDict = self.polarionDict
        self.polarionReadExcelThreadObject.polarionWb = self.polarionWb
        self.polarionReadExcelThreadObject.polarionWs = self.polarionWs
        self.polarionReadExcelThreadObject.getLogDict = self.getLogDict
        self.polarionReadExcelThreadObject.updatePolarionRevisionSignal.connect(self.updatePolarionRevisionEdit)
        self.polarionReadExcelThreadObject.finishedSignal.connect(self.polarionReadExcelFinished)
        self.polarionReadExcelThreadObject.start()

    def updatePolarionRevisionEdit(self, txt):
        self.polarionRevisionLineEdit.setText(txt)

    def loadPolarionWorkBook(self, path):
        self.polarionWb = load_workbook(filename=path)
        self.polarionWs = self.polarionWb.active

    def polarionReadExcelFinished(self, msg):
        self.polarionLogAppend(msg)
        self.updatePolarionTableViewModel()

    def updatePolarionTableViewModel(self):
        """Update the model for polarion table view."""
        model = self.polarionTableViewModel
        header = ['TestCase', 'StartRow', 'EndRow', 'Polarion Steps', 'TestCase Verdict', 'Hyperlinks']

        for row, d in enumerate(self.polarionDict):
            testCaseItem = QStandardItem(d)
            testCaseItem.setCheckable(True)

            if self.polarionDict[d]['update']:
                testCaseItem.setCheckState(Qt.Checked)

            model.setItem(row, 0, testCaseItem)

            startRowItem = QStandardItem(str(self.polarionDict[d]['startRow']))
            model.setItem(row, 1, startRowItem)

            endRowItem = QStandardItem(str(self.polarionDict[d]['endRow']))
            model.setItem(row, 2, endRowItem)

            lengthItem = QStandardItem(str(self.polarionDict[d]['length']))
            model.setItem(row, 3, lengthItem)

            testCaseVerdict = self.polarionDict[d]['testCaseVerdict']
            testCaseVerdictItem = QStandardItem(testCaseVerdict)

            if testCaseVerdict == 'Passed':
                testCaseVerdictItem.setIcon(QIcon(':/icon/passedIcon'))
            elif testCaseVerdict == 'Deferred' or testCaseVerdict == 'Error':
                testCaseVerdictItem.setIcon(QIcon(':/icon/failedIcon'))

            model.setItem(row, 4, testCaseVerdictItem)

            hyperlinksItem = QStandardItem(self.polarionDict[d]['hyperlinks'])

            model.setItem(row, 5, hyperlinksItem)


            # for j, p in enumerate(list(self.polarionDict[d].keys())):
            #     item = QStandardItem(str(self.polarionDict[d][p]))
            #     # item.setCheckable(True)
            #     model.setItem(i, j + 1, item)

        model.setHorizontalHeaderLabels(header)
        self.polarionTableView.resizeColumnsToContents()
        self.polarionTableView.setColumnWidth(0, 150)

        self.polarionTableView.setSortingEnabled(True)
        self.polarionTableView.sortByColumn(0, Qt.AscendingOrder)
        self.polarionTableView.setAlternatingRowColors(True)

        allTestCaseVerdicts = [self.logDict[x]['testCaseVerdict'] for x in self.logDict]

        passedTotal = allTestCaseVerdicts.count('Passed')
        deferredTotal = allTestCaseVerdicts.count('Deferred')
        errorTotal = allTestCaseVerdicts.count('Error')
        total = passedTotal + deferredTotal + errorTotal

        self.polarionOverViewLineEdit.setText(
            'Total Logs Found: {}    Passed: {}    Deferred: {}    Error: {}'.format(total, passedTotal, deferredTotal,
                                                                                     errorTotal))
        self.hideLoadingBar()


    # update polarion dict with 'passed' only test cases
    def polarionUpdateExcel(self, testCaseVerdict='Passed'):
        for t in self.polarionDict:
            try:
                if testCaseVerdict == 'All':
                    verdictCriteria = True
                else:
                    verdictCriteria = self.logDict[t]['testCaseVerdict'] == testCaseVerdict

                if self.polarionDict[t]['length'] == self.logDict[t]['length']:
                    if verdictCriteria:
                        self.polarionDict[t]['testCaseVerdict'] = self.logDict[t]['testCaseVerdict']
                else:
                    self.polarionDict[t]['testCaseVerdict'] = 'Steps mismatch'
            except KeyError as error:
                print('{} not found'.format(str(error)))


        self.updatePolarionTableViewModel()

        self.polarionWs = self.polarionWb.active

        count = 0
        for t in self.polarionDict:
            try:
                if testCaseVerdict == 'All':
                    verdictCriteria = True
                else:
                    verdictCriteria = self.logDict[t]['testCaseVerdict'] == testCaseVerdict

                if self.polarionDict[t]['length'] == self.logDict[t]['length']:
                    if verdictCriteria:
                        # print(t, 'Match')
                        startRow = self.polarionDict[t]['startRow']
                        endRow = self.polarionDict[t]['endRow']

                        actualResultRowStart = 'M{}'.format(startRow)
                        actualResultRowEnd = 'M{}'.format(endRow)

                        actualResultRows = self.polarionWs[actualResultRowStart:actualResultRowEnd]

                        for row, actual in zip(actualResultRows, self.logDict[t]['actualResult']):
                            row[0].value = str(actual)

                        stepVerdictRowStart = 'N{}'.format(startRow)
                        stepVerdictRowEnd = 'N{}'.format(endRow)

                        stepVerdictRows = self.polarionWs[stepVerdictRowStart:stepVerdictRowEnd]
                        for row, verdict in zip(stepVerdictRows, self.logDict[t]['passList']):
                            row[0].value = verdict

                        testCaseVerdictCellIndex = 'O{}'.format(startRow)
                        self.polarionWs[testCaseVerdictCellIndex].value = self.logDict[t]['testCaseVerdict']

                        testCaseCommentIndex = 'P{}'.format(startRow)
                        self.polarionWs[testCaseCommentIndex].value = self.logDict[t]['testComment']

                        count += 1

            except KeyError as error:
                print('{} not found'.format(str(error)))

        self.polarionLogAppend('Updated excel file with {} verdicts.'.format(testCaseVerdict))

    # update revision number in polarion excel
    def udpatePolarionRevision(self):
        polarionWs = self.polarionWb['_polarion']
        polarionColA = [x.value for x in polarionWs['A']]
        revisionRow = polarionColA.index('testRunRevision') + 1
        polarionWs.cell(row=revisionRow, column=2).value = self.polarionRevisionLineEdit.text()

        self.polarionLogAppend('Updated Polarion revision number.')

    def updateHyperlinks(self):
        class updateHyperlinksThread(QThread):
            finishedSignal = pyqtSignal('PyQt_PyObject')
            def __init__(self):
                QThread.__init__(self)
                self.polarionDict = None

            class TransportSubclass(Transport):
                def __init__(self, *args, **kwargs):
                    super(self.__class__, self).__init__(*args, **kwargs)
                    self.last_response = None

                def post(self, *args, **kwargs):
                    self.last_response = super(self.__class__, self).post(*args, **kwargs)
                    return self.last_response

            def run(self):
                # login session and get session id
                session = Session()
                transport = self.TransportSubclass(session=session)
                loginClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/SessionWebService?wsdl'
                loginClient = Client(wsdl=loginClientWsdl, transport=transport)
                loginClient.service.logIn('vle', 'workhard2020')

                # grab repsonse header and parse for session id
                root = etree.XML(transport.last_response.content)
                sessions = root.xpath('//ns1:sessionID', namespaces={'ns1': 'http://ws.polarion.com/session'})
                session_id = sessions[0]

                # use the new session id for transports
                transport = Transport(session=session)

                # use session id for web service
                testWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TestManagementWebService?wsdl'
                testClient = Client(testWsdl, transport=transport)
                testClient._default_soapheaders = [session_id]

                # use session id for web service
                trackerClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TrackerWebService?wsdl'
                trackerClient = Client(trackerClientWsdl, transport=transport)
                trackerClient._default_soapheaders = [session_id]

                queryString = ' '.join(self.polarionDict.keys())

                # query = trackerClient.service.queryWorkItems(
                #     query='testtype.KEY:manual AND status:(reviewed review) AND ecu.KEY:VCMB', sort='hyperlinks',
                #     fields=['id', 'hyperlinks'])

                query = trackerClient.service.queryWorkItems(
                    query=queryString, sort='hyperlinks',
                    fields=['id', 'hyperlinks'])

                hyperDict = {}

                for q in query:
                    hyperDict[q.id] = {'hyperlinks': q.hyperlinks}

                loginClient.service.endSession()
                self.finishedSignal.emit(hyperDict)

        self.showLoadingBar()
        self.updateHyperlinksThreadObject = updateHyperlinksThread()
        self.updateHyperlinksThreadObject.polarionDict = self.polarionDict
        self.updateHyperlinksThreadObject.finishedSignal.connect(self.updatePolarionDictWithHyperlinks)
        self.updateHyperlinksThreadObject.start()

    def updatePolarionSteps(self):
        class updatePolarionStepsThread(QThread):
            finishedSignal = pyqtSignal('PyQt_PyObject')
            logSignal = pyqtSignal('PyQt_PyObject')

            def __init__(self):
                QThread.__init__(self)
                self.polarionDict = None

            class TransportSubclass(Transport):
                def __init__(self, *args, **kwargs):
                    super(self.__class__, self).__init__(*args, **kwargs)
                    self.last_response = None

                def post(self, *args, **kwargs):
                    self.last_response = super(self.__class__, self).post(*args, **kwargs)
                    return self.last_response

            def run(self):
                teExcel, fileType = QFileDialog.getOpenFileName(
                    self.parent(),
                    "Open Polarion TE File",
                    '',
                    "XLSX Files (*.xlsx);;All Files (*)"
                )

                if len(teExcel) > 0:
                    self.logSignal.emit('Updating Polarion with new steps.')
                    # teExcel = r"C:\Users\pthil\Desktop\Test_Runs\K1_20_TestRun\BL_1000\BL_1000_Beta\SCM_Manual_V13\K1-20-1000_SCM_Manual_V13_KA_TE.xlsx"
                    wb = load_workbook(teExcel)
                    ws = wb.active

                    # login session and get session id
                    session = Session()
                    transport = self.TransportSubclass(session=session)
                    loginClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/SessionWebService?wsdl'
                    loginClient = Client(wsdl=loginClientWsdl, transport=transport)
                    loginClient.service.logIn('vle', 'workhard2020')

                    # grab repsonse header and parse for session id
                    root = etree.XML(transport.last_response.content)
                    sessions = root.xpath('//ns1:sessionID', namespaces={'ns1': 'http://ws.polarion.com/session'})
                    session_id = sessions[0]

                    # use the new session id for transports
                    transport = Transport(session=session)

                    # use session id for web service
                    testWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TestManagementWebService?wsdl'
                    testClient = Client(testWsdl, transport=transport)
                    testClient._default_soapheaders = [session_id]

                    # use session id for web service
                    trackerClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TrackerWebService?wsdl'
                    trackerClient = Client(trackerClientWsdl, transport=transport)
                    trackerClient._default_soapheaders = [session_id]

                    testCaseIdCol = ws['A']
                    stepNumberCol = ws['H']

                    allSteps = [str(x.value) for x in stepNumberCol]

                    polarionDict = OrderedDict()
                    startMarker = '1'
                    endMarker = 'None'

                    querySteps = None

                    # grab data from polarion excel
                    for eachRow in testCaseIdCol:
                        if re.match('\w+-\w+', str(eachRow.value)) is not None:
                            testCase = str(eachRow.value)
                            start = allSteps.index(startMarker, eachRow.row - 1) + 1

                            try:
                                end = allSteps.index(endMarker, start + 1)
                            except ValueError:
                                end = len(allSteps)

                            startRange = 'I{}'.format(start)
                            endRange = 'P{}'.format(end)

                            # print(startRange,endRange)

                            # convert excel cells into string values
                            # print(ws[startRange:endRange] != None)

                            allRows = ws[startRange:endRange]
                            querySteps = [list(col.value for col in row) for row in allRows]

                            title = ws['D{}'.format(start)].value
                            desc = ws['E{}'.format(start)].value
                            polarionDict[testCase] = {'startRow': start, 'endRow': end, 'length': end - start + 1,
                                                      'title': title, 'desc': desc, 'steps': querySteps}

                    # column indexes
                    columnIndexes = {
                        'Phase': 0,
                        'Action': 1,
                        'Description': 2,
                        'Variable': 3,
                        'Setting': 4,
                        'ExpectedResult': 5,
                        'Wait': 6,
                        'Remark': 7
                    }

                    # testStepCopy = None

                    for id in polarionDict:
                        # id = 'K1V2SCM-12261'
                        if self.polarionDict[id]['update']:
                        # if polarionDict[id]['update']:
                            # get workitem from polarion using the testcase id
                            query = trackerClient.service.queryWorkItems(query=id, sort='id', fields=['id'])

                            # do update if a query returns
                            if len(query) > 0:
                                testCaseUri = query[0]['uri']

                                # double check that id and test case uri matches
                                if id in testCaseUri:
                                    # grab steps from query
                                    # if testStepCopy is None:
                                    querySteps = testClient.service.getTestSteps(testCaseUri)['steps']['TestStep']

                                    updatedQuerySteps = []

                                    if len(querySteps) > 0:
                                        # fill updated query steps, use the first step as a copy
                                        while len(updatedQuerySteps) < polarionDict[id]['length']:
                                            testStepCopy = copy.deepcopy(querySteps[0])
                                            updatedQuerySteps.append(testStepCopy)

                                        for i in range(0, polarionDict[id]['length']):
                                            for idx in columnIndexes.values():
                                                updatedQuerySteps[i]['values']['Text'][idx]['content'] = \
                                                polarionDict[id]['steps'][i][idx]

                                        # service to update test steps for specific testcase
                                        testClient.service.setTestSteps(testCaseUri, updatedQuerySteps)

                                        # print('Updated {}. Number of Steps: {} -> {}.'.format(id, len(querySteps),
                                        #                                                       len(updatedQuerySteps)))
                                        self.logSignal.emit('Updated {}. Steps: {} -> {}.'.format(id, len(querySteps), len(updatedQuerySteps)))
                                        # time.sleep(2.0)
                            else:
                                self.logSignal.emit('{} was not found'.format(id))
                                # print(id, 'not found.')

                    # close session
                    loginClient.service.endSession()
                    self.finishedSignal.emit('Updating Polarion finished.')
                    self.logSignal.emit('Updating Polarion finished.')
                else:
                    self.logSignal.emit('Update Polarion cancelled.')


        self.showLoadingBar()
        self.udpatePolarionStepsThreadObject = updatePolarionStepsThread()
        self.udpatePolarionStepsThreadObject.polarionDict = self.polarionDict
        self.udpatePolarionStepsThreadObject.logSignal.connect(self.polarionLogAppend)
        self.udpatePolarionStepsThreadObject.finishedSignal.connect(self.updatePolarionDictWithQuerySteps)
        self.udpatePolarionStepsThreadObject.start()

    def polarionLogAppend(self, msg):
        self.polarionLogEdit.appendPlainText('{} - {}'.format(datetime.now().__str__(), msg))

    def updatePolarionDictWithQuerySteps(self, msg):
        self.hideLoadingBar()

    def updatePolarionDictWithHyperlinks(self, hyperDict):
        for t in self.polarionDict:
            try:
                links = ','.join([x['uri'] for x in hyperDict[t]['hyperlinks']['Hyperlink']])
                self.polarionDict[t]['hyperlinks'] = links
            except KeyError:
                # print('{} was not found in hyperlink dict'.format(str(error)))
                pass
            except TypeError:
                pass

        self.polarionLogAppend('Updated Polarion table with hyperlinks.')
        self.updatePolarionTableViewModel()

    def polarionSaveExcel(self):
        folder = os.path.dirname(self.polarionExcelEdit.text())
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Save Polarion Excel File",
            folder,
            'XLSX Files (*.xlsx);;All Files (*)'
        )
        if len(filePath) > 0:
            self.showLoadingBar()
            try:
                self.polarionWb.save(filePath)
                self.polarionLogAppend('Save successful.')
            except IOError as error:
                if str(error).__contains__('Permission denied'):
                    self.polarionLogAppend('Permission Denied. Unable to save excel file.')
            self.hideLoadingBar()

    # use the profile dictionary to update the gui
    def updateGuiFromProfileDict(self):
        try:
            polarionExcelPath = self.profileDict['Profile']['PolarionExcel']
            self.polarionExcelEdit.setText(polarionExcelPath)
        except KeyError:
            self.polarionExcelEdit.setText('')

        try:
            testcasepath = self.profileDict['Profile']['TestCaseExcel']
            self.testCaseExcelEdit.setText(testcasepath)
        except KeyError:
            self.testCaseExcelEdit.setText('')

        try:
            callFunctionFolder = self.profileDict['Profile']['CallFunctionFolder']
            if callFunctionFolder:
                self.callFunctionEdit.setText(callFunctionFolder)
                self.checkFolderExist(callFunctionFolder)
        except KeyError:
            self.callFunctionEdit.setText('')

        try:
            csvPath = self.profileDict['Profile']['CSVReportFolder']
            if csvPath:
                self.csvReportEdit.setText(csvPath)
                self.checkFolderExist(csvPath)
        except KeyError:
            self.csvReportEdit.setText('')

        try:
            varPoolPath = self.profileDict['Profile']['VariablePoolPath']
            self.variablePoolEdit.setText(varPoolPath)
            self.checkVarPoolExist(varPoolPath)
        except KeyError:
            self.variablePoolEdit.setText('')

        try:
            dtcExceptionEnableString = self.profileDict['Profile']['DTC']['@enable']
            dtcExceptionEnable = eval(dtcExceptionEnableString)
            self.dtcExCheckBox.setChecked(dtcExceptionEnable)
            self.showDtcException(dtcExceptionEnable)
        except KeyError:
            self.dtcExCheckBox.setChecked(False)
            self.showDtcException(False)

        try:
            callFunctionDebug = self.profileDict['Profile']['CallFunctionDebug']['@enable']
            self.callFunctionDebugCheckbox.setChecked(eval(callFunctionDebug))
        except KeyError:
            self.callFunctionDebugCheckBox.setChecked(False)

        try:
            versionCheckbox = self.profileDict['Profile']['Version']['@include']
            self.versionCheckBox.setChecked(eval(versionCheckbox))
        except KeyError:
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
        except KeyError:
            debugPrint('Signal list is empty')

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
        except KeyError:
            debugPrint('DTCs exception list is empty')

    def loadConfig(self):
        if os.path.exists(str(self.configFile)):
            with open(str(self.configFile), 'rb') as f:
                configValid = True

                try:
                    self.configDict = xmltodict.parse(f.read())
                    configValid &= True
                except:
                    debugPrint('Unable to parse XML config file')

                try:
                    configversion = self.configDict['Config']['@version']
                    if configversion == '1.0':
                        configValid &= True
                except:
                    debugPrint('Version was not found in config file.')

                try:
                    width = self.configDict['Config']['Width']
                    height = self.configDict['Config']['Height']
                    self.resize(int(width), int(height))
                except:
                    debugPrint('Window width or height is missing in config.')

                try:
                    profilepath = self.configDict['Config']['LastProfile']
                    self.profileFile = Path(profilepath)
                    if os.path.exists(profilepath):
                        self.loadProfile()
                except:
                    self.statusbar.showMessage(strings.CONFIG_PROFILE_NOTFOUND)
                    debugPrint('Last profile not found in config.')

                try:
                    autorun = self.configDict['Config']['Autorun']
                    self.autorunCheckBox.setChecked(eval(autorun))
                except:
                    debugPrint('Autorun setting not found in config.')

                try:
                    autoruntimer = self.configDict['Config']['AutorunTimer']
                    self.autorunSpinBox.setValue(eval(autoruntimer))
                except:
                    debugPrint('Autorun time not found in config.')

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
        self.setWindowTitle('[' + str(profilePath) + '] - AutomationDesk GUI ' + version)

    # def setProfileDict(
    #         self,
    #         testcaseexcel='',
    #         callfolder='',
    #         csvfolder='',
    #         varpoolpath='',
    #         includeversion='False',
    #         callfuncdebug='False',
    #         logmode='0',
    #         signallist=[],
    #         dtcenable='False',
    #         dtcexlist=[],
    #         updatevp='False'
    # ):
    #
    #     self.profileDict = {
    #         'Profile': {
    #             '@version': '1.0',
    #             'TestCaseExcel': testcaseexcel,
    #             'CallFunctionFolder': callfolder,
    #             'CSVReportFolder': csvfolder,
    #             'VariablePoolPath': varpoolpath,
    #             'UpdateVariablePool': updatevp,
    #             'Version': {'@include': includeversion},
    #             'CallFunctionDebug': {'@enable': callfuncdebug},
    #             'Log': {
    #                 '@mode': logmode,
    #                 'Signal': signallist
    #             },
    #             'DTC': {
    #                 '@enable': dtcenable,
    #                 'Except': dtcexlist
    #             }
    #         }
    #     }

    def setDefaultProfile(self):
        self.defaultProfile = True
        # load default profile if no params are given
        # self.setProfileDict()

        self.profileDict = {
            'Profile': {
                '@version': '1.0',
            }
        }

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
                debugPrint('File saved')

        self.saveConfig()
        self.updateProfileDictFromGui()
        self.close()

    def about(self):
        about = QMessageBox()
        about.setWindowIcon(QIcon(':/logo/graphics/karmalogo_48dp.png'))
        about.setWindowTitle('About')
        about.setText(version + '\n'
                      'Developer: Vu Le\n'
                      'The developer reserves all rights to this software.\n'
                      'Do not distribute this software without permission.')
        about.setInformativeText('Copyright (C) 2018')
        pixmap = QPixmap(':/icon/karmaIcon')
        pixmap = pixmap.scaledToWidth(128)
        about.setIconPixmap(pixmap)
        about.exec_()

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

    return form.profileDict, form.variablePoolDict  # return data to AutomationDesk


if __name__ == '__main__':
    main()
