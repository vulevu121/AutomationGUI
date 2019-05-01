# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutomationGUI_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/graphics/karmalogo_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FFCC80;\n"
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
        self.tabWidget.setStyleSheet("QToolBar {\n"
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
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
        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.generalLayout = QtWidgets.QGridLayout()
        self.generalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.generalLayout.setContentsMargins(0, -1, -1, -1)
        self.generalLayout.setObjectName("generalLayout")
        self.variablePoolLabel = QtWidgets.QLabel(self.tab)
        self.variablePoolLabel.setObjectName("variablePoolLabel")
        self.generalLayout.addWidget(self.variablePoolLabel, 4, 1, 1, 1)
        self.reloadVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_save_alt_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadVariablePoolBtn.setIcon(icon1)
        self.reloadVariablePoolBtn.setFlat(False)
        self.reloadVariablePoolBtn.setObjectName("reloadVariablePoolBtn")
        self.generalLayout.addWidget(self.reloadVariablePoolBtn, 5, 3, 1, 1)
        self.csvReportFolderToolButton = QtWidgets.QToolButton(self.tab)
        self.csvReportFolderToolButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_menu_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.csvReportFolderToolButton.setIcon(icon2)
        self.csvReportFolderToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.csvReportFolderToolButton.setAutoRaise(True)
        self.csvReportFolderToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.csvReportFolderToolButton.setObjectName("csvReportFolderToolButton")
        self.generalLayout.addWidget(self.csvReportFolderToolButton, 1, 4, 1, 1)
        self.callFunctionFolderToolButton = QtWidgets.QToolButton(self.tab)
        self.callFunctionFolderToolButton.setText("")
        self.callFunctionFolderToolButton.setIcon(icon2)
        self.callFunctionFolderToolButton.setObjectName("callFunctionFolderToolButton")
        self.generalLayout.addWidget(self.callFunctionFolderToolButton, 2, 4, 1, 1)
        self.testCaseExcelToolButton = QtWidgets.QToolButton(self.tab)
        self.testCaseExcelToolButton.setText("")
        self.testCaseExcelToolButton.setIcon(icon2)
        self.testCaseExcelToolButton.setObjectName("testCaseExcelToolButton")
        self.generalLayout.addWidget(self.testCaseExcelToolButton, 0, 4, 1, 1)
        self.variablePoolToolButton = QtWidgets.QToolButton(self.tab)
        self.variablePoolToolButton.setText("")
        self.variablePoolToolButton.setIcon(icon2)
        self.variablePoolToolButton.setObjectName("variablePoolToolButton")
        self.generalLayout.addWidget(self.variablePoolToolButton, 4, 4, 1, 1)
        self.testCaseExcelLabel = QtWidgets.QLabel(self.tab)
        self.testCaseExcelLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.testCaseExcelLabel.setObjectName("testCaseExcelLabel")
        self.generalLayout.addWidget(self.testCaseExcelLabel, 0, 1, 1, 1)
        self.testCaseExcelEdit = QtWidgets.QLineEdit(self.tab)
        self.testCaseExcelEdit.setObjectName("testCaseExcelEdit")
        self.generalLayout.addWidget(self.testCaseExcelEdit, 0, 2, 1, 1)
        self.csvReportLabel = QtWidgets.QLabel(self.tab)
        self.csvReportLabel.setObjectName("csvReportLabel")
        self.generalLayout.addWidget(self.csvReportLabel, 1, 1, 1, 1)
        self.callFunctionEdit = QtWidgets.QLineEdit(self.tab)
        self.callFunctionEdit.setObjectName("callFunctionEdit")
        self.generalLayout.addWidget(self.callFunctionEdit, 2, 2, 1, 1)
        self.variablePoolEdit = QtWidgets.QLineEdit(self.tab)
        self.variablePoolEdit.setObjectName("variablePoolEdit")
        self.generalLayout.addWidget(self.variablePoolEdit, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("image: url(:/icon/graphics/baseline_folder_black_24dp.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.generalLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.browseCallFunctionBtn = QtWidgets.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_folder_open_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseCallFunctionBtn.setIcon(icon3)
        self.browseCallFunctionBtn.setObjectName("browseCallFunctionBtn")
        self.generalLayout.addWidget(self.browseCallFunctionBtn, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("image: url(:/icon/graphics/baseline_file_copy_black_24dp.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.generalLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.csvReportEdit = QtWidgets.QLineEdit(self.tab)
        self.csvReportEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.csvReportEdit.setClearButtonEnabled(False)
        self.csvReportEdit.setObjectName("csvReportEdit")
        self.generalLayout.addWidget(self.csvReportEdit, 1, 2, 1, 1)
        self.browseVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        self.browseVariablePoolBtn.setIcon(icon3)
        self.browseVariablePoolBtn.setObjectName("browseVariablePoolBtn")
        self.generalLayout.addWidget(self.browseVariablePoolBtn, 4, 3, 1, 1)
        self.callFunctionLabel = QtWidgets.QLabel(self.tab)
        self.callFunctionLabel.setObjectName("callFunctionLabel")
        self.generalLayout.addWidget(self.callFunctionLabel, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("image: url(:/icon/graphics/baseline_folder_black_24dp.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.generalLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.browseCsvReportBtn = QtWidgets.QPushButton(self.tab)
        self.browseCsvReportBtn.setIcon(icon3)
        self.browseCsvReportBtn.setObjectName("browseCsvReportBtn")
        self.generalLayout.addWidget(self.browseCsvReportBtn, 1, 3, 1, 1)
        self.browseTestCaseExcelBtn = QtWidgets.QPushButton(self.tab)
        self.browseTestCaseExcelBtn.setIcon(icon3)
        self.browseTestCaseExcelBtn.setObjectName("browseTestCaseExcelBtn")
        self.generalLayout.addWidget(self.browseTestCaseExcelBtn, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("image: url(:/icon/graphics/excel_24dp.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.generalLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.generalLayout, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_tab_unselected_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("graphics/baseline_tab_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")
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
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.loggingTabLayout.addWidget(self.addSignalGroupBox)
        self.horizontalLayout_3.addLayout(self.loggingTabLayout)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_tab_unselected_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_tab_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon5, "")
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
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.dtcTabLayout.addWidget(self.dtcExGroupBox)
        self.horizontalLayout_11.addLayout(self.dtcTabLayout)
        self.tabWidget.addTab(self.tab_3, icon5, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.runEdit = QtWidgets.QPlainTextEdit(self.tab_5)
        self.runEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.runEdit.setObjectName("runEdit")
        self.horizontalLayout_5.addWidget(self.runEdit)
        self.runYesNoEdit = QtWidgets.QPlainTextEdit(self.tab_5)
        self.runYesNoEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.runYesNoEdit.setObjectName("runYesNoEdit")
        self.horizontalLayout_5.addWidget(self.runYesNoEdit)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.copyButton = QtWidgets.QPushButton(self.tab_5)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout_9.addWidget(self.copyButton)
        self.processRunListButton = QtWidgets.QPushButton(self.tab_5)
        self.processRunListButton.setObjectName("processRunListButton")
        self.verticalLayout_9.addWidget(self.processRunListButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.settingsVerticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.settingsVerticalLayoutLeft.setObjectName("settingsVerticalLayoutLeft")
        self.autorunHorizontalLayout = QtWidgets.QHBoxLayout()
        self.autorunHorizontalLayout.setObjectName("autorunHorizontalLayout")
        self.autorunLabel = QtWidgets.QLabel(self.groupBox_2)
        self.autorunLabel.setObjectName("autorunLabel")
        self.autorunHorizontalLayout.addWidget(self.autorunLabel)
        self.autorunSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autorunSpinBox.sizePolicy().hasHeightForWidth())
        self.autorunSpinBox.setSizePolicy(sizePolicy)
        self.autorunSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.autorunSpinBox.setObjectName("autorunSpinBox")
        self.autorunHorizontalLayout.addWidget(self.autorunSpinBox)
        self.settingsVerticalLayoutLeft.addLayout(self.autorunHorizontalLayout)
        self.verticalLayout_8.addLayout(self.settingsVerticalLayoutLeft)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
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
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_4, icon5, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.bottombuttonsLayout = QtWidgets.QHBoxLayout()
        self.bottombuttonsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.bottombuttonsLayout.setContentsMargins(0, -1, -1, -1)
        self.bottombuttonsLayout.setObjectName("bottombuttonsLayout")
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_exit_to_app_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon6)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/png/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon7)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/png/icons/contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConfigFolder = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/svg/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigFolder.setIcon(icon9)
        self.actionConfigFolder.setObjectName("actionConfigFolder")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setIcon(icon9)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIcon(icon7)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/svg/icons/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon10)
        self.actionNew.setObjectName("actionNew")
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionConfigFolder)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionAbout)
        self.variablePoolLabel.setBuddy(self.variablePoolEdit)
        self.testCaseExcelLabel.setBuddy(self.testCaseExcelEdit)
        self.csvReportLabel.setBuddy(self.csvReportEdit)
        self.callFunctionLabel.setBuddy(self.callFunctionEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.exitButton.clicked.connect(self.actionExit.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.testCaseExcelEdit, self.browseTestCaseExcelBtn)
        MainWindow.setTabOrder(self.browseTestCaseExcelBtn, self.csvReportEdit)
        MainWindow.setTabOrder(self.csvReportEdit, self.browseCsvReportBtn)
        MainWindow.setTabOrder(self.browseCsvReportBtn, self.callFunctionEdit)
        MainWindow.setTabOrder(self.callFunctionEdit, self.browseCallFunctionBtn)
        MainWindow.setTabOrder(self.browseCallFunctionBtn, self.variablePoolEdit)
        MainWindow.setTabOrder(self.variablePoolEdit, self.browseVariablePoolBtn)
        MainWindow.setTabOrder(self.browseVariablePoolBtn, self.reloadVariablePoolBtn)
        MainWindow.setTabOrder(self.reloadVariablePoolBtn, self.exitButton)
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
        MainWindow.setTabOrder(self.removeDtcExBtn, self.autorunSpinBox)
        MainWindow.setTabOrder(self.autorunSpinBox, self.updateVariablePoolCheckBox)
        MainWindow.setTabOrder(self.updateVariablePoolCheckBox, self.showDebugCheckBox)
        MainWindow.setTabOrder(self.showDebugCheckBox, self.autorunCheckBox)
        MainWindow.setTabOrder(self.autorunCheckBox, self.testCaseExcelToolButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Runtime Options"))
        self.dtcExCheckBox.setText(_translate("MainWindow", "Enable DTC Exception(s)"))
        self.callFunctionDebugCheckbox.setText(_translate("MainWindow", "Debug Call Functions"))
        self.versionCheckBox.setText(_translate("MainWindow", "Include HW && SW Version"))
        self.variablePoolLabel.setText(_translate("MainWindow", "VariablePool File:"))
        self.reloadVariablePoolBtn.setToolTip(_translate("MainWindow", "Load Variable Pool"))
        self.reloadVariablePoolBtn.setText(_translate("MainWindow", "Load VP"))
        self.csvReportFolderToolButton.setText(_translate("MainWindow", "..."))
        self.callFunctionFolderToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.testCaseExcelToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.variablePoolToolButton.setToolTip(_translate("MainWindow", "Open Folder + File"))
        self.testCaseExcelLabel.setText(_translate("MainWindow", "<html><head/><body><p>Test Case Excel File</p></body></html>"))
        self.testCaseExcelEdit.setPlaceholderText(_translate("MainWindow", "Specify test case excel file"))
        self.csvReportLabel.setText(_translate("MainWindow", "CSV Report Folder:"))
        self.callFunctionEdit.setPlaceholderText(_translate("MainWindow", "Specify the call function folder"))
        self.variablePoolEdit.setPlaceholderText(_translate("MainWindow", "Specify the variable pool text file"))
        self.browseCallFunctionBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCallFunctionBtn.setText(_translate("MainWindow", "Browse"))
        self.csvReportEdit.setPlaceholderText(_translate("MainWindow", "Specify the CSV report folder"))
        self.browseVariablePoolBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseVariablePoolBtn.setText(_translate("MainWindow", "Browse"))
        self.callFunctionLabel.setText(_translate("MainWindow", "Call Function Folder:"))
        self.browseCsvReportBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCsvReportBtn.setText(_translate("MainWindow", "Browse"))
        self.browseTestCaseExcelBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseTestCaseExcelBtn.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
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
        self.runEdit.setPlaceholderText(_translate("MainWindow", "List of test cases from excel file..."))
        self.runYesNoEdit.setPlaceholderText(_translate("MainWindow", "List of failed test cases to rerun..."))
        self.copyButton.setText(_translate("MainWindow", "Copy"))
        self.processRunListButton.setText(_translate("MainWindow", "Process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Run"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parameters"))
        self.autorunLabel.setText(_translate("MainWindow", "Autorun Timer (sec)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Options"))
        self.updateVariablePoolCheckBox.setText(_translate("MainWindow", "Update VariablePool in AutomationDesk"))
        self.showDebugCheckBox.setText(_translate("MainWindow", "Show Debug Messages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Settings"))
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
