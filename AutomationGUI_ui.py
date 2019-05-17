# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutomationGUI_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(907, 762)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/karmaIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow, QFrame {\n"
"    background-color: rgb(208, 218, 232);\n"
"    font: 9pt;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgba(0, 0, 0, 0.8);\n"
"    font: 9pt;\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    min-height: 30px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit,  QPlainTextEdit, QListView{\n"
"    background-color: white;\n"
"    border: 1px solid  rgba(0, 0, 0, 0.2);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit:hover, QListView:hover {\n"
"    border: 1px solid  rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #202020;\n"
"}\n"
"\n"
"QToolBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(236, 236, 236, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    spacing: 5px;\n"
"    padding: 8px 8px 8px 8px;\n"
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
"QMenuBar, QMenuBar::item {\n"
"    color: black;\n"
"    background-color: rgb(245, 245, 245);\n"
"    padding: 4px 8px 4px 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu {\n"
"    color: black;\n"
"    background-color: rgb(245, 245, 245);\n"
"    border-radius: 4px;\n"
"    padding: 8px 8px 8px 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    color: black;\n"
"    background-color: rgb(245, 245, 245);\n"
"    border-radius: 4px;\n"
"    padding: 4px 4px 4px 28px;\n"
"}\n"
"\n"
"QMenuBar::item:selected, QMenu::item:selected {\n"
"    color: black;\n"
"    background-color:  rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QMenuBar {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/checkbox/graphics/baseline_radio_button_unchecked_black_24dp.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/checkbox/graphics/baseline_check_circle_black_24dp.png);\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color: rgb(20, 21, 23);\n"
"}\n"
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
"    image: url(:/checkbox/uncheckedButton);\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QCheckBox::indicator:checked:pressed {\n"
"    image: url(:/checkbox/checkedButton);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QRadioButton::indicator:checked:pressed {\n"
"    image: url(:/checkbox/radioCheckedButton);\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("\n"
"QToolBar {\n"
"    background-color: rgb(245, 245, 245);\n"
"    spacing: 5px;\n"
"    padding: 8px 8px 8px 8px;\n"
"}\n"
"\n"
"QPushButton, QToolButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(253, 236, 218, 0.6), stop:0.4 rgba(253, 223, 186, 0.6), stop:0.42 rgba(255, 206, 105, 0.6), stop:0.9 rgba(255, 206, 105, 0.6), stop:1 rgba(255, 255, 215, 0.6));\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"    min-height: 40px;\n"
"    padding: 0px 5px 0px 5px;\n"
"    border-bottom: 1px solid rgba(255, 206, 105, 0.8);\n"
"    border-right: 1px solid  rgba(255, 206, 105, 0.8);\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed, QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(253, 236, 218, 255), stop:0.4 rgba(253, 223, 186, 255), stop:0.42 rgba(255, 206, 105, 255), stop:0.9 rgba(255, 206, 105, 255), stop:1 rgba(255, 255, 215, 255));\n"
"}")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.generalLayout = QtWidgets.QGridLayout()
        self.generalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.generalLayout.setHorizontalSpacing(5)
        self.generalLayout.setVerticalSpacing(8)
        self.generalLayout.setObjectName("generalLayout")
        self.browsePolarionExcelBtn = QtWidgets.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/excelBlackIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browsePolarionExcelBtn.setIcon(icon1)
        self.browsePolarionExcelBtn.setObjectName("browsePolarionExcelBtn")
        self.generalLayout.addWidget(self.browsePolarionExcelBtn, 0, 2, 1, 1)
        self.polarionExcelToolButton = QtWidgets.QToolButton(self.tab)
        self.polarionExcelToolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/menuIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polarionExcelToolButton.setIcon(icon2)
        self.polarionExcelToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.polarionExcelToolButton.setAutoRaise(False)
        self.polarionExcelToolButton.setObjectName("polarionExcelToolButton")
        self.generalLayout.addWidget(self.polarionExcelToolButton, 0, 3, 1, 1)
        self.browseCsvReportBtn = QtWidgets.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/folderOpenIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseCsvReportBtn.setIcon(icon3)
        self.browseCsvReportBtn.setObjectName("browseCsvReportBtn")
        self.generalLayout.addWidget(self.browseCsvReportBtn, 2, 2, 1, 1)
        self.browseTestCaseExcelBtn = QtWidgets.QPushButton(self.tab)
        self.browseTestCaseExcelBtn.setIcon(icon1)
        self.browseTestCaseExcelBtn.setObjectName("browseTestCaseExcelBtn")
        self.generalLayout.addWidget(self.browseTestCaseExcelBtn, 1, 2, 1, 1)
        self.polarionExcelEdit = QtWidgets.QLineEdit(self.tab)
        self.polarionExcelEdit.setObjectName("polarionExcelEdit")
        self.generalLayout.addWidget(self.polarionExcelEdit, 0, 1, 1, 1)
        self.testCaseExcelLabel_2 = QtWidgets.QLabel(self.tab)
        self.testCaseExcelLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.testCaseExcelLabel_2.setObjectName("testCaseExcelLabel_2")
        self.generalLayout.addWidget(self.testCaseExcelLabel_2, 0, 0, 1, 1)
        self.csvReportFolderToolButton = QtWidgets.QToolButton(self.tab)
        self.csvReportFolderToolButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.csvReportFolderToolButton.setIcon(icon2)
        self.csvReportFolderToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.csvReportFolderToolButton.setAutoRaise(False)
        self.csvReportFolderToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.csvReportFolderToolButton.setObjectName("csvReportFolderToolButton")
        self.generalLayout.addWidget(self.csvReportFolderToolButton, 2, 3, 1, 1)
        self.callFunctionFolderToolButton = QtWidgets.QToolButton(self.tab)
        self.callFunctionFolderToolButton.setText("")
        self.callFunctionFolderToolButton.setIcon(icon2)
        self.callFunctionFolderToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.callFunctionFolderToolButton.setObjectName("callFunctionFolderToolButton")
        self.generalLayout.addWidget(self.callFunctionFolderToolButton, 3, 3, 1, 1)
        self.browseVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/copyIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseVariablePoolBtn.setIcon(icon4)
        self.browseVariablePoolBtn.setObjectName("browseVariablePoolBtn")
        self.generalLayout.addWidget(self.browseVariablePoolBtn, 5, 2, 1, 1)
        self.callFunctionLabel = QtWidgets.QLabel(self.tab)
        self.callFunctionLabel.setObjectName("callFunctionLabel")
        self.generalLayout.addWidget(self.callFunctionLabel, 3, 0, 1, 1)
        self.browseCallFunctionBtn = QtWidgets.QPushButton(self.tab)
        self.browseCallFunctionBtn.setIcon(icon3)
        self.browseCallFunctionBtn.setObjectName("browseCallFunctionBtn")
        self.generalLayout.addWidget(self.browseCallFunctionBtn, 3, 2, 1, 1)
        self.csvReportEdit = QtWidgets.QLineEdit(self.tab)
        self.csvReportEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.csvReportEdit.setClearButtonEnabled(False)
        self.csvReportEdit.setObjectName("csvReportEdit")
        self.generalLayout.addWidget(self.csvReportEdit, 2, 1, 1, 1)
        self.variablePoolLabel = QtWidgets.QLabel(self.tab)
        self.variablePoolLabel.setObjectName("variablePoolLabel")
        self.generalLayout.addWidget(self.variablePoolLabel, 5, 0, 1, 1)
        self.csvReportLabel = QtWidgets.QLabel(self.tab)
        self.csvReportLabel.setObjectName("csvReportLabel")
        self.generalLayout.addWidget(self.csvReportLabel, 2, 0, 1, 1)
        self.callFunctionEdit = QtWidgets.QLineEdit(self.tab)
        self.callFunctionEdit.setObjectName("callFunctionEdit")
        self.generalLayout.addWidget(self.callFunctionEdit, 3, 1, 1, 1)
        self.variablePoolEdit = QtWidgets.QLineEdit(self.tab)
        self.variablePoolEdit.setObjectName("variablePoolEdit")
        self.generalLayout.addWidget(self.variablePoolEdit, 5, 1, 1, 1)
        self.testCaseExcelToolButton = QtWidgets.QToolButton(self.tab)
        self.testCaseExcelToolButton.setText("")
        self.testCaseExcelToolButton.setIcon(icon2)
        self.testCaseExcelToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.testCaseExcelToolButton.setObjectName("testCaseExcelToolButton")
        self.generalLayout.addWidget(self.testCaseExcelToolButton, 1, 3, 1, 1)
        self.variablePoolToolButton = QtWidgets.QToolButton(self.tab)
        self.variablePoolToolButton.setText("")
        self.variablePoolToolButton.setIcon(icon2)
        self.variablePoolToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.variablePoolToolButton.setObjectName("variablePoolToolButton")
        self.generalLayout.addWidget(self.variablePoolToolButton, 5, 3, 1, 1)
        self.testCaseExcelLabel = QtWidgets.QLabel(self.tab)
        self.testCaseExcelLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.testCaseExcelLabel.setObjectName("testCaseExcelLabel")
        self.generalLayout.addWidget(self.testCaseExcelLabel, 1, 0, 1, 1)
        self.testCaseExcelEdit = QtWidgets.QLineEdit(self.tab)
        self.testCaseExcelEdit.setObjectName("testCaseExcelEdit")
        self.generalLayout.addWidget(self.testCaseExcelEdit, 1, 1, 1, 1)
        self.reloadVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reloadVariablePoolBtn.sizePolicy().hasHeightForWidth())
        self.reloadVariablePoolBtn.setSizePolicy(sizePolicy)
        self.reloadVariablePoolBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/saveIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadVariablePoolBtn.setIcon(icon5)
        self.reloadVariablePoolBtn.setFlat(False)
        self.reloadVariablePoolBtn.setObjectName("reloadVariablePoolBtn")
        self.generalLayout.addWidget(self.reloadVariablePoolBtn, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13.addLayout(self.generalLayout)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dtcExCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtcExCheckBox.sizePolicy().hasHeightForWidth())
        self.dtcExCheckBox.setSizePolicy(sizePolicy)
        self.dtcExCheckBox.setObjectName("dtcExCheckBox")
        self.horizontalLayout_2.addWidget(self.dtcExCheckBox)
        self.callFunctionDebugCheckbox = QtWidgets.QCheckBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.callFunctionDebugCheckbox.sizePolicy().hasHeightForWidth())
        self.callFunctionDebugCheckbox.setSizePolicy(sizePolicy)
        self.callFunctionDebugCheckbox.setObjectName("callFunctionDebugCheckbox")
        self.horizontalLayout_2.addWidget(self.callFunctionDebugCheckbox)
        self.versionCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionCheckBox.sizePolicy().hasHeightForWidth())
        self.versionCheckBox.setSizePolicy(sizePolicy)
        self.versionCheckBox.setObjectName("versionCheckBox")
        self.horizontalLayout_2.addWidget(self.versionCheckBox)
        self.verticalLayout_13.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.settingsVerticalLayoutRight = QtWidgets.QVBoxLayout()
        self.settingsVerticalLayoutRight.setObjectName("settingsVerticalLayoutRight")
        self.updateVariablePoolCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.updateVariablePoolCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.updateVariablePoolCheckBox.setObjectName("updateVariablePoolCheckBox")
        self.settingsVerticalLayoutRight.addWidget(self.updateVariablePoolCheckBox)
        self.showDebugCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.showDebugCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.showDebugCheckBox.setObjectName("showDebugCheckBox")
        self.settingsVerticalLayoutRight.addWidget(self.showDebugCheckBox)
        self.verticalLayout_7.addLayout(self.settingsVerticalLayoutRight)
        self.verticalLayout_13.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/tuneIcon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loggingTabLayout = QtWidgets.QHBoxLayout()
        self.loggingTabLayout.setObjectName("loggingTabLayout")
        self.logmodeLayout = QtWidgets.QVBoxLayout()
        self.logmodeLayout.setObjectName("logmodeLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logRadioBtn0 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logRadioBtn0.sizePolicy().hasHeightForWidth())
        self.logRadioBtn0.setSizePolicy(sizePolicy)
        self.logRadioBtn0.setObjectName("logRadioBtn0")
        self.verticalLayout_4.addWidget(self.logRadioBtn0)
        self.logRadioBtn1 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logRadioBtn1.sizePolicy().hasHeightForWidth())
        self.logRadioBtn1.setSizePolicy(sizePolicy)
        self.logRadioBtn1.setObjectName("logRadioBtn1")
        self.verticalLayout_4.addWidget(self.logRadioBtn1)
        self.logRadioBtn2 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logRadioBtn2.sizePolicy().hasHeightForWidth())
        self.logRadioBtn2.setSizePolicy(sizePolicy)
        self.logRadioBtn2.setObjectName("logRadioBtn2")
        self.verticalLayout_4.addWidget(self.logRadioBtn2)
        self.logmodeLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.logmodeLayout.addItem(spacerItem1)
        self.loggingTabLayout.addLayout(self.logmodeLayout)
        self.addSignalGroupBox = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSignalGroupBox.sizePolicy().hasHeightForWidth())
        self.addSignalGroupBox.setSizePolicy(sizePolicy)
        self.addSignalGroupBox.setObjectName("addSignalGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.addSignalGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addSignalListView = QtWidgets.QListView(self.addSignalGroupBox)
        self.addSignalListView.setEnabled(True)
        self.addSignalListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addSignalListView.setObjectName("addSignalListView")
        self.verticalLayout_5.addWidget(self.addSignalListView)
        self.addSignalEdit = QtWidgets.QLineEdit(self.addSignalGroupBox)
        self.addSignalEdit.setObjectName("addSignalEdit")
        self.verticalLayout_5.addWidget(self.addSignalEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addSignalBtn = QtWidgets.QPushButton(self.addSignalGroupBox)
        self.addSignalBtn.setObjectName("addSignalBtn")
        self.verticalLayout.addWidget(self.addSignalBtn)
        self.removeSignalBtn = QtWidgets.QPushButton(self.addSignalGroupBox)
        self.removeSignalBtn.setObjectName("removeSignalBtn")
        self.verticalLayout.addWidget(self.removeSignalBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.loggingTabLayout.addWidget(self.addSignalGroupBox)
        self.horizontalLayout_3.addLayout(self.loggingTabLayout)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/recordIcon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon7, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.dtcTabLayout = QtWidgets.QVBoxLayout()
        self.dtcTabLayout.setObjectName("dtcTabLayout")
        self.dtcExGroupBox = QtWidgets.QGroupBox(self.tab_3)
        self.dtcExGroupBox.setObjectName("dtcExGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dtcExGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dtcExListView = QtWidgets.QListView(self.dtcExGroupBox)
        self.dtcExListView.setObjectName("dtcExListView")
        self.verticalLayout_6.addWidget(self.dtcExListView)
        self.addDtcExEdit = QtWidgets.QLineEdit(self.dtcExGroupBox)
        self.addDtcExEdit.setObjectName("addDtcExEdit")
        self.verticalLayout_6.addWidget(self.addDtcExEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addDtcExBtn = QtWidgets.QPushButton(self.dtcExGroupBox)
        self.addDtcExBtn.setObjectName("addDtcExBtn")
        self.verticalLayout_2.addWidget(self.addDtcExBtn)
        self.removeDtcExBtn = QtWidgets.QPushButton(self.dtcExGroupBox)
        self.removeDtcExBtn.setObjectName("removeDtcExBtn")
        self.verticalLayout_2.addWidget(self.removeDtcExBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.dtcTabLayout.addWidget(self.dtcExGroupBox)
        self.horizontalLayout_11.addLayout(self.dtcTabLayout)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/tabSelectedIcon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_3, icon8, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.runTableView = QtWidgets.QTableView(self.tab_5)
        self.runTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.runTableView.setStyleSheet("QFrame, QTableView{\n"
"    background-color: rgb(255, 255, 255)\n"
"}")
        self.runTableView.setAlternatingRowColors(True)
        self.runTableView.setSortingEnabled(True)
        self.runTableView.setObjectName("runTableView")
        self.verticalLayout_11.addWidget(self.runTableView)
        self.dSpaceOverviewLineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.dSpaceOverviewLineEdit.setEnabled(True)
        self.dSpaceOverviewLineEdit.setFrame(True)
        self.dSpaceOverviewLineEdit.setReadOnly(True)
        self.dSpaceOverviewLineEdit.setPlaceholderText("")
        self.dSpaceOverviewLineEdit.setClearButtonEnabled(False)
        self.dSpaceOverviewLineEdit.setObjectName("dSpaceOverviewLineEdit")
        self.verticalLayout_11.addWidget(self.dSpaceOverviewLineEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dSpaceReadExcelButton = QtWidgets.QToolButton(self.tab_5)
        self.dSpaceReadExcelButton.setIcon(icon1)
        self.dSpaceReadExcelButton.setIconSize(QtCore.QSize(24, 24))
        self.dSpaceReadExcelButton.setObjectName("dSpaceReadExcelButton")
        self.verticalLayout_9.addWidget(self.dSpaceReadExcelButton)
        self.copyButton = QtWidgets.QToolButton(self.tab_5)
        self.copyButton.setIcon(icon4)
        self.copyButton.setIconSize(QtCore.QSize(24, 24))
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout_9.addWidget(self.copyButton)
        self.exportExcelButton = QtWidgets.QToolButton(self.tab_5)
        self.exportExcelButton.setIcon(icon5)
        self.exportExcelButton.setIconSize(QtCore.QSize(24, 24))
        self.exportExcelButton.setObjectName("exportExcelButton")
        self.verticalLayout_9.addWidget(self.exportExcelButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/automationDeskIcon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_5, icon9, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.polarionTableView = QtWidgets.QTableView(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polarionTableView.sizePolicy().hasHeightForWidth())
        self.polarionTableView.setSizePolicy(sizePolicy)
        self.polarionTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.polarionTableView.setStyleSheet("QFrame, QTableView{\n"
"    background-color: rgb(255, 255, 255)\n"
"}")
        self.polarionTableView.setAlternatingRowColors(True)
        self.polarionTableView.setSortingEnabled(True)
        self.polarionTableView.setObjectName("polarionTableView")
        self.verticalLayout_12.addWidget(self.polarionTableView)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.polarionOverViewLineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.polarionOverViewLineEdit.setReadOnly(True)
        self.polarionOverViewLineEdit.setObjectName("polarionOverViewLineEdit")
        self.horizontalLayout_7.addWidget(self.polarionOverViewLineEdit)
        self.polarionRevisionLineEdit = QtWidgets.QLineEdit(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polarionRevisionLineEdit.sizePolicy().hasHeightForWidth())
        self.polarionRevisionLineEdit.setSizePolicy(sizePolicy)
        self.polarionRevisionLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.polarionRevisionLineEdit.setObjectName("polarionRevisionLineEdit")
        self.horizontalLayout_7.addWidget(self.polarionRevisionLineEdit)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.polarionLogEdit = QtWidgets.QPlainTextEdit(self.tab_6)
        self.polarionLogEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.polarionLogEdit.setReadOnly(True)
        self.polarionLogEdit.setObjectName("polarionLogEdit")
        self.verticalLayout_12.addWidget(self.polarionLogEdit)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.polarionReadExcelButton = QtWidgets.QToolButton(self.tab_6)
        self.polarionReadExcelButton.setIcon(icon1)
        self.polarionReadExcelButton.setIconSize(QtCore.QSize(24, 24))
        self.polarionReadExcelButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.polarionReadExcelButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.polarionReadExcelButton.setObjectName("polarionReadExcelButton")
        self.verticalLayout_10.addWidget(self.polarionReadExcelButton)
        self.polarionSaveExcelButton = QtWidgets.QToolButton(self.tab_6)
        self.polarionSaveExcelButton.setIcon(icon5)
        self.polarionSaveExcelButton.setIconSize(QtCore.QSize(24, 24))
        self.polarionSaveExcelButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.polarionSaveExcelButton.setObjectName("polarionSaveExcelButton")
        self.verticalLayout_10.addWidget(self.polarionSaveExcelButton)
        self.polarionUpdatePassedButton = QtWidgets.QToolButton(self.tab_6)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/passedVerdictIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polarionUpdatePassedButton.setIcon(icon10)
        self.polarionUpdatePassedButton.setIconSize(QtCore.QSize(24, 24))
        self.polarionUpdatePassedButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.polarionUpdatePassedButton.setObjectName("polarionUpdatePassedButton")
        self.verticalLayout_10.addWidget(self.polarionUpdatePassedButton)
        self.polarionUpdateAllButton = QtWidgets.QToolButton(self.tab_6)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/allVerdictsIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polarionUpdateAllButton.setIcon(icon11)
        self.polarionUpdateAllButton.setIconSize(QtCore.QSize(24, 24))
        self.polarionUpdateAllButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.polarionUpdateAllButton.setObjectName("polarionUpdateAllButton")
        self.verticalLayout_10.addWidget(self.polarionUpdateAllButton)
        self.polarionUpdateRevisionButton = QtWidgets.QToolButton(self.tab_6)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/historyIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polarionUpdateRevisionButton.setIcon(icon12)
        self.polarionUpdateRevisionButton.setIconSize(QtCore.QSize(24, 24))
        self.polarionUpdateRevisionButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.polarionUpdateRevisionButton.setObjectName("polarionUpdateRevisionButton")
        self.verticalLayout_10.addWidget(self.polarionUpdateRevisionButton)
        self.updateStepsButton = QtWidgets.QToolButton(self.tab_6)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/numberedListIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateStepsButton.setIcon(icon13)
        self.updateStepsButton.setIconSize(QtCore.QSize(24, 24))
        self.updateStepsButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.updateStepsButton.setObjectName("updateStepsButton")
        self.verticalLayout_10.addWidget(self.updateStepsButton)
        self.updateHyperlinksButton = QtWidgets.QToolButton(self.tab_6)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/linkIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateHyperlinksButton.setIcon(icon14)
        self.updateHyperlinksButton.setIconSize(QtCore.QSize(24, 24))
        self.updateHyperlinksButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.updateHyperlinksButton.setObjectName("updateHyperlinksButton")
        self.verticalLayout_10.addWidget(self.updateHyperlinksButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icon/polarionIcon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_6, icon15, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.bottombuttonsLayout = QtWidgets.QHBoxLayout()
        self.bottombuttonsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.bottombuttonsLayout.setContentsMargins(0, -1, -1, -1)
        self.bottombuttonsLayout.setObjectName("bottombuttonsLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottombuttonsLayout.addItem(spacerItem6)
        self.autorunSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autorunSpinBox.sizePolicy().hasHeightForWidth())
        self.autorunSpinBox.setSizePolicy(sizePolicy)
        self.autorunSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.autorunSpinBox.setObjectName("autorunSpinBox")
        self.bottombuttonsLayout.addWidget(self.autorunSpinBox)
        self.autorunCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autorunCheckBox.sizePolicy().hasHeightForWidth())
        self.autorunCheckBox.setSizePolicy(sizePolicy)
        self.autorunCheckBox.setChecked(True)
        self.autorunCheckBox.setObjectName("autorunCheckBox")
        self.bottombuttonsLayout.addWidget(self.autorunCheckBox, 0, QtCore.Qt.AlignRight)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_exit_to_app_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon16)
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")
        self.bottombuttonsLayout.addWidget(self.exitButton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.bottombuttonsLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icon/saveColorIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon17)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIcon(icon16)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icon/contactColorIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon18)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConfigFolder = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icon/folderColorIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigFolder.setIcon(icon19)
        self.actionConfigFolder.setObjectName("actionConfigFolder")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setIcon(icon19)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIcon(icon17)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icon/newColorIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon20)
        self.actionNew.setObjectName("actionNew")
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionConfigFolder)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionAbout)
        self.testCaseExcelLabel_2.setBuddy(self.testCaseExcelEdit)
        self.callFunctionLabel.setBuddy(self.callFunctionEdit)
        self.variablePoolLabel.setBuddy(self.variablePoolEdit)
        self.csvReportLabel.setBuddy(self.csvReportEdit)
        self.testCaseExcelLabel.setBuddy(self.testCaseExcelEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.exitButton.clicked.connect(self.actionExit.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.testCaseExcelEdit, self.browseTestCaseExcelBtn)
        MainWindow.setTabOrder(self.browseTestCaseExcelBtn, self.csvReportEdit)
        MainWindow.setTabOrder(self.csvReportEdit, self.browseCsvReportBtn)
        MainWindow.setTabOrder(self.browseCsvReportBtn, self.callFunctionEdit)
        MainWindow.setTabOrder(self.callFunctionEdit, self.browseCallFunctionBtn)
        MainWindow.setTabOrder(self.browseCallFunctionBtn, self.variablePoolEdit)
        MainWindow.setTabOrder(self.variablePoolEdit, self.browseVariablePoolBtn)
        MainWindow.setTabOrder(self.browseVariablePoolBtn, self.exitButton)
        MainWindow.setTabOrder(self.exitButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.variablePoolToolButton)
        MainWindow.setTabOrder(self.variablePoolToolButton, self.callFunctionFolderToolButton)
        MainWindow.setTabOrder(self.callFunctionFolderToolButton, self.csvReportFolderToolButton)
        MainWindow.setTabOrder(self.csvReportFolderToolButton, self.logRadioBtn0)
        MainWindow.setTabOrder(self.logRadioBtn0, self.logRadioBtn1)
        MainWindow.setTabOrder(self.logRadioBtn1, self.logRadioBtn2)
        MainWindow.setTabOrder(self.logRadioBtn2, self.addSignalListView)
        MainWindow.setTabOrder(self.addSignalListView, self.addSignalEdit)
        MainWindow.setTabOrder(self.addSignalEdit, self.addSignalBtn)
        MainWindow.setTabOrder(self.addSignalBtn, self.removeSignalBtn)
        MainWindow.setTabOrder(self.removeSignalBtn, self.dtcExListView)
        MainWindow.setTabOrder(self.dtcExListView, self.addDtcExEdit)
        MainWindow.setTabOrder(self.addDtcExEdit, self.addDtcExBtn)
        MainWindow.setTabOrder(self.addDtcExBtn, self.removeDtcExBtn)
        MainWindow.setTabOrder(self.removeDtcExBtn, self.autorunCheckBox)
        MainWindow.setTabOrder(self.autorunCheckBox, self.testCaseExcelToolButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browsePolarionExcelBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browsePolarionExcelBtn.setText(_translate("MainWindow", "Browse"))
        self.polarionExcelToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.browseCsvReportBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCsvReportBtn.setText(_translate("MainWindow", "Browse"))
        self.browseTestCaseExcelBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseTestCaseExcelBtn.setText(_translate("MainWindow", "Browse"))
        self.polarionExcelEdit.setPlaceholderText(_translate("MainWindow", "Specify Polarion test case excel file"))
        self.testCaseExcelLabel_2.setText(_translate("MainWindow", "<html><head/><body><p>Polarion Excel File</p></body></html>"))
        self.csvReportFolderToolButton.setText(_translate("MainWindow", "..."))
        self.callFunctionFolderToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.browseVariablePoolBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseVariablePoolBtn.setText(_translate("MainWindow", "Browse"))
        self.callFunctionLabel.setText(_translate("MainWindow", "Call Function Folder:"))
        self.browseCallFunctionBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCallFunctionBtn.setText(_translate("MainWindow", "Browse"))
        self.csvReportEdit.setPlaceholderText(_translate("MainWindow", "Specify the CSV report folder"))
        self.variablePoolLabel.setText(_translate("MainWindow", "VariablePool File:"))
        self.csvReportLabel.setText(_translate("MainWindow", "CSV Report Folder:"))
        self.callFunctionEdit.setPlaceholderText(_translate("MainWindow", "Specify the call function folder"))
        self.variablePoolEdit.setPlaceholderText(_translate("MainWindow", "Specify the variable pool text file"))
        self.testCaseExcelToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.variablePoolToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.testCaseExcelLabel.setText(_translate("MainWindow", "<html><head/><body><p>dSPACE Excel File</p></body></html>"))
        self.testCaseExcelEdit.setPlaceholderText(_translate("MainWindow", "Specify dSPACE test case excel file"))
        self.reloadVariablePoolBtn.setToolTip(_translate("MainWindow", "Load Variable Pool"))
        self.reloadVariablePoolBtn.setText(_translate("MainWindow", "Load VariablePool"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Runtime Options"))
        self.dtcExCheckBox.setText(_translate("MainWindow", "Enable DTC Exception(s)"))
        self.callFunctionDebugCheckbox.setText(_translate("MainWindow", "Debug Call Functions"))
        self.versionCheckBox.setText(_translate("MainWindow", "Include HW && SW Version"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tool Options"))
        self.updateVariablePoolCheckBox.setText(_translate("MainWindow", "Update VariablePool in AutomationDesk"))
        self.showDebugCheckBox.setText(_translate("MainWindow", "Console Messages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Logging Mode"))
        self.logRadioBtn0.setText(_translate("MainWindow", "Execution Only (Default)"))
        self.logRadioBtn1.setText(_translate("MainWindow", "Execution with Filtered Logging"))
        self.logRadioBtn2.setText(_translate("MainWindow", "Execution with Full Logging\n"
"and Additional Signals"))
        self.addSignalGroupBox.setTitle(_translate("MainWindow", "Additional Signal List"))
        self.addSignalBtn.setText(_translate("MainWindow", "Add"))
        self.removeSignalBtn.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Logging"))
        self.dtcExGroupBox.setTitle(_translate("MainWindow", "DTC Exception List"))
        self.addDtcExBtn.setText(_translate("MainWindow", "Add"))
        self.removeDtcExBtn.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "DTC"))
        self.dSpaceReadExcelButton.setToolTip(_translate("MainWindow", "Read dSpace excel file"))
        self.dSpaceReadExcelButton.setText(_translate("MainWindow", "Read dSPACE Excel"))
        self.copyButton.setToolTip(_translate("MainWindow", "Copy Yes/No column"))
        self.copyButton.setText(_translate("MainWindow", "Copy Yes/No"))
        self.exportExcelButton.setToolTip(_translate("MainWindow", "Export to Polarion Excel Format"))
        self.exportExcelButton.setText(_translate("MainWindow", "Copy Yes/No"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "dSPACE"))
        self.polarionRevisionLineEdit.setPlaceholderText(_translate("MainWindow", "Revision number"))
        self.polarionReadExcelButton.setToolTip(_translate("MainWindow", "Read Polarion excel file"))
        self.polarionReadExcelButton.setText(_translate("MainWindow", "Read"))
        self.polarionSaveExcelButton.setToolTip(_translate("MainWindow", "Save polarion excel file"))
        self.polarionSaveExcelButton.setText(_translate("MainWindow", "Save"))
        self.polarionUpdatePassedButton.setToolTip(_translate("MainWindow", "Update excel with Passed verdicts only"))
        self.polarionUpdatePassedButton.setText(_translate("MainWindow", "Update Passed Verdicts Only"))
        self.polarionUpdateAllButton.setToolTip(_translate("MainWindow", "Update excel with All verdicts"))
        self.polarionUpdateAllButton.setText(_translate("MainWindow", "Update All Verdicts"))
        self.polarionUpdateRevisionButton.setToolTip(_translate("MainWindow", "Update excel with current revision number"))
        self.polarionUpdateRevisionButton.setText(_translate("MainWindow", "Revision"))
        self.updateStepsButton.setToolTip(_translate("MainWindow", "Update Polarion server with new steps"))
        self.updateStepsButton.setText(_translate("MainWindow", "Steps"))
        self.updateHyperlinksButton.setToolTip(_translate("MainWindow", "Pull hyperlinks from Polarion server"))
        self.updateHyperlinksButton.setText(_translate("MainWindow", "Hyperlinks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Polarion"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.autorunCheckBox.setText(_translate("MainWindow", "Autorun"))
        self.exitButton.setText(_translate("MainWindow", "Continue"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionConfigFolder.setText(_translate("MainWindow", "Config Folder"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))

import AutomationGUI_rc
