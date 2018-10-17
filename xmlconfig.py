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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/graphics/development_python_32px_540419_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow, QFrame {\n"
"    background-color: rgb(208, 218, 232);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgba(0, 0, 0, 0.8);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton#reloadVariablePoolBtn {\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: rgba(255, 255, 255, 0.5);\n"
"    padding: 2px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    min-height: 30px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit,  QListView{\n"
"    background-color: white;\n"
"    border: 1px solid  rgba(0, 0, 0, 0.2);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit:hover, QListView:hover {\n"
"    border: 1px solid  rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(253, 236, 218, 0.6), stop:0.4 rgba(253, 223, 186, 0.6), stop:0.42 rgba(255, 206, 105, 0.6), stop:0.9 rgba(255, 206, 105, 0.6), stop:1 rgba(255, 255, 215, 0.6));\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"    min-height: 40px;\n"
"    padding: 0px 5px 0px 5px;\n"
"    border-bottom: 1px solid rgba(255, 206, 105, 0.8);\n"
"    border-right: 1px solid  rgba(255, 206, 105, 0.8);\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(253, 236, 218, 255), stop:0.4 rgba(253, 223, 186, 255), stop:0.42 rgba(255, 206, 105, 255), stop:0.9 rgba(255, 206, 105, 255), stop:1 rgba(255, 255, 215, 255));\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(0, 0, 0, 0.2);\n"
"    border-radius: 8px;\n"
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
"    color: black;\n"
"    border-top: 1px solid rgba(0, 0, 0, 0.2);\n"
"    background-color: rgb(208, 218, 232);\n"
"}\n"
"\n"
"QTabWidget::pane, QStackedWidget {\n"
"    border-bottom-left-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-left: 1px solid  rgba(0, 0, 0, 0.1);\n"
"    border-bottom: 1px solid  rgba(0, 0, 0, 0.4);\n"
"    border-right: 1px solid rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 0px;\n"
"    padding: 10px;\n"
"    min-width: 120px;\n"
"    top: 2px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-left: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-top: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-right: 1px solid rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color:rgb(245, 245, 245);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    color: black;\n"
"    background-color: rgb(191, 205, 219);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(20, 21, 23);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(20, 21, 23);\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    border:1px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu, QMenu::item, QMenuBar, QMenuBar::item {\n"
"    color: black;\n"
"    background-color: rgb(245, 245, 245);\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected, QMenu::item:selected {\n"
"    color: black;\n"
"    background-color:  rgba(0, 0, 0, 0.1);\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color: rgb(20, 21, 23);\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"    padding: 5px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: rgba(255, 255, 255, 1.0);\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked, QRadioButton::indicator::unchecked {\n"
"    image: url(:/checkbox/graphics/baseline_radio_button_unchecked_black_24dp.png);\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QCheckBox::indicator:checked:pressed {\n"
"    image: url(:/checkbox/graphics/baseline_check_circle_black_24dp.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QRadioButton::indicator:checked:pressed {\n"
"    image: url(:/checkbox/graphics/baseline_radio_button_checked_black_24dp.png);\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 761, 331))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 711, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.browseVariablePoolBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.browseVariablePoolBtn.setObjectName("browseVariablePoolBtn")
        self.gridLayout.addWidget(self.browseVariablePoolBtn, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.variablePoolEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.variablePoolEdit.setObjectName("variablePoolEdit")
        self.gridLayout.addWidget(self.variablePoolEdit, 2, 1, 1, 1)
        self.versionCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionCheckBox.sizePolicy().hasHeightForWidth())
        self.versionCheckBox.setSizePolicy(sizePolicy)
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
        self.browseCsvReportBtn.setObjectName("browseCsvReportBtn")
        self.gridLayout.addWidget(self.browseCsvReportBtn, 1, 2, 1, 1)
        self.reloadVariablePoolBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.reloadVariablePoolBtn.setFlat(False)
        self.reloadVariablePoolBtn.setObjectName("reloadVariablePoolBtn")
        self.gridLayout.addWidget(self.reloadVariablePoolBtn, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 291, 151))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logRadioBtn0.sizePolicy().hasHeightForWidth())
        self.logRadioBtn0.setSizePolicy(sizePolicy)
        self.logRadioBtn0.setObjectName("logRadioBtn0")
        self.gridLayout_2.addWidget(self.logRadioBtn0, 0, 0, 1, 1)
        self.addSignalGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.addSignalGroupBox.setGeometry(QtCore.QRect(330, 10, 411, 261))
        self.addSignalGroupBox.setObjectName("addSignalGroupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.addSignalGroupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 281, 211))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addSignalEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.addSignalEdit.setObjectName("addSignalEdit")
        self.gridLayout_3.addWidget(self.addSignalEdit, 2, 0, 1, 1)
        self.addSignalListView = QtWidgets.QListView(self.layoutWidget2)
        self.addSignalListView.setEnabled(True)
        self.addSignalListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addSignalListView.setObjectName("addSignalListView")
        self.gridLayout_3.addWidget(self.addSignalListView, 1, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.addSignalGroupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(310, 30, 91, 91))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addSignalBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.addSignalBtn.setObjectName("addSignalBtn")
        self.verticalLayout.addWidget(self.addSignalBtn)
        self.removeSignalBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.removeSignalBtn.setObjectName("removeSignalBtn")
        self.verticalLayout.addWidget(self.removeSignalBtn)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.dtcExGroupBox = QtWidgets.QGroupBox(self.tab_3)
        self.dtcExGroupBox.setGeometry(QtCore.QRect(140, 20, 521, 251))
        self.dtcExGroupBox.setObjectName("dtcExGroupBox")
        self.layoutWidget4 = QtWidgets.QWidget(self.dtcExGroupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(410, 30, 91, 127))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addDtcExBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.addDtcExBtn.setObjectName("addDtcExBtn")
        self.verticalLayout_2.addWidget(self.addDtcExBtn)
        self.removeDtcExBtn = QtWidgets.QPushButton(self.layoutWidget4)
        self.removeDtcExBtn.setObjectName("removeDtcExBtn")
        self.verticalLayout_2.addWidget(self.removeDtcExBtn)
        self.layoutWidget5 = QtWidgets.QWidget(self.dtcExGroupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 30, 391, 211))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.addDtcExEdit = QtWidgets.QLineEdit(self.layoutWidget5)
        self.addDtcExEdit.setObjectName("addDtcExEdit")
        self.gridLayout_4.addWidget(self.addDtcExEdit, 1, 0, 1, 2)
        self.dtcExListView = QtWidgets.QListView(self.layoutWidget5)
        self.dtcExListView.setObjectName("dtcExListView")
        self.gridLayout_4.addWidget(self.dtcExListView, 0, 0, 1, 2)
        self.dtcExCheckBox = QtWidgets.QCheckBox(self.tab_3)
        self.dtcExCheckBox.setGeometry(QtCore.QRect(20, 20, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtcExCheckBox.sizePolicy().hasHeightForWidth())
        self.dtcExCheckBox.setSizePolicy(sizePolicy)
        self.dtcExCheckBox.setObjectName("dtcExCheckBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 418))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget6 = QtWidgets.QWidget(self.frame)
        self.layoutWidget6.setGeometry(QtCore.QRect(460, 360, 326, 52))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.saveAsBtn = QtWidgets.QPushButton(self.layoutWidget6)
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.gridLayout_5.addWidget(self.saveAsBtn, 0, 0, 1, 1)
        self.saveBtn = QtWidgets.QPushButton(self.layoutWidget6)
        self.saveBtn.setFlat(False)
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout_5.addWidget(self.saveBtn, 0, 1, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_5.addWidget(self.exitButton, 0, 2, 1, 1)
        self.frame.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 40))
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
        self.tabWidget.setCurrentIndex(0)
        self.saveBtn.clicked.connect(self.actionSave.trigger)
        self.saveAsBtn.clicked.connect(self.actionSaveAs.trigger)
        self.exitButton.clicked.connect(self.actionExit.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.addSignalGroupBox.setTitle(_translate("MainWindow", "Additional Signal List"))
        self.addSignalBtn.setText(_translate("MainWindow", "Add"))
        self.removeSignalBtn.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Logging"))
        self.dtcExGroupBox.setTitle(_translate("MainWindow", "DTC Exception List"))
        self.addDtcExBtn.setText(_translate("MainWindow", "Add"))
        self.removeDtcExBtn.setText(_translate("MainWindow", "Remove"))
        self.dtcExCheckBox.setText(_translate("MainWindow", "Enable"))
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
