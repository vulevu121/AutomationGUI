# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xmlconfig.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/graphics/development_python_32px_540419_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(59, 56, 56, 80);\n"
"    height: 40px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0px 10px 0px 10px;\n"
"    left: 10px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background: black;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    background-color: transparent;\n"
"    border: 1px solid lightgray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    padding: 10px;\n"
"    min-width: 150px;\n"
"    top: 2px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid lightgray;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: transparent;\n"
"    border\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(:/checkbox/graphics/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QRadioButton::indicator:checked:pressed, QRadioButton::indicator:checked:hover {\n"
"    image: url(:/checkbox/graphics/checkbox_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/checkbox/graphics/checkbox_hover.png);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(59, 56, 56);\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    border:1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu, QMenu::item {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QMenuBar::item:selected, QMenu::item:selected {\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked, QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(:/checkbox/graphics/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QCheckBox::indicator:checked:pressed, QCheckBox::indicator:checked:hover {\n"
"    image: url(:/checkbox/graphics/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/checkbox/graphics/checkbox_hover.png);\n"
"}\n"
"\n"
"QListView {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#reloadVariablePoolBtn {\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgLabel.setObjectName("bgLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 761, 351))
        self.tabWidget.setStyleSheet("QWidget {\n"
"    background-color: transparent;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 711, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.browseVariablePoolBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.browseVariablePoolBtn.setFlat(True)
        self.browseVariablePoolBtn.setObjectName("browseVariablePoolBtn")
        self.gridLayout.addWidget(self.browseVariablePoolBtn, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.variablePoolEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.variablePoolEdit.setObjectName("variablePoolEdit")
        self.gridLayout.addWidget(self.variablePoolEdit, 2, 1, 1, 1)
        self.versionCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.versionCheckBox.setObjectName("versionCheckBox")
        self.gridLayout.addWidget(self.versionCheckBox, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.browseCallFunctionBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.browseCallFunctionBtn.setObjectName("browseCallFunctionBtn")
        self.gridLayout.addWidget(self.browseCallFunctionBtn, 0, 2, 1, 1)
        self.callFunctionEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.callFunctionEdit.setObjectName("callFunctionEdit")
        self.gridLayout.addWidget(self.callFunctionEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.csvReportEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.csvReportEdit.setObjectName("csvReportEdit")
        self.gridLayout.addWidget(self.csvReportEdit, 1, 1, 1, 1)
        self.browseCsvReportBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.browseCsvReportBtn.setFlat(True)
        self.browseCsvReportBtn.setObjectName("browseCsvReportBtn")
        self.gridLayout.addWidget(self.browseCsvReportBtn, 1, 2, 1, 1)
        self.reloadVariablePoolBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.reloadVariablePoolBtn.setObjectName("reloadVariablePoolBtn")
        self.gridLayout.addWidget(self.reloadVariablePoolBtn, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 321, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logRadioBtn1 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.logRadioBtn1.setObjectName("logRadioBtn1")
        self.gridLayout_2.addWidget(self.logRadioBtn1, 1, 0, 1, 1)
        self.logRadioBtn2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.logRadioBtn2.setObjectName("logRadioBtn2")
        self.gridLayout_2.addWidget(self.logRadioBtn2, 2, 0, 1, 1)
        self.logRadioBtn0 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.logRadioBtn0.setObjectName("logRadioBtn0")
        self.gridLayout_2.addWidget(self.logRadioBtn0, 0, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 20, 371, 271))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addSignalListView = QtWidgets.QListView(self.layoutWidget2)
        self.addSignalListView.setEnabled(True)
        self.addSignalListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addSignalListView.setObjectName("addSignalListView")
        self.gridLayout_3.addWidget(self.addSignalListView, 1, 0, 1, 2)
        self.addSignalEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.addSignalEdit.setObjectName("addSignalEdit")
        self.gridLayout_3.addWidget(self.addSignalEdit, 2, 0, 1, 2)
        self.addSignalBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.addSignalBtn.setObjectName("addSignalBtn")
        self.gridLayout_3.addWidget(self.addSignalBtn, 3, 0, 1, 1)
        self.removeSignalBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.removeSignalBtn.setObjectName("removeSignalBtn")
        self.gridLayout_3.addWidget(self.removeSignalBtn, 3, 1, 1, 1)
        self.addSignalLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.addSignalLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addSignalLabel.setObjectName("addSignalLabel")
        self.gridLayout_3.addWidget(self.addSignalLabel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 60, 681, 211))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.addDtcExEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.addDtcExEdit.setObjectName("addDtcExEdit")
        self.gridLayout_4.addWidget(self.addDtcExEdit, 1, 0, 1, 2)
        self.addDtcExBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.addDtcExBtn.setObjectName("addDtcExBtn")
        self.gridLayout_4.addWidget(self.addDtcExBtn, 2, 0, 1, 1)
        self.removeDtcExBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.removeDtcExBtn.setObjectName("removeDtcExBtn")
        self.gridLayout_4.addWidget(self.removeDtcExBtn, 2, 1, 1, 1)
        self.dtcExListView = QtWidgets.QListView(self.layoutWidget3)
        self.dtcExListView.setObjectName("dtcExListView")
        self.gridLayout_4.addWidget(self.dtcExListView, 0, 0, 1, 2)
        self.dtcExCheckBox = QtWidgets.QCheckBox(self.tab_3)
        self.dtcExCheckBox.setGeometry(QtCore.QRect(40, 20, 336, 32))
        self.dtcExCheckBox.setObjectName("dtcExCheckBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(460, 380, 321, 44))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.saveAsBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.gridLayout_5.addWidget(self.saveAsBtn, 0, 0, 1, 1)
        self.saveBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.saveBtn.setFlat(True)
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout_5.addWidget(self.saveBtn, 0, 1, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_5.addWidget(self.exitButton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpenConfigFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenConfigFolder.setObjectName("actionOpenConfigFolder")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpenConfigFolder)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.saveBtn.clicked.connect(self.actionSave.trigger)
        self.saveAsBtn.clicked.connect(self.actionSaveAs.trigger)
        self.exitButton.clicked.connect(self.actionExit.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bgLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.browseVariablePoolBtn.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "VariablePool CSV File"))
        self.versionCheckBox.setText(_translate("MainWindow", "Include HW && SW Version"))
        self.label_5.setText(_translate("MainWindow", "Call Function Folder"))
        self.browseCallFunctionBtn.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "CSV Report Folder"))
        self.browseCsvReportBtn.setText(_translate("MainWindow", "Browse"))
        self.reloadVariablePoolBtn.setText(_translate("MainWindow", "Load Variable\n"
"Pool File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.logRadioBtn1.setText(_translate("MainWindow", "Execution with Filtered Logging"))
        self.logRadioBtn2.setText(_translate("MainWindow", "Execution with Full Logging\n"
"and Additional Signals"))
        self.logRadioBtn0.setText(_translate("MainWindow", "Execution Only (Default)"))
        self.addSignalBtn.setText(_translate("MainWindow", "Add"))
        self.removeSignalBtn.setText(_translate("MainWindow", "Remove"))
        self.addSignalLabel.setText(_translate("MainWindow", "Additional Signal List:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Logging"))
        self.addDtcExBtn.setText(_translate("MainWindow", "Add"))
        self.removeDtcExBtn.setText(_translate("MainWindow", "Remove"))
        self.dtcExCheckBox.setText(_translate("MainWindow", "Enabled DTC Exception"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "DTC"))
        self.saveAsBtn.setText(_translate("MainWindow", "Save Profile As"))
        self.saveBtn.setText(_translate("MainWindow", "Save Profile"))
        self.exitButton.setText(_translate("MainWindow", "Continue"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpenConfigFolder.setText(_translate("MainWindow", "Open Config Folder"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))

import xmlconfig_rc
