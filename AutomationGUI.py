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
import csv
from datetime import datetime
from openpyxl import load_workbook
from collections import OrderedDict
from functools import partial

if sys.version_info[0] < 3:
    FileNotFoundError = IOError

debug = False

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
        self.logDict = {}
        # dict to hold data from polarion sheet
        self.polarionDict = OrderedDict()
        self.variablePoolDict = {}
        self.updateVariablePool = False  # update variable pool in AutomationDesk
        self.defaultProfile = True  # false when a profile is loaded

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

        # test case excel toolbutton

        self.testCaseExcelToolButton.setPopupMode(QToolButton.InstantPopup)
        testCaseExcelMenu = QMenu()

        openTestCaseExcelFileAction = QAction(QIcon(':/svg/icons/excel.svg'), 'Open Test Case File', self)
        openTestCaseExcelFileAction.triggered.connect(self.openTestCaseExcelFile)
        testCaseExcelMenu.addAction(openTestCaseExcelFileAction)

        openTestCaseExcelFolderAction = QAction(QIcon(':/svg/icons/folder.svg'), 'Open Test Case Folder', self)
        openTestCaseExcelFolderAction.triggered.connect(self.openTestCaseExcelFolder)
        testCaseExcelMenu.addAction(openTestCaseExcelFolderAction)

        self.testCaseExcelToolButton.setMenu(testCaseExcelMenu)

        # csv report toolbutton

        self.csvReportFolderToolButton.setPopupMode(QToolButton.InstantPopup)
        csvReportFolderMenu = QMenu()

        openCsvReportFolderAction = QAction(QIcon(':/svg/icons/folder.svg'), 'Open Report Folder', self)
        openCsvReportFolderAction.triggered.connect(self.openCsvReportFolder)
        csvReportFolderMenu.addAction(openCsvReportFolderAction)

        useTestCasePathAction = QAction(QIcon(':/svg/icons/folder.svg'), 'Use {TestCaseFolder}\\Logs', self)
        useTestCasePathAction.triggered.connect(self.useTestCasePath)
        csvReportFolderMenu.addAction(useTestCasePathAction)

        self.csvReportFolderToolButton.setMenu(csvReportFolderMenu)

        # call function toolbutton

        self.callFunctionFolderToolButton.setPopupMode(QToolButton.InstantPopup)
        callFunctionFolderMenu = QMenu()

        openCallFunctionFolderAction = QAction(QIcon(':/svg/icons/folder.svg'), 'Open Call Function Folder', self)
        openCallFunctionFolderAction.triggered.connect(self.openCallFunctionFolder)
        callFunctionFolderMenu.addAction(openCallFunctionFolderAction)

        self.callFunctionFolderToolButton.setMenu(callFunctionFolderMenu)

        # variable pool toolbutton

        self.variablePoolToolButton.setPopupMode(QToolButton.InstantPopup)
        variablePoolMenu = QMenu()

        openVariablePoolFileAction = QAction(QIcon(':/svg/icons/file.svg'), 'Open Variable Pool File', self)
        openVariablePoolFileAction.triggered.connect(self.openVarPoolFile)
        variablePoolMenu.addAction(openVariablePoolFileAction)

        openVariablePoolFolderAction = QAction(QIcon(':/svg/icons/folder.svg'), 'Open Variable Pool Folder', self)
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
        self.processRunListButton.clicked.connect(self.getRunList)
        self.copyButton.clicked.connect(self.copyRunList)

        # polarion tab
        self.polarionReadExcelButton.clicked.connect(self.readPolarion)
        self.polarionUpdatePassedButton.clicked.connect(partial(self.polarionUpdateExcel, 'Passed'))
        self.polarionUpdateAllButton.clicked.connect(partial(self.polarionUpdateExcel, 'All'))
        self.polarionSaveExcelButton.clicked.connect(self.polarionSaveExcel)
        self.polarionUpdateRevisionButton.clicked.connect(self.polarionUpdateRevision)

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

        self.progressBar.setValue(0)
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

    # updates the profile dict
    def updateProfileDictFromGui(self):
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
                    self.setItem(i, j + 1, QStandardItem(str(data[d][p])))

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
    def getRunList(self):
        self.progressBar.setValue(10)

        # grab the active worksheet
        wb = load_workbook(self.testCaseExcelEdit.text())
        ws = wb.active

        self.progressBar.setValue(20)
        # grab the test case column
        testCaseColumn = ws['K']

        # less the header name and empty row, get only the test case names
        runList = [str(each.value) for each in testCaseColumn][2:]

        # remove empty or none entries
        while runList[-1] == 'None' or runList[-1] == '':
            runList.pop()

        self.progressBar.setValue(30)
        self.getLogDict()

        self.progressBar.setValue(50)
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

        self.progressBar.setValue(70)
        runDict = OrderedDict()

        for t in runList:
            try:
                if self.logDict[t]['testCaseVerdict'] == 'Passed':
                    runDict[t] = {'run': 'No',
                                  'testCaseVerdict': self.logDict[t]['testCaseVerdict']}
                else:
                    runDict[t] = {'run': 'Yes',
                                  'testCaseVerdict': self.logDict[t]['testCaseVerdict']}
            except KeyError as error:
                print('KeyError:', str(error))
                runDict[t] = {'run': 'Yes',
                              'testCaseVerdict': 'Not Found'}

        header = ['TestCase', 'TestCase Verdict', 'Run']

        model = self.MyItemModel(runDict, header)

        self.runTableView.setModel(model)
        self.runTableView.resizeColumnToContents(0)
        self.runTableView.setSortingEnabled(True)
        self.runTableView.sortByColumn(0, Qt.AscendingOrder)

        self.progressBar.setValue(100)

    # copy the run list
    def copyRunList(self):
        model = self.runTableView.model()

        rowCount = model.rowCount()
        runList = [model.item(x, 2).text() for x in range(0, rowCount)]
        runListString = '\n'.join(runList)

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(runListString, mode=cb.Clipboard)

        self.statusbar.showMessage('Run list copied.')

    def readPolarion(self):
        startTime = datetime.now()
        self.progressBar.setValue(10)
        polarionExcel = self.polarionExcelEdit.text()
        self.wb = load_workbook(filename=polarionExcel)
        self.ws = self.wb.active

        # grab necessary columns to work from polarion excel file
        testCaseNameCol = self.ws['A']  # test case names
        stepNumberCol = self.ws['D']  # step numbers
        # actualResultCol = self.ws['M']  # actual result
        # stepVerdictCol = self.ws['N']  # step verdict
        # testCaseVerdictCol = self.ws['O']  # test case verdict
        # testCommentCol = self.ws['P']  # test comment

        # get all testcase names and row start
        allSteps = list(filter(lambda x: x != None, [x.value for x in stepNumberCol]))
        i = 1

        polarionWs = self.wb['_polarion']
        polarionColA = [x.value for x in polarionWs['A']]
        revisionRow = polarionColA.index('testRunRevision') + 1
        self.polarionRevisionLineEdit.setText(str(polarionWs.cell(row=revisionRow, column=2).value))


        for eachRow in testCaseNameCol:
            if eachRow.value is not None and eachRow.value != 'ID':
                testCase = eachRow.value
                # grab the start and end row for each test case
                start = i
                try:
                    end = allSteps.index(1, i + 1)
                except ValueError:
                    end = len(allSteps)
                i = end
                self.polarionDict[testCase] = OrderedDict()
                self.polarionDict[testCase]['startRow'] = start
                self.polarionDict[testCase]['endRow'] = end
                self.polarionDict[testCase]['length'] = end - start
                self.polarionDict[testCase]['testCaseVerdict'] = '-'


        self.progressBar.setValue(40)
        self.getLogDict()
        self.progressBar.setValue(70)


        #
        # # self.wb.save('UpdatePolarionSheet.xlsx')
        #
        # timeDiff = datetime.now() - startTime
        # print('Time Elapsed:', timeDiff.__str__())
        #
        # allTestCaseVerdicts = [self.logDict[x]['testCaseVerdict'] for x in self.logDict]
        #
        # passedTotal = allTestCaseVerdicts.count('Passed')
        # deferredTotal = allTestCaseVerdicts.count('Deferred')
        # errorTotal = allTestCaseVerdicts.count('Error')
        #
        # print('Passed:', passedTotal)
        # print('Deferred:', deferredTotal)
        # print('Error:', errorTotal)
        # print('Total:', passedTotal + deferredTotal + errorTotal)

        # def getError(x, errorType):
        #     if self.logDict[x]['testCaseVerdict'] == errorType:
        #         return (x)

        # passedList = list(filter(lambda x: x != None, [getError(x, 'Passed') for x in self.logDict]))
        # deferredList = list(filter(lambda x: x != None, [getError(x, 'Deferred') for x in self.logDict]))
        # errorList = list(filter(lambda x: x != None, [getError(x, 'Error') for x in self.logDict]))


        header = ['TestCase', 'StartRow', 'EndRow', 'Steps', 'TestCase Verdict']

        model = self.MyItemModel(self.polarionDict, header)

        self.polarionTableView.setModel(model)
        self.polarionTableView.resizeColumnToContents(0)
        self.polarionTableView.setSortingEnabled(True)
        self.polarionTableView.sortByColumn(0, Qt.AscendingOrder)

        self.progressBar.setValue(100)

        self.statusbar.showMessage('Polarion file read sucessfully.')

    # update polarion dict with 'passed' only test cases
    def polarionUpdateExcel(self, testCaseVerdict='Passed'):
        for t in self.polarionDict:
            try:
                if testCaseVerdict == 'All':
                    useCriteria = True
                else:
                    useCriteria = self.logDict[t]['testCaseVerdict'] == testCaseVerdict

                if self.polarionDict[t]['length'] == self.logDict[t]['length'] and useCriteria:
                    self.polarionDict[t]['testCaseVerdict'] = self.logDict[t]['testCaseVerdict']
            except KeyError as error:
                print('{} not found'.format(str(error)))

        header = ['TestCase', 'StartRow', 'EndRow', 'Steps', 'TestCase Verdict']

        model = self.MyItemModel(self.polarionDict, header)

        self.polarionTableView.setModel(model)
        self.polarionTableView.resizeColumnToContents(0)
        self.polarionTableView.setSortingEnabled(True)
        self.polarionTableView.sortByColumn(0, Qt.AscendingOrder)

        self.ws = self.wb.active

        # grab necessary columns to work from polarion excel file
        actualResultCol = self.ws['M']  # actual result
        stepVerdictCol = self.ws['N']  # step verdict
        testCaseVerdictCol = self.ws['O']  # test case verdict
        testCommentCol = self.ws['P']  # test comment

        count = 0
        for t in self.polarionDict:
            try:
                if testCaseVerdict == 'All':
                    useCriteria = True
                else:
                    useCriteria = self.logDict[t]['testCaseVerdict'] == testCaseVerdict

                if self.polarionDict[t]['length'] == self.logDict[t]['length'] and useCriteria:
                    # print(t, 'Match')
                    startRow = self.polarionDict[t]['startRow']
                    endRow = self.polarionDict[t]['endRow']

                    actualResultRows = actualResultCol[startRow:endRow]
                    for row, actual in zip(actualResultRows, self.logDict[t]['actualResult']):
                        row.value = actual

                    stepVerdictRows = stepVerdictCol[startRow:endRow]
                    for row, verdict in zip(stepVerdictRows, self.logDict[t]['passList']):
                        row.value = verdict

                    testCaseVerdictCol[startRow].value = self.logDict[t]['testCaseVerdict']
                    testCommentCol[startRow].value = self.logDict[t]['testComment']

                    count += 1
            # else:
            # 	print('{} does not match'.format(t))
            except KeyError as error:
                print('{} not found'.format(str(error)))

        self.statusbar.showMessage('Updated Polarion Dictionary with {} testcases.'.format(testCaseVerdict))

    # update revision number in polarion excel
    def polarionUpdateRevision(self):
        polarionWs = self.wb['_polarion']
        polarionColA = [x.value for x in polarionWs['A']]
        revisionRow = polarionColA.index('testRunRevision') + 1
        polarionWs.cell(row=revisionRow, column=2).value = self.polarionRevisionLineEdit.text()

        self.statusbar.showMessage('Updated Polarion Revision Number.')

    def polarionSaveExcel(self):
        folder = os.path.dirname(self.polarionExcelEdit.text())
        filePath, fileType = QFileDialog.getSaveFileName(
            self,
            "Open Profile",
            folder,
            'XLSX Files (*.xlsx);;All Files (*)'
        )
        if len(filePath) > 0:
            self.wb.save(filePath)

        self.statusbar.showMessage('Save successful.')

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
        about.setText('Version 1.28\nDeveloper: Vu Le')
        about.setInformativeText('Copyright (C) 2018')
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
