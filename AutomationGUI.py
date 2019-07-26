# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 7/23/19 Changelog
# Added dark theme
# Fixed total wait time bug
# Added AD blocks conversion
# Improved sw/hw ecu versions support

# 7/11/19 Changelog
# Title and descriptions are shown when test case is clicked
# Fixed bug with saving pickles
# Migrated to Python 3.6

# 7/3/19 Changelog
# Added Polarion authentication check
# Added run test context menu actions
# Profile is now saved as JSON instead of XML

# 6/28/19 Changelog
# Added additional run test context menu actions
# Fixed wait time sorting

# 6/11/19 Changelog
# Parsed Polarion data are now saved on local directory
# Added view for csv log files
# Changed styling to Fusion
# Saving is now threaded
# Reading excel now uses xlrd for speed
# Added wait times column

# 5/28/19 Changelog
# Added loading bar
# Improved signal/slots in threading operations
# Config settings are now saved in registry
# DTC exception hex input are now validated

# 5/13/19 Changelog
# Added toolbar for polarion and dspace tabs
# Improved thread handling between gui and reading excel files
# Added polarion view

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
#import xmltodict
from pathlib import Path
from AutomationGUI_ui import *
import os
import sys
#import strings
import csv
import re
import json
import pickle
import xlrd
from datetime import datetime
from openpyxl import load_workbook
from collections import OrderedDict

import webbrowser
# from functools import partial # used for calling with args

# polarion related libs
import zeep
import requests
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
    def __init__(self, aud=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # create a frameless window without titlebar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # platform independent settings

        # set default xml config file path
        self.configFile = 'C:/DS_Config/config.xml'
        # self.profileFile = 'C:/DS_Config/profile1.xml'

        self.configDict = {}
        self.profileDict = {}
        self.runList = []
        # dict to hold data from all log files
        self.logDict = OrderedDict()
        # dict to hold data from polarion sheet
        self.runDict = OrderedDict()
        self.polarionDict = OrderedDict()
        self.polarionWs = None
        self.polarionWb = None
        self.polarionUsername = ''
        self.polarionPassword = ''
        self.variablePoolDict = {}
        self.updateVariablePool = False  # update variable pool in AutomationDesk
        self.defaultProfile = True  # false when a profile is loaded

        # threads
        self.polarionReadExcelThread = None

        # progress bar
        self.progressBarTimer = QTimer()
        self.progressBarTimer.timeout.connect(self.progressBarAnimation)

        # Qt item models
        self.versionTableModel = QStandardItemModel()
        self.versionTableView.setModel(self.versionTableModel)
        self.versionTableModel.itemChanged.connect(self.versionTableViewItemChanged)

        self.addSignalModel = QStandardItemModel()
        self.addSignalListView.setModel(self.addSignalModel)


        self.dtcTableModel = QStandardItemModel()
        self.dtcTableView.setModel(self.dtcTableModel)
        self.dtcTableModel.itemChanged.connect(self.dtcTableModelItemChanged)

        self.loadSettings()
        self.changesSaved = True

        # general tab
        self.browsePolarionExcelBtn.clicked.connect(self.browsePolarionExcel)
        self.browseTestCaseExcelBtn.clicked.connect(self.browseTestCaseExcel)
        self.browseCallFunctionBtn.clicked.connect(self.browseCallFunction)
        self.browseCsvReportBtn.clicked.connect(self.browseCsvReport)
        self.browseVariablePoolBtn.clicked.connect(self.browseVariablePool)
        self.testCaseExcelEdit.textChanged.connect(self.useTestCaseFolderForLogs)

        # connections for changes
        self.polarionExcelEdit.textChanged.connect(self.unsavedChanges)
        self.testCaseExcelEdit.textChanged.connect(self.unsavedChanges)
        self.callFunctionEdit.textChanged.connect(self.unsavedChanges)
        self.csvReportEdit.textChanged.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)
        self.variablePoolEdit.textChanged.connect(self.unsavedChanges)
        self.dtcExCheckBox.clicked.connect(self.unsavedChanges)
        self.callFunctionDebugCheckbox.clicked.connect(self.unsavedChanges)
        self.versionCheckBox.clicked.connect(self.unsavedChanges)

        self.logRadioBtn0.clicked.connect(self.unsavedChanges)
        self.logRadioBtn1.clicked.connect(self.unsavedChanges)
        self.logRadioBtn2.clicked.connect(self.unsavedChanges)

        self.versionAddButton.clicked.connect(self.versionAddRow)
        self.versionRemoveButton.clicked.connect(self.versionRemoveRow)

        # polarion excel toolbutton
        self.polarionExcelMenu = QMenu()

        openPolarionExcelFileAction = QAction(QIcon(':/icon/excel'), 'Open Test Case File', self)
        openPolarionExcelFileAction.triggered.connect(self.openPolarionExcelFile)
        self.polarionExcelMenu.addAction(openPolarionExcelFileAction)


        openPolarionExcelFolderAction = QAction(QIcon(':/icon/folderOpen'), 'Open Test Case Folder', self)
        openPolarionExcelFolderAction.triggered.connect(self.openPolarionExcelFolder)
        self.polarionExcelMenu.addAction(openPolarionExcelFolderAction)

        self.polarionExcelToolButton.setMenu(self.polarionExcelMenu)

        # test case excel toolbutton
        testCaseExcelMenu = QMenu()

        openTestCaseExcelFileAction = QAction(QIcon(':/icon/excel'), 'Open Test Case File', self)
        openTestCaseExcelFileAction.triggered.connect(self.openTestCaseExcelFile)
        testCaseExcelMenu.addAction(openTestCaseExcelFileAction)

        openTestCaseExcelFolderAction = QAction(QIcon(':/icon/folderOpen'), 'Open Test Case Folder', self)
        openTestCaseExcelFolderAction.triggered.connect(self.openTestCaseExcelFolder)
        testCaseExcelMenu.addAction(openTestCaseExcelFolderAction)

        self.testCaseExcelToolButton.setMenu(testCaseExcelMenu)

        # csv report toolbutton
        csvReportFolderMenu = QMenu()

        openCsvReportFolderAction = QAction(QIcon(':/icon/folderOpen'), 'Open Report Folder', self)
        openCsvReportFolderAction.triggered.connect(self.openCsvReportFolder)
        csvReportFolderMenu.addAction(openCsvReportFolderAction)

        useTestCasePathAction = QAction(QIcon(':/icon/folderOpen'), 'Use {TestCaseFolder}\\Logs', self)
        useTestCasePathAction.triggered.connect(self.useTestCasePath)
        csvReportFolderMenu.addAction(useTestCasePathAction)

        self.csvReportFolderToolButton.setMenu(csvReportFolderMenu)

        # call function toolbutton
        callFunctionFolderMenu = QMenu()

        openCallFunctionFolderAction = QAction(QIcon(':/icon/folderOpen'), 'Open Call Function Folder', self)
        openCallFunctionFolderAction.triggered.connect(self.openCallFunctionFolder)
        callFunctionFolderMenu.addAction(openCallFunctionFolderAction)

        self.callFunctionFolderToolButton.setMenu(callFunctionFolderMenu)

        # variable pool toolbutton
        variablePoolMenu = QMenu()

        reloadVariablePoolFileAction = QAction(QIcon(':/icon/refresh'), 'Reload Variable Pool', self)
        reloadVariablePoolFileAction.triggered.connect(self.loadVariablePool)
        variablePoolMenu.addAction(reloadVariablePoolFileAction)

        openVariablePoolFileAction = QAction(QIcon(':/icon/copy'), 'Open Variable Pool File', self)
        openVariablePoolFileAction.triggered.connect(self.openVarPoolFile)
        variablePoolMenu.addAction(openVariablePoolFileAction)

        openVariablePoolFolderAction = QAction(QIcon(':/icon/folderOpen'), 'Open Variable Pool Folder', self)
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

        # dtc tab

        self.updateDtcTableView()
        self.addDtcExBtn.clicked.connect(self.addDtcEx2)

        self.addDtcExEdit.setInputMask('>NN NN NN NN;_')
        self.addDtcExEdit.setMaxLength(11)
        self.addDtcExEdit.returnPressed.connect(self.addDtcEx2)
        self.removeDtcExBtn.clicked.connect(self.removeDtcEx2)

        # # run list tab
        # self.dSpaceReadExcelButton.clicked.connect(self.dSpaceReadExcel)
        # self.runTableViewModel = QStandardItemModel()
        # self.runTableView.setModel(self.runTableViewModel)
        #
        # self.copyButton.clicked.connect(self.copyRunList)
        # self.runTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.runTableView.customContextMenuRequested.connect(self.runTableContextMenuEvent)

        # polarion tab
        self.polarionReadExcelButton.clicked.connect(self.readPolarionExcel)
        self.polarionTableViewModel = QStandardItemModel()
        self.polarionTableView.setModel(self.polarionTableViewModel)
        self.polarionTableView.clicked.connect(self.polarionTableViewClicked)


        self.polarionUpdatePassedButton.clicked.connect(lambda: self.updatePolarionVerdicts('Passed'))
        self.polarionUpdateAllButton.clicked.connect(lambda: self.updatePolarionVerdicts('All'))
        self.polarionSaveExcelButton.clicked.connect(self.savePolarionExcel)
        self.polarionUpdateRevisionButton.clicked.connect(self.udpatePolarionRevision)
        self.updateHyperlinksButton.clicked.connect(self.updateHyperlinks)
        self.updateStepsButton.clicked.connect(self.updatePolarionSteps)
        self.polarionCopyRunListButton.clicked.connect(self.polarionCopyRunList)


        # self.polarionTableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.polarionTableView.customContextMenuRequested.connect(self.polarionTableContextMenuEvent)

        self.loadPolarionJson()
        self.loadLogResults()

        # settings tab
        self.updateVariablePoolCheckBox.clicked.connect(self.toggleUpdateVariablePool)

        # TBX 2 Text tab
        self.tbxBrowseButton.clicked.connect(self.browseTbxFile)
        self.tbxConvertButton.clicked.connect(self.tbx2text)
        self.tbxCopyTitleButton.clicked.connect(lambda: self.tbxCopy(self.tbxTitleLineEdit))
        self.tbxCopyDescButton.clicked.connect(lambda: self.tbxCopy(self.tbxDescLineEdit))
        self.tbxCopyTextButton.clicked.connect(lambda: self.tbxCopy(self.tbxPlainTextEdit))

        # file menu
        self.actionLoad.triggered.connect(self.browseProfile)
        self.actionNew.triggered.connect(self.newProfile)
        self.actionSave.triggered.connect(self.saveProfile)
        self.actionSaveAs.triggered.connect(self.saveAsProfile)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
        self.actionConfigFolder.triggered.connect(self.openConfigFolder)

        # gui layout related
        # dropShadow = QGraphicsDropShadowEffect()
        # dropShadow.setXOffset(1)
        # dropShadow.setYOffset(1)
        # dropShadow.setBlurRadius(6)
        # self.tabWidget.setGraphicsEffect(dropShadow)

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
        self.progressBar.setValue(0 if value > 99 else value + 20)

    def showLoadingBar(self):
        self.progressBarTimer.start(1000)

    def hideLoadingBar(self):
        self.progressBarTimer.stop()
        self.progressBar.setValue(0)

    def savePolarionJson(self):
        # save results to a file
        if len(self.polarionExcelEdit.text()) > 0:
            polarionJsonPath = '{}.json'.format(self.polarionExcelEdit.text()[:-5])

            with open(polarionJsonPath, 'w') as f:
                polarionJson = json.dumps(self.polarionDict)
                f.write(polarionJson)

    def loadPolarionJson(self):
        polarionJsonPath = '{}.json'.format(self.polarionExcelEdit.text()[:-5])
        if os.path.exists(polarionJsonPath):
            with open(polarionJsonPath) as f:
                self.polarionDict = json.load(f)
                self.updatePolarionTableModel()

    def saveLogResults(self):
        # save log file results to a pickle file
        csvReportFolder = self.csvReportEdit.text()
        logPicklePath = os.path.join(csvReportFolder, 'LogResults.pkl')
        with open(logPicklePath, 'wb') as f:
            pickle.dump(self.logDict, f)

    def loadLogResults(self):
        logPicklePath = os.path.join(self.csvReportEdit.text(), 'LogResults.pkl')
        try:
            with open(logPicklePath, 'rb') as f:
                self.logDict = pickle.load(f)
        except:
            print('Exception for def loadLogResults')

    def polarionTableContextMenuEvent(self, qpoint):
        menu = QMenu(self)

        testCaseCol = self.polarionTableHeader.index('TestCase')
        runtestCol = self.polarionTableHeader.index('Run Test')
        totalWaitTimeCol = self.polarionTableHeader.index('Total Wait Time')
        hyperlinksCol = self.polarionTableHeader.index('Hyperlinks')

        modelIndex = self.polarionTableView.indexAt(qpoint)
        selectedColumn = modelIndex.column()
        item = self.polarionTableViewModel.itemFromIndex(modelIndex)

        if selectedColumn == testCaseCol:
            copyAction = QAction(QIcon(':/icon/copy'), 'Copy TestCase ID', self)
            copyAction.triggered.connect(self.copySelectionPolarionTable)
            menu.addAction(copyAction)
            menu.addSeparator()

        # if selectedColumn == runtestCol:
        #     runPassedAction = QAction(QIcon(':/icon/passed'), 'Run Passed testcases', self)
        #     runPassedAction.triggered.connect(lambda: self.runTestCasesWithVerdict('Passed'))
        #     menu.addAction(runPassedAction)
        #
        #     runDeferredAction = QAction(QIcon(':/icon/failed'), 'Run Deferred testcases', self)
        #     runDeferredAction.triggered.connect(lambda: self.runTestCasesWithVerdict('Deferred'))
        #     menu.addAction(runDeferredAction)
        #
        #     runWithoutLogsAction = QAction(QIcon(':/icon/notInterested'), 'Run testcases without logs', self)
        #     runWithoutLogsAction.triggered.connect(lambda: self.runTestCasesWithVerdict('No log found'))
        #     menu.addAction(runWithoutLogsAction)
        #
        #     runTotalWaitTimeAction = QAction(QIcon(':/icon/clock'), 'Run testcases with TotalWaitTime =< 400s', self)
        #     runTotalWaitTimeAction.triggered.connect(lambda: self.runTotalWaitTimeTestCases('=<', 400))
        #     menu.addAction(runTotalWaitTimeAction)
        #
        #     runTotalWaitTimeAction = QAction(QIcon(':/icon/clock'), 'Run testcases with TotalWaitTime > 400s',
        #                                      self)
        #     runTotalWaitTimeAction.triggered.connect(lambda: self.runTotalWaitTimeTestCases('>', 400))
        #     menu.addAction(runTotalWaitTimeAction)
        #
        #     runTestCasesWithHyperlinksAction = QAction(QIcon(':/icon/link'), 'Run Deferred with Hyperlinks', self)
        #     runTestCasesWithHyperlinksAction.triggered.connect(lambda: self.runTestCasesWithVerdictHyperlinks(verdict='Deferred', hasHyperlinks=True))
        #     menu.addAction(runTestCasesWithHyperlinksAction)
        #
        #
        #     runTestCasesWithNoHyperlinksAction = QAction(QIcon(':/icon/noLink'), 'Run Deferred with no Hyperlinks', self)
        #     runTestCasesWithNoHyperlinksAction.triggered.connect(
        #         lambda: self.runTestCasesWithVerdictHyperlinks(verdict='Deferred', hasHyperlinks=False))
        #     menu.addAction(runTestCasesWithNoHyperlinksAction)
        #
        #
        #     menu.addSeparator()

        if selectedColumn == hyperlinksCol:
            hyperlink = item.text()
            if len(hyperlink) > 0:
                openLinkAction = QAction(QIcon(':/icon/link'), 'Open Hyperlink', self)
                openLinkAction.triggered.connect(lambda: self.openHyperlink(hyperlink))
                menu.addAction(openLinkAction)
                menu.addSeparator()

        openLogFileAction = QAction(QIcon(':/icon/openNew'), 'Open Log File', self)
        openLogFileAction.triggered.connect(self.openLogFile)
        menu.addAction(openLogFileAction)

        checkAllAction = QAction(QIcon(':icon/checked'), 'Check All', self)
        checkAllAction.triggered.connect(self.checkAllPolarionTable)
        menu.addAction(checkAllAction)

        decheckAllAction = QAction(QIcon(':icon/notChecked'), 'Check None', self)
        decheckAllAction.triggered.connect(self.decheckAllPolarionTable)
        menu.addAction(decheckAllAction)

        menu.addSeparator()

        runSelectedTestCasesAction = QAction(QIcon(':/icon/selectAll'), 'Run selected test cases', self)
        runSelectedTestCasesAction.triggered.connect(lambda: self.runSelectedTestCases(True))
        menu.addAction(runSelectedTestCasesAction)

        dontRunSelectedTestCasesAction = QAction(QIcon(':/icon/gridOff'), 'Do not run selected test cases', self)
        dontRunSelectedTestCasesAction.triggered.connect(lambda: self.runSelectedTestCases(False))
        menu.addAction(dontRunSelectedTestCasesAction)

        runAllTestCasesAction = QAction(QIcon(':/icon/selectAll'), 'Run ALL test cases', self)
        runAllTestCasesAction.triggered.connect(lambda: self.runAllTestCases(all=True))
        menu.addAction(runAllTestCasesAction)

        dontRunAllTestCasesAction = QAction(QIcon(':/icon/gridOff'), 'Do NOT run ALL test cases', self)
        dontRunAllTestCasesAction.triggered.connect(lambda: self.runAllTestCases(all=False))
        menu.addAction(dontRunAllTestCasesAction)

        if menu.actions().__len__() > 0:
            menu.popup(QCursor.pos())

    def checkAllPolarionTable(self):
        model = self.polarionTableViewModel
        rowCount = model.rowCount()

        for i in range(0, rowCount):
            item = model.item(i, 0)
            item.setCheckState(Qt.Checked)

    def decheckAllPolarionTable(self):
        model = self.polarionTableViewModel
        rowCount = model.rowCount()

        for i in range(0, rowCount):
            item = model.item(i, 0)
            item.setCheckState(Qt.Unchecked)

    def runSelectedTestCases(self, run):
        model = self.polarionTableViewModel
        view = self.polarionTableView

        if self.polarionTableView.model():
            selectionModel = self.polarionTableView.selectionModel()

            runTestCol = self.polarionTableHeader.index('Run Test')

            for each in view.selectedIndexes():
                runTestItem = model.item(each.row(), runTestCol)
                runTestItem.setText('Yes' if run else 'No')
                # runTestItem.setIcon(QIcon(':/icon/checkBoxChecked') if run else QIcon(':/icon/checkBoxBlank'))
                runTestItem.setCheckState(Qt.Checked if run else Qt.Unchecked)

    def runAllTestCases(self, all):
        model = self.polarionTableViewModel
        runTestCol = self.polarionTableHeader.index('Run Test')

        for row in range(0, model.rowCount()):
            runTestItem = model.item(row, runTestCol)
            runTestItem.setText('Yes' if all else 'No')
            # runTestItem.setIcon(QIcon(':/icon/checkBoxChecked') if all else QIcon(':/icon/checkBoxBlank'))
            runTestItem.setCheckState(Qt.Checked if all else Qt.Unchecked)

    def makeRunList(self):
        testCaseCol = self.polarionTableHeader.index('TestCase')
        runTestCol = self.polarionTableHeader.index('Run Test')
        model = self.polarionTableViewModel
        rowCount = model.rowCount()

        self.runList = []
        runList = self.runList

        for i in range(0, rowCount):
            testCaseItem = model.item(i, testCaseCol)
            runTestItem = model.item(i, runTestCol)
            testCase = testCaseItem.text()
            runTest = runTestItem.text()
            runList.append([testCase, runTest])

            try:
                self.polarionDict[testCase]['run'] = runTest
            except KeyError:
                pass

    def polarionTableViewClicked(self, qmodelindex):
        # QModelIndex
        row = qmodelindex.row()
        column = qmodelindex.column()

        testCaseCol = self.polarionTableHeader.index('TestCase')
        testCaseId = self.polarionTableViewModel.item(row, testCaseCol).text()
        runTestCol = self.polarionTableHeader.index('Run Test')

        try:
            csvFilePath = self.logDict[testCaseId]['filePath']
            if os.path.exists(csvFilePath):
                self.updateLogTableWidget(csvFilePath)
        except KeyError:
            print('KeyError for def polarionTableViewClicked, csvFilePath')

        try:
            title = self.polarionDict[testCaseId]['title']
            description = self.polarionDict[testCaseId]['desc']
            self.titleEdit.setText(title)
            self.descriptionEdit.setText(description)
        except KeyError:
            print('KeyError for def polarionTableViewClicked, title')

        # if column == runTestCol:
        #     runTestItem = self.polarionTableViewModel.item(row, column)
        #     runTestItem.setText('Yes' if runTestItem.checkState() else 'No')

        # if column == testCaseCol:
        #     item = self.polarionTableViewModel.item(row, column)
        #     testCaseId = item.text()
        #     checked = item.checkState() == 2
        #     # print(row, column, testCaseId, checked)
        #     self.polarionDict[testCaseId]['update'] = checked

    def polarionTableViewModelItemChanged(self, item):
        column = item.column()
        runTestCol = self.polarionTableHeader.index('Run Test')

        if column == runTestCol:
            # print('Changed')
            item.setText('Yes' if item.checkState() else 'No')

    def updateLogTableWidget(self, csvFilePath):
        self.logTableHeader = ['Action', 'Description', 'Variable', 'Settings', 'Value', 'Wait', 'Actual Value', 'Step Verdict', 'Step Message']

        # stepCol = self.logTableHeader.index('Step')
        actionCol = self.logTableHeader.index('Action')
        descriptionCol = self.logTableHeader.index('Description')
        variableCol = self.logTableHeader.index('Variable')
        settingsCol = self.logTableHeader.index('Settings')
        valueCol = self.logTableHeader.index('Value')
        waitCol = self.logTableHeader.index('Wait')
        actualCol = self.logTableHeader.index('Actual Value')
        verdictCol = self.logTableHeader.index('Step Verdict')
        statusCol = self.logTableHeader.index('Step Message')

        self.logTableWidget.clear()

        with open(csvFilePath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            allRows = [row for row in csvReader]

            self.logTableWidget.setRowCount(allRows.__len__())
            self.logTableWidget.setColumnCount(self.logTableHeader.__len__())

            rowIndex = 0

            for row in allRows:
                try:
                    self.logTableWidget.setItem(rowIndex, actionCol, QTableWidgetItem(row['Action']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, descriptionCol, QTableWidgetItem(row['Description']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, variableCol, QTableWidgetItem(row['Variable']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, settingsCol, QTableWidgetItem(row['Settings']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, valueCol, QTableWidgetItem(row['Value']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, waitCol, QTableWidgetItem(row['Wait']))
                except KeyError:
                    pass

                try:
                    self.logTableWidget.setItem(rowIndex, actualCol, QTableWidgetItem(row['Actual Value']))
                except KeyError:
                    pass

                try:
                    verdict = row['Step Verdict']
                    verdictItem = QTableWidgetItem(verdict)
                    if verdict == 'Passed':
                        verdictItem.setIcon(QIcon(':/icon/passed'))
                    elif verdict == 'Deferred' or verdict == 'Error' or verdict == 'Not Passed':
                        verdictItem.setIcon(QIcon(':/icon/failed'))

                    self.logTableWidget.setItem(rowIndex, verdictCol, verdictItem)

                except KeyError:
                    print('KeyError for updateLogTableWidget, verdict')

                try:
                    self.logTableWidget.setItem(rowIndex, statusCol, QTableWidgetItem(row['Step Message']))
                except KeyError:
                    print('KeyError for updateLogTableWidget, QTableWidgetItem')

                rowIndex += 1

            self.logTableWidget.setHorizontalHeaderLabels(self.logTableHeader)
            self.logTableWidget.setAlternatingRowColors(True)
            self.logTableWidget.resizeColumnsToContents()
            self.logTableWidget.setColumnWidth(descriptionCol, 20)

    def openLogFile(self):
        if self.polarionTableView.model():
            selectionModel = self.polarionTableView.selectionModel()

            openList = []

            for each in selectionModel.selectedIndexes():
                item = self.polarionTableViewModel.item(each.row(), 0)
                openList.append(item.text())
            try:
                filePaths = [self.logDict[x]['filePath'] for x in openList]

                for p in filePaths:
                    if os.path.exists(str(p)):
                        os.startfile(str(p))

            except KeyError:
                self.statusbar.showMessage('No log file found.')
        else:
            self.statusbar.showMessage('No model found.')

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
        debug = ~debug
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
                'Use [{}] to store reports?'.format(newCsvReportFolder),
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
        self.statusbar.showMessage('You have unsaved changes.')

    def newProfile(self):
        self.setDefaultProfile()
        self.profileFile = ''
        self.setTitle('Untitled Profile')
        self.updateGuiFromProfileDict()
        self.statusbar.showMessage('Default profile loaded.')

    def browseProfile(self):
        profileFolder = os.path.dirname(self.profileFile)
        filePath, fileType = QFileDialog.getOpenFileName(
            self,
            "Open Profile",
            profileFolder,
            "JSON Files (*.json);;All Files (*)"
        )

        if filePath:
            self.profileFile = filePath
            self.loadProfile()
            self.saveSettings()

    def browsePolarionExcel(self):
        filePath = self.browseFile(self.polarionExcelEdit.text(), 'Select Polarion TestCase Excel File', 'Excel Files (*.xlsx)')
        self.polarionExcelEdit.setText(filePath)

        msgReply = QMessageBox.question(
            self,
            'KA File Path',
            'Use default KA file path?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if msgReply == QMessageBox.Yes:
            fileName = self.polarionExcelEdit.text()[:-5]
            fileExtension = self.polarionExcelEdit.text()[-4:]
            kaFilePath = '{}_KA.xlsm'.format(fileName)
            self.testCaseExcelEdit.setText(kaFilePath)

    def browseTestCaseExcel(self):
        filePath = self.browseFile(self.testCaseExcelEdit.text(), 'Select Test Case Excel File', 'Excel Files (*.xlsm)')
        self.testCaseExcelEdit.setText(filePath)

    def browseCallFunction(self):
        self.callFunctionEdit.setText(self.browseFolder(self.callFunctionEdit.text(), 'Select Call Function Directory'))

    def browseCsvReport(self):
        self.browseFolder(self.csvReportEdit, 'Select CSV Report Directory')

    def browseVariablePool(self):
        filePath = self.browseFile(self.variablePoolEdit.text(), 'Open Variable Pool', 'TXT Files (*.txt)')
        self.variablePoolEdit.setText(filePath)
        self.loadVariablePool()

    def browseFile(self, filePath='', titleDialog='', fileType=''):
        if len(filePath) > 0:
            folder = str(os.path.dirname(filePath))
        else:
            folder = ''

        openFilePath, openFileType = QFileDialog.getOpenFileName(
            self,
            titleDialog,
            folder,
            "{};;All Files (*)".format(fileType)
        )

        return openFilePath.replace('/', '\\') if len(openFilePath) > 0 else filePath

    def browseFolder(self, folder, title):
        folderPath = QFileDialog.getExistingDirectory(self, title, folder)

        return folderPath.replace('/', '\\') if len(folderPath) > 0 else folder

    def browseTbxFile(self):
        filePath = self.browseFile(self.tbxLineEdit.text(), 'Select TBX file', 'TBX Files (*.tbx)')
        self.tbxLineEdit.setText(filePath)

    def tbx2text(self):
        import xmltodict

        txtEdit = self.tbxPlainTextEdit
        txtEdit.clear()
        try:
            with open(self.tbxLineEdit.text(), 'r') as f:
                xml_input = f.read()

                testCase = xmltodict.parse(xml_input)

                dob = testCase['TemplateBlock']['Block']['DataObjects']['DOB']
                titleDescNames = [x['@Name'].strip('\'') for x in dob]
                title = dob[titleDescNames.index('Title')]['@Value'].strip('\'')
                desc = dob[titleDescNames.index('Desc')]['@Value'].strip('\'')

                self.tbxTitleLineEdit.setText(title)
                self.tbxDescLineEdit.setText(desc)

                blocks = testCase['TemplateBlock']['Block']['SubSystems']['Block']

                for i, block in enumerate(blocks):
                    blockLink = block['@CustomLibraryLink'].strip('\'')
                    blockName = blockLink.split('.')[-1]
                    blockEnable = block['@EnableMode']

                    dataObjects = block['InheritedDataObjects']['DOB']
                    dataObjectsNames = [x['@Name'].strip('\'') for x in block['InheritedDataObjects']['DOB']]

                    action = dataObjects[dataObjectsNames.index('Action')]['@Value']
                    desc = dataObjects[dataObjectsNames.index('Descrip')]['@Value']
                    variable = dataObjects[dataObjectsNames.index('Variable')]['@Value']
                    settings = dataObjects[dataObjectsNames.index('Settings')]['@Value']
                    value = dataObjects[dataObjectsNames.index('Value')]['@Value']
                    wait = dataObjects[dataObjectsNames.index('Wait')]['@Value']
                    remarks = dataObjects[dataObjectsNames.index('Remarks')]['@Value']

                    def checkValue(s):
                        if isinstance(s, str):
                            s = s.strip('\'')
                            return '-' if len(s) == 0 else s
                        return str(s)

                    if eval(blockEnable):
                        stepList = [checkValue(x) for x in [blockName, desc, variable, settings, value, wait, remarks]]
                        txtEdit.appendPlainText('\t'.join(stepList))
        except KeyError as e:
            print(e)

    def tbxCopy(self, edit):
        edit.selectAll()
        edit.copy()

    def newConfig(self):
        self.setDefaultConfigDict()

    def saveProfile(self):
        configFolder = os.path.dirname(str(self.configFile))

        # save config file as well
        self.saveSettings()
        self.makeRunList()
        self.savePolarionJson()

        # updates the profile dict before dumping to json
        self.updateProfileDictFromGui()

        try:
            with open(self.profileFile, 'w') as f:
                jsonDump = json.dumps(self.profileDict)
                f.write(jsonDump)
                self.setTitle(self.profileFile)
                self.defaultProfile = False
                self.changesSaved = True
                self.statusbar.showMessage('Saving Profile...OK!')

        except FileNotFoundError:
            self.statusbar.showMessage('Unable to save profile.')

    def saveAsProfile(self):
        profileFolder = os.path.dirname(self.profileFile)
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Save Profile As",
            profileFolder,
            "JSON Files (*.json);;All Files (*)"
        )

        if filePath:
            self.profileFile = filePath
            self.saveProfile()

    def updateProfileDictFromGui(self):
        """Updates the profile dict from GUI elements."""

        # generate the log mode number based on checkboxes
        logMode = (self.logRadioBtn0.isChecked() + self.logRadioBtn1.isChecked() * 2 + self.logRadioBtn2.isChecked() * 3) - 1

        # update signal list
        signalList = []
        for i in range(0, self.addSignalModel.rowCount()):
            signalList.append(self.addSignalModel.item(i, 0).text())


        dtcExList = []
        dtcModel = self.dtcTableModel
        dtcHexCodeCol = self.dtcTableHeader.index('Hex Code')
        dtcDescCol = self.dtcTableHeader.index('Description')
        dtcModuleCol = self.dtcTableHeader.index('Module')

        for row in range(0, dtcModel.rowCount()):
            hexCode = dtcModel.item(row, dtcHexCodeCol).text()
            desc = dtcModel.item(row, dtcDescCol).text()
            module = dtcModel.item(row, dtcModuleCol).text()
            dtcExList.append({
                'Hex Code': hexCode,
                'Description': desc,
                'Module': module,
            })

        versionDict = {}
        versionModel = self.versionTableModel
        versionHeader = self.versionTableHeader

        swCol = versionHeader.index('Software')
        hwCol = versionHeader.index('Hardware')
        ecuCol = versionHeader.index('ECU')
        for row in range(0, versionModel.rowCount()):
            ecu = versionModel.item(row, ecuCol).text()
            sw = versionModel.item(row, swCol).text()
            hw = versionModel.item(row, hwCol).text()

            try:
                versionDict[ecu] = {
                    'Software': sw,
                    'Hardware': hw,
                }
            except:
                pass

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
                },
                'Versions': versionDict,
            }
        }

    def dtcTableModelItemChanged(self, item):
        model = self.dtcTableModel
        header = self.dtcTableHeader
        try:
            dtcExList = self.profileDict['Profile']['DTC']['Except']
            row = item.row()
            column = item.column()
            colName = header[column]

            if column > 0:
                # print(row, colName, item.text())
                try:
                    dtcExList[row][colName] = item.text()
                except:
                    pass
        except KeyError:
            print('KeyError for dtcTableModelItemChanged, profileDict')

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
                self.statusbar.showMessage('Duplicate signal. Try again.')

            if foundInVp and not foundInModel:
                self.addSignalModel.appendRow(QStandardItem(self.addSignalEdit.text()))
                self.addSignalEdit.clear()
                self.addSignalEdit.setFocus()
                self.statusbar.showMessage('Signal added...OK!')
        except:
            self.statusbar.showMessage('Signal not found in variable pool.')

    def removeSignal(self):
        self.addSignalModel.removeRow(self.addSignalListView.currentIndex().row())

    def addDtcEx2(self):
        hexCode = self.addDtcExEdit.text()
        model = self.dtcTableModel

        model.appendRow([QStandardItem(x) for x in [hexCode, '', '']])
        self.addDtcExEdit.clear()
        self.addDtcExEdit.setFocus()
        self.statusbar.showMessage('DTC exception added...OK!')

    def removeDtcEx2(self):
        selectedIndexes = self.dtcTableView.selectedIndexes()
        model = self.dtcTableModel
        for i in selectedIndexes:
            model.removeRow(i.row())

    def saveSettings(self):
        self.settings = QSettings('AutomationGUI', 'AutomationGUI')
        self.settings.setValue('AutoRun', self.autorunCheckBox.isChecked())
        self.settings.setValue('AutoRunTimer', int(self.autorunSpinBox.value()))
        self.settings.setValue('LastProfile', self.profileFile)
        self.settings.setValue('Width', self.width())
        self.settings.setValue('Height', self.height())
        self.settings.setValue('PolarionUsername', self.polarionUsername)
        self.settings.setValue('PolarionLeftTableWidth', self.polarionTableView.width())

        del self.settings

    def loadProfile(self):
        try:
            with open(self.profileFile) as f:
                self.profileDict = json.load(f)

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
                        self.statusbar.showMessage('Variable pool file not found.')
                    profileValid &= True
                except:
                    debugPrint('No variable pool file defined in profile.')
                    self.statusbar.showMessage('No variable pool file found.')

                if profileValid:
                    # updates the gui after loading a valid profile
                    self.defaultProfile = False
                    self.updateGuiFromProfileDict()
                    if os.path.exists(str(varpoolfile)):
                        self.loadVariablePool()
                    self.setTitle(self.profileFile)
                    self.statusbar.showMessage('Profile loaded OK!')
                else:
                    self.statusbar.showMessage('Invalid profile detected.')
        except IOError:
            # self.newProfile()
            self.statusbar.showMessage('Profile does not exist. Please load profile.')
        except ValueError:
            self.statusbar.showMessage('No valid profile found.')

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
        if path is not None:
            basename = os.path.basename(str(path))
            if not os.path.exists(path):
                msgReply = QMessageBox.question(
                    self,
                    'Varpool Not Found',
                    'Varpool {} does not exist. Browse for one?'.format(basename),
                    # '\'' + basename + '\'' + ' file was not found. Would you like to browse for one?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )

                if msgReply == QMessageBox.Yes:
                    self.browseVariablePool()

    # read all log files and extract data
    def getLogDict(self):
        """Enumerate the latest log files and extract results"""

        class getLogDictThread(QThread):
            showLoadingBarSignal = pyqtSignal()
            hideLoadingBarSignal = pyqtSignal()

            def __init__(self):
                QThread.__init__(self)

            def run(self):
                self.showLoadingBarSignal.emit()
                # enumerate the log folder and determine the latest log files
                for fileName in os.listdir(self.csvReportFolder):
                    if fileName.endswith('.csv'):
                        filePath = os.path.join(self.csvReportFolder, fileName)
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
                    statusMessage = []

                    filePath = None

                    try:
                        filePath = self.logDict[t]['filePath']
                    except KeyError:
                        pass

                    if filePath is not None:
                        with open(filePath) as csvFile:
                            csvReader = csv.DictReader(csvFile)
                            for row in csvReader:
                                try:
                                    passList.append(row['Step Verdict'])
                                except KeyError:
                                    pass
                                try:
                                    actualResult.append(row['Actual Value'])
                                except KeyError:
                                    pass
                                try:
                                    statusMessage.append(row['Step Message'])
                                except KeyError:
                                    pass
                                if len(row['Test Case Verdict']) > 0:
                                    testCaseVerdict = row['Test Case Verdict']
                                if len(row['Test Comment']) > 0:
                                    testComment = row['Test Comment']

                        self.logDict[t]['testCaseVerdict'] = testCaseVerdict
                        self.logDict[t]['testComment'] = testComment
                        self.logDict[t]['actualResult'] = actualResult
                        self.logDict[t]['passList'] = passList
                        self.logDict[t]['length'] = len(passList)

                self.hideLoadingBarSignal.emit()

        self.logDict.clear()
        self.getLogDictThread = getLogDictThread()

        myThread = self.getLogDictThread
        myThread.logDict = self.logDict
        myThread.showLoadingBarSignal.connect(self.showLoadingBar)
        myThread.hideLoadingBarSignal.connect(self.hideLoadingBar)
        myThread.hideLoadingBarSignal.connect(self.saveLogResults)
        myThread.csvReportFolder = self.csvReportEdit.text()
        myThread.start()

    def polarionCopyRunList(self):
        """Copy the yes/no rerun list to clipboard."""
        runtestCol = self.polarionTableHeader.index('Run Test')
        testCaseCol = self.polarionTableHeader.index('TestCase')
        self.polarionTableView.sortByColumn(testCaseCol, Qt.AscendingOrder)
        self.polarionTableView.selectColumn(runtestCol)
        selectionModel = self.polarionTableView.selectionModel()
        selectedIndexes = selectionModel.selectedIndexes()

        if len(selectedIndexes) > 0:
            copyList = []

            for each in selectedIndexes:
                item = self.polarionTableViewModel.item(each.row(), each.column())
                copyList.append(item.text())

            copyString = '\n'.join(copyList)

            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(copyString, mode=cb.Clipboard)

            self.statusbar.showMessage('Copy Yes/No successful.')

    def savePolarionExcel(self):
        """Save to Polarion excel file"""
        class savePolarionExcelThread(QThread):
            showLoadingBarSignal = pyqtSignal()
            hideLoadingBarSignal = pyqtSignal()
            appendMessageSignal = pyqtSignal('PyQt_PyObject')
            updatePolarionRevisionSignal = pyqtSignal()

            def __init__(self):
                QThread.__init__(self)

            def run(self):
                if len(self.filePath) > 0:
                    self.showLoadingBarSignal.emit()
                    try:
                        # udpate polarion excel file

                        if self.polarionWb:
                            self.polarionWb.close()

                        self.polarionWb = load_workbook(filename=self.polarionExcelPath)
                        self.polarionWs = self.polarionWb.active

                        # self.updatePolarionRevisionSignal.emit()

                        count = 0
                        for t in self.polarionDict:
                            try:
                                if self.polarionDict[t]['length'] == self.logDict[t]['length']:
                                    if self.polarionDict[t]['testCaseVerdict'] in ['Passed', 'Deferred', 'Error']:
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
                                        self.polarionWs[testCaseVerdictCellIndex].value = self.logDict[t][
                                            'testCaseVerdict']

                                        testCaseCommentIndex = 'P{}'.format(startRow)
                                        self.polarionWs[testCaseCommentIndex].value = self.logDict[t]['testComment']

                                        count += 1
                            except KeyError:
                                pass

                        self.polarionWb.save(self.filePath)
                        self.appendMessageSignal.emit('Save successful.')
                    except IOError as error:
                        if str(error).__contains__('Permission denied'):
                            self.appendMessageSignal.emit('Permission Denied. Unable to save excel file.')
                    self.hideLoadingBarSignal.emit()

        folder = os.path.dirname(self.polarionExcelEdit.text())
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Save Polarion Excel File",
            folder,
            'XLSX Files (*.xlsx);;All Files (*)'
        )

        self.savePolarionExcelThreadObject = savePolarionExcelThread()
        myThread = self.savePolarionExcelThreadObject
        myThread.filePath = filePath
        myThread.polarionExcelPath = self.polarionExcelEdit.text()
        myThread.polarionWb = self.polarionWb
        myThread.polarionWs = self.polarionWs
        myThread.polarionDict = self.polarionDict
        myThread.logDict = self.logDict
        myThread.showLoadingBarSignal.connect(self.showLoadingBar)
        myThread.hideLoadingBarSignal.connect(self.hideLoadingBar)
        myThread.appendMessageSignal.connect(self.appendPolarionLog)
        myThread.updatePolarionRevisionSignal.connect(self.udpatePolarionRevision)
        myThread.start()

    def readPolarionExcel(self):
        """Read and process the polarion excel file in a thread."""
        class readPolarionExcelThread(QThread):
            finishedSignal = pyqtSignal('PyQt_PyObject')
            updatePolarionRevisionSignal = pyqtSignal('PyQt_PyObject')
            appendMessageSignal = pyqtSignal('PyQt_PyObject')

            def __init__(self):
                QThread.__init__(self)


            def run(self):
                self.appendMessageSignal.emit('Loading Polarion excel.')

                # self.polarionWb = load_workbook(filename=self.polarionExcel, read_only=True)
                # self.polarionWs = self.polarionWb['Sheet1']
                book = xlrd.open_workbook(filename=self.polarionExcel)
                sheet = book.sheet_by_name('Sheet1')

                self.appendMessageSignal.emit('Loading Polarion excel...OK')
                self.appendMessageSignal.emit('Reading Polarion excel data.')

                testStepList = []
                self.polarionDict.clear()
                startRow = 0
                endRow = 0
                testCaseIdCol = 0
                titleCol = 1
                descCol = 2
                stepCol = 3
                waitCol = 10
                if sheet.nrows > 1:
                    for i in range(1, sheet.nrows + 1):
                        try:
                            row = sheet.row_values(i, 0, 16)
                        except IndexError:
                            pass

                        testCaseStep = row[stepCol]
                        if testCaseStep in ['1', '1.0', 1, 1.0] or i == sheet.nrows:
                            if len(testStepList) > 0:
                                endRow = i
                                length = len(testStepList)
                                startRow = endRow - length + 1
                                title = testStepList[0][titleCol]
                                desc = testStepList[0][descCol]

                                def conv2float(x):
                                    try:
                                        return float(x)
                                    except:
                                        return 0.0

                                totalWaitTime = round(sum([conv2float(x[waitCol]) for x in testStepList]), 1)

                                self.polarionDict[testStepList[0][testCaseIdCol]] = {
                                    'title': title,
                                    'desc': desc,
                                    'steps': copy.copy(testStepList),
                                    'startRow': startRow,
                                    'endRow': endRow,
                                    'length': length,
                                    'testCaseVerdict': '',
                                    'hyperlinks': '',
                                    'run': 'No',
                                    'totalWaitTime': totalWaitTime
                                }
                                testStepList = []
                        testStepList.append(row)


                    # read revision number
                    revisionSheet = book.sheet_by_name('_polarion')

                    for i in range(0, revisionSheet.nrows):
                        row = revisionSheet.row_values(i, 0, 1)
                        if row[0] == 'testRunRevision':
                            revisionRow = i
                            revisionNumber = revisionSheet.cell_value(revisionRow, 1)
                            self.updatePolarionRevisionSignal.emit(revisionNumber)
                            break

                # maxRow = self.polarionWs.max_row
                # maxCol = 16
                #
                # # def conv2str(y):
                # # 	if type(y) is unicode:
                # # 		return y.encode('utf-8') if y is not None else None
                # # 	else:
                # # 		return '{}'.format(y) if y is not None else None
                # # 	return None
                #
                # polarionData = [x for x in
                #                 self.polarionWs.iter_rows(min_row=2, max_row=maxRow, min_col=1, max_col=maxCol,
                #                                           values_only=True)]
                #
                # testStepList = []
                # self.polarionDict = OrderedDict()
                # startRow = 0
                # endRow = 0
                # testCaseIdCol = 0
                # titleCol = 1
                # descCol = 2
                # stepCol = 3
                #
                # for i, row in enumerate(polarionData):
                #     testCaseStep = row[stepCol]
                #     if testCaseStep in ['1', '1.0', 1, 1.0] or i == len(polarionData) - 1:
                #         if len(testStepList) > 0:
                #             endRow = i + 1
                #             length = len(testStepList)
                #             startRow = endRow - length + 1
                #             title = testStepList[0][titleCol]
                #             desc = testStepList[0][descCol]
                #
                #             self.polarionDict[testStepList[0][testCaseIdCol]] = {
                #                 'title': title,
                #                 'desc': desc,
                #                 'steps': copy.copy(testStepList),
                #                 'startRow': startRow,
                #                 'endRow': endRow,
                #                 'length': length,
                #                 'testCaseVerdict': '',
                #                 'hyperlinks': '',
                #                 'update': False
                #             }
                #             testStepList = []
                #     testStepList.append(row)

                # # grab necessary columns to work from polarion excel file
                # testCaseIdCol = self.polarionWs['A']  # test case names
                # stepNumberCol = self.polarionWs['D']  # step numbers
                #
                # # get all testcase names and row start
                # allSteps = [str(x.value).replace('.0','') for x in stepNumberCol]
                #
                # while (allSteps[-1] == 'None' or allSteps[-1] == ''):
                #     allSteps.pop()
                #
                # # read revision number
                # revisionWs = self.polarionWb['_polarion']
                # polarionColA = [x.value for x in revisionWs['A']]
                # revisionRow = polarionColA.index('testRunRevision') + 1
                # revision = str(revisionWs.cell(row=revisionRow, column=2).value)
                # self.updatePolarionRevisionSignal.emit(revision)
                #
                # startMarker = '1'
                # endMarker = '1'
                #
                # for eachRow in testCaseIdCol:
                #     if re.match('\w+-\w+', str(eachRow.value)) is not None:
                #         testCase = str(eachRow.value)
                #         # grab the start and end row for each test case
                #         start = allSteps.index(startMarker, eachRow.row - 1) + 1
                #         try:
                #             end = allSteps.index(endMarker, start + 1)
                #         except ValueError:
                #             end = len(allSteps)
                #
                #         self.polarionDict[testCase] = OrderedDict()
                #         self.polarionDict[testCase]['startRow'] = start
                #         self.polarionDict[testCase]['endRow'] = end
                #         self.polarionDict[testCase]['length'] = end - start + 1
                #         self.polarionDict[testCase]['testCaseVerdict'] = ''
                #         self.polarionDict[testCase]['hyperlinks'] = ''
                #         self.polarionDict[testCase]['update'] = False


                self.finishedSignal.emit('Reading Polarion excel data...OK')

        self.showLoadingBar()

        self.polarionDict.clear()
        self.polarionTableViewModel.clear()
        self.polarionTableView.model().clear()
        self.polarionReadExcelThread = readPolarionExcelThread()
        myThread = self.polarionReadExcelThread
        myThread.polarionDict = self.polarionDict
        # myThread.polarionWb = self.polarionWb
        # myThread.polarionWs = self.polarionWs
        myThread.getLogDict = self.getLogDict
        myThread.polarionExcel = self.polarionExcelEdit.text()
        # myThread.loadPolarionWorkBook = self.loadPolarionWorkBook
        myThread.appendMessageSignal.connect(self.appendPolarionLog)
        myThread.updatePolarionRevisionSignal.connect(self.polarionRevisionLineEdit.setText)
        myThread.finishedSignal.connect(self.polarionReadExcelFinished)
        myThread.start()

    def loadPolarionWorkBook(self):
        polarionExcel = self.polarionExcelEdit.text()
        self.polarionWb = load_workbook(filename=polarionExcel, read_only=True)
        self.polarionWs = self.polarionWb.active
        if self.polarionReadExcelThread is not None:
            self.polarionReadExcelThread.polarionWb = self.polarionWb
            self.polarionReadExcelThread.polarionWs = self.polarionWs

    def updateDtcTableView(self):
        self.dtcTableHeader = [
            'Hex Code',
            'Description',
            'Module',
        ]
        model = self.dtcTableModel
        view = self.dtcTableView
        model.setHorizontalHeaderLabels(self.dtcTableHeader)
        view.resizeColumnsToContents()

    def updateVersionTableModel(self):
        self.versionTableHeader = [
            'ECU',
            'Software',
            'Hardware'
        ]

        # self.versionDict = {
        #     'VCMB': {'Hardware': '00_00', 'Software': '00_16'},
        #     'VCMS': {'Hardware': '00_00', 'Software': '00_21'}
        # }


        header = self.versionTableHeader
        view = self.versionTableView
        model = self.versionTableModel
        model.setHorizontalHeaderLabels(header)

        try:
            versionDict = self.profileDict['Profile']['Versions']
            ecuCol = header.index('ECU')
            swVersionCol = header.index('Software')
            hwVersionCol = header.index('Hardware')

            for ecu in versionDict:
                ecuItem = QStandardItem(ecu)
                ecuItem.setEditable(False)
                swVersionItem = QStandardItem(versionDict[ecu]['Software'])
                hwVersionItem = QStandardItem(versionDict[ecu]['Hardware'])
                model.appendRow([ecuItem, swVersionItem, hwVersionItem])


            view.resizeColumnsToContents()
            view.setAlternatingRowColors(True)
        except KeyError:
            print('There was an error with updating version table model')

    def versionAddRow(self):
        model = self.versionTableModel
        model.appendRow(QStandardItem(''))

    def versionRemoveRow(self):
        model = self.versionTableModel
        selectedIndexes = self.versionTableView.selectedIndexes()

        for s in selectedIndexes:
            model.removeRow(s.row())

    def versionTableViewItemChanged(self, item):
        model = self.versionTableModel
        header = self.versionTableHeader
        row = item.row()
        column = item.column()
        versionDict = self.profileDict['Profile']['Versions']
        ecuCol = header.index('ECU')
        ecu = model.item(row, ecuCol).text()
        colName = header[column]
        if column > 0 and len(ecu) > 0:
            try:
                versionDict[ecu][colName] = item.text()
            except KeyError:
                versionDict[ecu] = {}
                versionDict[ecu][colName] = item.text()

    def polarionReadExcelFinished(self, msg):
        self.savePolarionJson()
        self.appendPolarionLog(msg)
        self.updatePolarionTableModel()

    def updatePolarionTableModel(self):
        """Update the model for polarion table view."""
        model = self.polarionTableViewModel

        self.polarionTableHeader = ['TestCase', 'Steps', 'Total Wait Time', 'Run Test',
                                    'TestCase Verdict',
                                    'Hyperlinks']

        testCaseCol = self.polarionTableHeader.index('TestCase')
        # startRowCol = self.polarionTableHeader.index('StartRow')
        # endRowCol = self.polarionTableHeader.index('EndRow')
        stepsTotalCol = self.polarionTableHeader.index('Steps')
        totalWaitTimeCol = self.polarionTableHeader.index('Total Wait Time')
        runTestCol = self.polarionTableHeader.index('Run Test')
        stepVerdictCol = self.polarionTableHeader.index('TestCase Verdict')
        hyperlinksCol = self.polarionTableHeader.index('Hyperlinks')

        for row, d in enumerate(self.polarionDict):
            testCaseItem = QStandardItem(d)
            testCaseItem.setCheckable(True)
            testCaseItem.setEditable(False)
            model.setItem(row, testCaseCol, testCaseItem)

            try:
                lengthItem = QStandardItem()
                lengthItem.setData(self.polarionDict[d]['length'], Qt.DisplayRole)
                lengthItem.setEditable(False)
                model.setItem(row, stepsTotalCol, lengthItem)
            except KeyError:
                pass

            try:
                timeItem = QStandardItem()
                timeItem.setData(self.polarionDict[d]['totalWaitTime'], Qt.DisplayRole)
                timeItem.setEditable(False)
                model.setItem(row, totalWaitTimeCol, timeItem)
            except KeyError:
                pass

            try:
                testCaseVerdict = self.polarionDict[d]['testCaseVerdict']
                testCaseVerdictItem = QStandardItem(testCaseVerdict)
                testCaseVerdictItem.setEditable(False)
            except KeyError:
                pass

            try:
                runTest = self.polarionDict[d]['run']
                runTestItem = QStandardItem(runTest)
                runTestItem.setCheckable(True)
                if runTest == 'Yes':
                    # runTestItem.setIcon(QIcon(':/icon/checkBoxChecked'))
                    runTestItem.setCheckState(Qt.Checked)
                else:
                    # runTestItem.setIcon(QIcon(':/icon/checkBoxBlank'))
                    runTestItem.setCheckState(Qt.Unchecked)
                runTestItem.setEditable(False)
                model.setItem(row, runTestCol, runTestItem)
            except KeyError:
                model.setItem(row, runTestCol, QStandardItem('No'))

            if testCaseVerdict == 'Passed':
                testCaseVerdictItem.setIcon(QIcon(':/icon/passed'))
            elif testCaseVerdict == 'Deferred' or testCaseVerdict == 'Error' or testCaseVerdict == 'Not Passed':
                testCaseVerdictItem.setIcon(QIcon(':/icon/failed'))


            model.setItem(row, stepVerdictCol, testCaseVerdictItem)
            hyperlinksItem = QStandardItem(self.polarionDict[d]['hyperlinks'])
            hyperlinksItem.setEditable(False)
            model.setItem(row, hyperlinksCol, hyperlinksItem)

        model.setHorizontalHeaderLabels(self.polarionTableHeader)
        # testCaseIdHeaderItem = model.horizontalHeaderItem(testCaseCol)
        # testCaseIdHeaderItem.setCheckable(True)

        self.polarionTableView.resizeColumnsToContents()
        self.polarionTableView.setColumnWidth(testCaseCol, 150)

        self.polarionTableView.setSortingEnabled(True)
        self.polarionTableView.sortByColumn(testCaseCol, Qt.AscendingOrder)
        # self.polarionTableView.setAlternatingRowColors(True)

        allTestCaseVerdicts = [self.logDict[x]['testCaseVerdict'] for x in self.logDict]

        passedTotal = allTestCaseVerdicts.count('Passed')
        deferredTotal = allTestCaseVerdicts.count('Deferred')
        errorTotal = allTestCaseVerdicts.count('Error')
        total = passedTotal + deferredTotal + errorTotal

        self.polarionOverViewLineEdit.setText(
            'Total Logs Found: {}    Passed: {}    Deferred: {}    Error: {}'.format(total, passedTotal, deferredTotal,
                                                                                     errorTotal))
        self.hideLoadingBar()

        self.polarionTableViewModel.itemChanged.connect(self.polarionTableViewModelItemChanged)

    # update polarion dict with 'passed' only test cases
    def updatePolarionVerdicts(self, testCaseVerdict=''):
        self.getLogDict()
        self.getLogDictThread.hideLoadingBarSignal.connect(lambda: self.updatePolarionDict(testCaseVerdict))

    def updatePolarionDict(self, testCaseVerdict):
        for t in self.polarionDict:
            self.polarionDict[t]['testCaseVerdict'] = ''

            try:
                if self.polarionDict[t]['length'] == self.logDict[t]['length']:
                    if self.logDict[t]['testCaseVerdict'] == testCaseVerdict or testCaseVerdict == 'All':
                        self.polarionDict[t]['testCaseVerdict'] = self.logDict[t]['testCaseVerdict']
                else:
                    self.polarionDict[t]['testCaseVerdict'] = 'Log steps mismatch'
            except KeyError:
                self.polarionDict[t]['testCaseVerdict'] = 'No log found'

        self.updatePolarionTableModel()
        self.appendPolarionLog('Updated excel file with {} verdicts.'.format(testCaseVerdict))
        self.getLogDictThread.disconnect()

    # update revision number in polarion excel
    def udpatePolarionRevision(self):
        polarionWs = self.polarionWb['_polarion']
        polarionColA = [x.value for x in polarionWs['A']]
        revisionRow = polarionColA.index('testRunRevision') + 1
        polarionWs.cell(row=revisionRow, column=2).value = self.polarionRevisionLineEdit.text()

        self.appendPolarionLog('Updated Polarion revision number.')

    def updateHyperlinks(self):
        class updateHyperlinksThread(QThread):
            showLoadingBarSignal = pyqtSignal()
            hideLoadingBarSignal = pyqtSignal()
            finishedSignal = pyqtSignal('PyQt_PyObject')
            appendMessageSignal = pyqtSignal('PyQt_PyObject')

            def __init__(self):
                QThread.__init__(self)

            class TransportSubclass(zeep.transports.Transport):
                def __init__(self, *args, **kwargs):
                    super(self.__class__, self).__init__(*args, **kwargs)
                    self.last_response = None

                def post(self, *args, **kwargs):
                    self.last_response = super(self.__class__, self).post(*args, **kwargs)
                    return self.last_response

            def run(self):
                # login session and get session id
                session = requests.Session()
                transport = self.TransportSubclass(session=session)
                loginClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/SessionWebService?wsdl'
                try:
                    loginClient = zeep.Client(wsdl=loginClientWsdl, transport=transport)

                    try:
                        loginClient.service.logIn(self.username, self.password)

                        self.showLoadingBarSignal.emit()
                        # grab repsonse header and parse for session id
                        root = etree.XML(transport.last_response.content)
                        sessions = root.xpath('//ns1:sessionID', namespaces={'ns1': 'http://ws.polarion.com/session'})
                        session_id = sessions[0]

                        # use the new session id for transports
                        transport = zeep.transports.Transport(session=session)

                        # use session id for web service
                        testWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TestManagementWebService?wsdl'
                        testClient = zeep.Client(testWsdl, transport=transport)
                        testClient._default_soapheaders = [session_id]

                        # use session id for web service
                        trackerClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TrackerWebService?wsdl'
                        trackerClient = zeep.Client(trackerClientWsdl, transport=transport)
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
                    except zeep.exceptions.Fault as error:
                        if error.message.__contains__('Authentication failed'):
                            self.appendMessageSignal.emit('Authentication failed. Invalid username or password.')

                except requests.exceptions.HTTPError:
                    self.appendMessageSignal.emit('Unable to pull hyperlinks.')
                    pass

                self.hideLoadingBarSignal.emit()

        self.getPolarionAccount()

        if self.polarionUsername != '' and self.polarionPassword != '':
            self.updateHyperlinksThreadObject = updateHyperlinksThread()
            myThread = self.updateHyperlinksThreadObject
            myThread.polarionDict = self.polarionDict
            myThread.appendMessageSignal.connect(self.appendPolarionLog)
            myThread.showLoadingBarSignal.connect(self.showLoadingBar)
            myThread.hideLoadingBarSignal.connect(self.hideLoadingBar)
            myThread.username = self.polarionUsername
            myThread.password = self.polarionPassword
            myThread.finishedSignal.connect(self.updatePolarionDictWithHyperlinks)
            myThread.start()

    def updatePolarionSteps(self):
        class updatePolarionStepsThread(QThread):
            finishedSignal = pyqtSignal('PyQt_PyObject')
            appendMessageSignal = pyqtSignal('PyQt_PyObject')
            showLoadingBarSignal = pyqtSignal()
            hideLoadingBarSignal = pyqtSignal()

            def __init__(self):
                QThread.__init__(self)

            class TransportSubclass(zeep.transports.Transport):
                def __init__(self, *args, **kwargs):
                    super(self.__class__, self).__init__(*args, **kwargs)
                    self.last_response = None

                def post(self, *args, **kwargs):
                    self.last_response = super(self.__class__, self).post(*args, **kwargs)
                    return self.last_response

            def run(self):
                try:
                    self.appendMessageSignal.emit('Connecting to Polarion server.')

                    # login session and get session id
                    session = requests.Session()
                    transport = self.TransportSubclass(session=session)
                    loginClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/SessionWebService?wsdl'
                    loginClient = zeep.Client(wsdl=loginClientWsdl, transport=transport)

                    try:
                        loginClient.service.logIn(self.username, self.password)
                        self.showLoadingBarSignal.emit()
                        # grab repsonse header and parse for session id
                        root = etree.XML(transport.last_response.content)
                        sessions = root.xpath('//ns1:sessionID', namespaces={'ns1': 'http://ws.polarion.com/session'})
                        session_id = sessions[0]

                        # use the new session id for transports
                        transport = zeep.transports.Transport(session=session)

                        # use session id for web service
                        testWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TestManagementWebService?wsdl'
                        testClient = zeep.Client(testWsdl, transport=transport)
                        testClient._default_soapheaders = [session_id]

                        # use session id for web service
                        trackerClientWsdl = 'http://polarion.karmaautomotive.com/polarion/ws/services/TrackerWebService?wsdl'
                        trackerClient = zeep.Client(trackerClientWsdl, transport=transport)
                        trackerClient._default_soapheaders = [session_id]

                        self.appendMessageSignal.emit('Connected to Polarion server.')

                        # teExcel = r"C:\Users\pthil\Desktop\Test_Runs\K1_20_TestRun\BL_1000\BL_1000_Beta\SCM_Manual_V13\K1-20-1000_SCM_Manual_V13_KA_TE.xlsx"
                        wb = load_workbook(self.teExcelPath)
                        ws = wb.active


                        testCaseIdCol = ws['A']
                        stepNumberCol = ws['H']

                        allSteps = [str(x.value) for x in stepNumberCol]

                        polarionDict = OrderedDict()
                        startMarker = '1'
                        endMarker = 'None'

                        querySteps = None

                        # grab data from polarion excel
                        self.appendMessageSignal.emit('Grabbing data from excel file.')
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
                        self.appendMessageSignal.emit('Updating testcases.')
                        for id in self.testCasesList:
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
                                        self.appendMessageSignal.emit('Updated {}. Steps: {} -> {}.'.format(id, len(querySteps), len(updatedQuerySteps)))
                                        # time.sleep(2.0)
                            else:
                                self.appendMessageSignal.emit('{} was not found'.format(id))
                                # print(id, 'not found.')

                        # close session
                        loginClient.service.endSession()
                        self.finishedSignal.emit('Updating Polarion finished.')
                        self.appendMessageSignal.emit('Updating Polarion finished.')
                    except zeep.exceptions.Fault as error:
                        if error.message.__contains__('Authentication failed'):
                            self.appendMessageSignal.emit('Authentication failed. Invalid username or password.')
                except:
                    self.hideLoadingBarSignal.emit()

        teExcelPath = self.browseFile(self.polarionExcelEdit.text(), 'Open Polarion TE excel file', 'XLSX Files (*.xlsx)')

        # teExcelPath, fileType = QFileDialog.getOpenFileName(
        #     self.parent(),
        #     "Open Polarion TE File",
        #     '',
        #     "XLSX Files (*.xlsx);;All Files (*)"
        # )

        self.getPolarionAccount()

        if len(teExcelPath) > 0 and self.polarionUsername != '' and self.polarionPassword != '':
            self.udpatePolarionStepsThread = updatePolarionStepsThread()
            myThread = self.udpatePolarionStepsThread

            myThread.teExcelPath = teExcelPath
            myThread.polarionDict = self.polarionDict
            myThread.username = self.polarionUsername
            myThread.password = self.polarionPassword

            testCasesList = []
            model = self.polarionTableViewModel
            rowCount = model.rowCount()
            testCaseCol = self.polarionTableHeader.index('TestCase')

            for i in range(0, rowCount):
                item = model.item(i, testCaseCol)
                if item.checkState():
                    testCasesList.append(item.text())

            myThread.testCasesList = testCasesList
            myThread.appendMessageSignal.connect(self.appendPolarionLog)
            myThread.showLoadingBarSignal.connect(self.showLoadingBar)
            myThread.hideLoadingBarSignal.connect(self.hideLoadingBar)
            myThread.finishedSignal.connect(self.updatePolarionDictWithQuerySteps)
            myThread.start()
        else:
            self.appendPolarionLog('Update steps cancelled.')

    def getPolarionAccount(self):
        username, okPressed1 = QInputDialog.getText(self, 'Enter Polarion Account', 'Username:',
                                                    QLineEdit.Normal, self.polarionUsername)
        password, okPressed2 = QInputDialog.getText(self, 'Enter Polarion Account', 'Password:',
                                                    QLineEdit.Password, self.polarionPassword)

        if okPressed1:
            self.polarionUsername = username
        if okPressed2:
            self.polarionPassword = password

    def appendPolarionLog(self, msg):
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

        self.savePolarionJson()
        self.appendPolarionLog('Updated Polarion table with hyperlinks.')
        self.updatePolarionTableModel()

    # use the profile dictionary to update the gui
    def updateGuiFromProfileDict(self):
        # print(self.profileDict)
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
            # self.checkVarPoolExist(varPoolPath)
        except KeyError:
            self.variablePoolEdit.setText('')

        try:
            dtcExceptionEnable = self.profileDict['Profile']['DTC']['@enable']
            self.dtcExCheckBox.setChecked(dtcExceptionEnable)
            self.showDtcException(dtcExceptionEnable)
        except KeyError:
            self.dtcExCheckBox.setChecked(False)
            self.showDtcException(False)
        except TypeError:
            print('TypeError: eval() arg 1 must be a string or code object')

        try:
            callFunctionDebug = self.profileDict['Profile']['CallFunctionDebug']['@enable']
            self.callFunctionDebugCheckbox.setChecked(callFunctionDebug)
        except KeyError:
            self.callFunctionDebugCheckbox.setChecked(False)

        try:
            versionCheckbox = self.profileDict['Profile']['Version']['@include']
            self.versionCheckBox.setChecked(versionCheckbox)
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

        # self.dtcExModel.clear()
        #
        # # if temp is a list we iterate and add, else we append a single element
        # try:
        #     exceptlist = self.profileDict['Profile']['DTC']['Except']
        #     dtcExList = []
        #     if isinstance(exceptlist, list):
        #         dtcExList.extend(x for x in exceptlist)
        #     else:
        #         dtcExList.append(exceptlist)
        #
        #     # add rows into qt list widget
        #     for s in dtcExList:
        #         self.dtcExModel.appendRow(QStandardItem(str(s)))
        # except KeyError:
        #     debugPrint('DTCs exception list is empty')

        self.dtcTableModel.clear()
        try:
            dtcExList = self.profileDict['Profile']['DTC']['Except']

            for dtc in dtcExList:
                self.dtcTableModel.appendRow([QStandardItem(x) for x in [dtc['Hex Code'], dtc['Description'], dtc['Module']]])
        except:
            print('KeyError for updateGuiFromProfileDict, dtcExList2')

        self.updateVersionTableModel()

    def loadSettings(self):
        self.settings = QSettings('AutomationGUI', 'AutomationGUI')
        self.profileFile = self.settings.value('LastProfile', type=str)
        autoRun = self.settings.value('AutoRun', type=bool)
        self.autorunCheckBox.setChecked(autoRun)
        self.autorunSpinBox.setValue(self.settings.value('AutoRunTimer', type=int))
        width = self.settings.value('Width', type=int)
        height = self.settings.value('Height', type=int)
        self.resize(width, height)
        self.polarionUsername = self.settings.value('PolarionUsername', type=str)

        polarionLeftTableWidth = self.settings.value('PolarionLeftTableWidth', type=int)

        self.polarionTableView.resize(polarionLeftTableWidth, self.polarionTableView.height())

        if os.path.exists(self.profileFile):
            self.loadProfile()

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
                    self.statusbar.showMessage('Variable pool loaded...OK!')
            except FileNotFoundError:
                self.statusbar.showMessage('Variable pool file not found.')

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

        self.saveSettings()
        self.makeRunList()
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
        pixmap = QPixmap(':/icon/karma')
        pixmap = pixmap.scaledToWidth(128)
        about.setIconPixmap(pixmap)
        about.exec_()

def main(aud=None):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    form = App(aud)
    form.show()
    app.exec_()
    return form.runList, form.profileDict, form.variablePoolDict  # return data to AutomationDesk

if __name__ == '__main__':
    main(aud=None)