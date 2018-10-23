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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/graphics/karmalogo_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.generalLayout = QtWidgets.QGridLayout()
        self.generalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.generalLayout.setContentsMargins(0, -1, -1, -1)
        self.generalLayout.setObjectName("generalLayout")
        self.browseVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_folder_open_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseVariablePoolBtn.setIcon(icon1)
        self.browseVariablePoolBtn.setObjectName("browseVariablePoolBtn")
        self.generalLayout.addWidget(self.browseVariablePoolBtn, 2, 2, 1, 1)
        self.variablePoolEdit = QtWidgets.QLineEdit(self.tab)
        self.variablePoolEdit.setObjectName("variablePoolEdit")
        self.generalLayout.addWidget(self.variablePoolEdit, 2, 1, 1, 1)
        self.variablePoolLabel = QtWidgets.QLabel(self.tab)
        self.variablePoolLabel.setObjectName("variablePoolLabel")
        self.generalLayout.addWidget(self.variablePoolLabel, 2, 0, 1, 1)
        self.callFunctionLabel = QtWidgets.QLabel(self.tab)
        self.callFunctionLabel.setObjectName("callFunctionLabel")
        self.generalLayout.addWidget(self.callFunctionLabel, 0, 0, 1, 1)
        self.csvReportLabel = QtWidgets.QLabel(self.tab)
        self.csvReportLabel.setObjectName("csvReportLabel")
        self.generalLayout.addWidget(self.csvReportLabel, 1, 0, 1, 1)
        self.browseCallFunctionBtn = QtWidgets.QPushButton(self.tab)
        self.browseCallFunctionBtn.setIcon(icon1)
        self.browseCallFunctionBtn.setObjectName("browseCallFunctionBtn")
        self.generalLayout.addWidget(self.browseCallFunctionBtn, 0, 2, 1, 1)
        self.callFunctionEdit = QtWidgets.QLineEdit(self.tab)
        self.callFunctionEdit.setObjectName("callFunctionEdit")
        self.generalLayout.addWidget(self.callFunctionEdit, 0, 1, 1, 1)
        self.csvReportEdit = QtWidgets.QLineEdit(self.tab)
        self.csvReportEdit.setObjectName("csvReportEdit")
        self.generalLayout.addWidget(self.csvReportEdit, 1, 1, 1, 1)
        self.browseCsvReportBtn = QtWidgets.QPushButton(self.tab)
        self.browseCsvReportBtn.setIcon(icon1)
        self.browseCsvReportBtn.setObjectName("browseCsvReportBtn")
        self.generalLayout.addWidget(self.browseCsvReportBtn, 1, 2, 1, 1)
        self.openCallFunctionFolderButton = QtWidgets.QPushButton(self.tab)
        self.openCallFunctionFolderButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_open_in_browser_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openCallFunctionFolderButton.setIcon(icon2)
        self.openCallFunctionFolderButton.setObjectName("openCallFunctionFolderButton")
        self.generalLayout.addWidget(self.openCallFunctionFolderButton, 0, 3, 1, 1)
        self.openVarPoolFolderButton = QtWidgets.QPushButton(self.tab)
        self.openVarPoolFolderButton.setText("")
        self.openVarPoolFolderButton.setIcon(icon2)
        self.openVarPoolFolderButton.setObjectName("openVarPoolFolderButton")
        self.generalLayout.addWidget(self.openVarPoolFolderButton, 2, 3, 1, 1)
        self.openCsvReportFolderButton = QtWidgets.QPushButton(self.tab)
        self.openCsvReportFolderButton.setText("")
        self.openCsvReportFolderButton.setIcon(icon2)
        self.openCsvReportFolderButton.setObjectName("openCsvReportFolderButton")
        self.generalLayout.addWidget(self.openCsvReportFolderButton, 1, 3, 1, 1)
        self.reloadVariablePoolBtn = QtWidgets.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_save_alt_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadVariablePoolBtn.setIcon(icon3)
        self.reloadVariablePoolBtn.setFlat(False)
        self.reloadVariablePoolBtn.setObjectName("reloadVariablePoolBtn")
        self.generalLayout.addWidget(self.reloadVariablePoolBtn, 3, 2, 1, 1)
        self.versionCheckBox = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionCheckBox.sizePolicy().hasHeightForWidth())
        self.versionCheckBox.setSizePolicy(sizePolicy)
        self.versionCheckBox.setObjectName("versionCheckBox")
        self.generalLayout.addWidget(self.versionCheckBox, 3, 1, 1, 1)
        self.fullMessagesCheckbox = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullMessagesCheckbox.sizePolicy().hasHeightForWidth())
        self.fullMessagesCheckbox.setSizePolicy(sizePolicy)
        self.fullMessagesCheckbox.setObjectName("fullMessagesCheckbox")
        self.generalLayout.addWidget(self.fullMessagesCheckbox, 4, 1, 1, 1)
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
        self.dtcExCheckBox = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtcExCheckBox.sizePolicy().hasHeightForWidth())
        self.dtcExCheckBox.setSizePolicy(sizePolicy)
        self.dtcExCheckBox.setObjectName("dtcExCheckBox")
        self.dtcTabLayout.addWidget(self.dtcExCheckBox)
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
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.bottombuttonsLayout = QtWidgets.QHBoxLayout()
        self.bottombuttonsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.bottombuttonsLayout.setContentsMargins(0, -1, -1, -1)
        self.bottombuttonsLayout.setObjectName("bottombuttonsLayout")
        self.saveAsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsBtn.sizePolicy().hasHeightForWidth())
        self.saveAsBtn.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_save_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAsBtn.setIcon(icon6)
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.bottombuttonsLayout.addWidget(self.saveAsBtn)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setIcon(icon6)
        self.saveBtn.setFlat(False)
        self.saveBtn.setObjectName("saveBtn")
        self.bottombuttonsLayout.addWidget(self.saveBtn)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_exit_to_app_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon7)
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")
        self.bottombuttonsLayout.addWidget(self.exitButton)
        self.verticalLayout_3.addLayout(self.bottombuttonsLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 40))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuOptions.sizePolicy().hasHeightForWidth())
        self.menuOptions.setSizePolicy(sizePolicy)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_info_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpenConfigFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenConfigFolder.setIcon(icon2)
        self.actionOpenConfigFolder.setObjectName("actionOpenConfigFolder")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setIcon(icon1)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIcon(icon6)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/graphics/baseline_file_copy_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon9)
        self.actionNew.setObjectName("actionNew")
        self.actionShow_Debug_Messages = QtWidgets.QAction(MainWindow)
        self.actionShow_Debug_Messages.setCheckable(True)
        self.actionShow_Debug_Messages.setObjectName("actionShow_Debug_Messages")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpenConfigFolder)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionShow_Debug_Messages)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.exitButton.clicked.connect(self.actionExit.trigger)
        self.saveBtn.clicked.connect(self.actionSave.trigger)
        self.saveAsBtn.clicked.connect(self.actionSaveAs.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseVariablePoolBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseVariablePoolBtn.setText(_translate("MainWindow", "Open"))
        self.variablePoolLabel.setText(_translate("MainWindow", "VariablePool CSV File:"))
        self.callFunctionLabel.setText(_translate("MainWindow", "Call Function Folder:"))
        self.csvReportLabel.setText(_translate("MainWindow", "CSV Report Folder:"))
        self.browseCallFunctionBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCallFunctionBtn.setText(_translate("MainWindow", "Open"))
        self.browseCsvReportBtn.setToolTip(_translate("MainWindow", "Browse"))
        self.browseCsvReportBtn.setText(_translate("MainWindow", "Open"))
        self.openCallFunctionFolderButton.setToolTip(_translate("MainWindow", "Open Folder"))
        self.openVarPoolFolderButton.setToolTip(_translate("MainWindow", "Open Folder"))
        self.openCsvReportFolderButton.setToolTip(_translate("MainWindow", "Open Folder"))
        self.reloadVariablePoolBtn.setToolTip(_translate("MainWindow", "Load Variable Pool"))
        self.reloadVariablePoolBtn.setText(_translate("MainWindow", "Load VP"))
        self.versionCheckBox.setText(_translate("MainWindow", "Include HW && SW Version"))
        self.fullMessagesCheckbox.setText(_translate("MainWindow", "Show Full Call Function Messages"))
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
        self.dtcExCheckBox.setText(_translate("MainWindow", "Enable DTC Exception"))
        self.dtcExGroupBox.setTitle(_translate("MainWindow", "DTC Exception List"))
        self.addDtcExBtn.setText(_translate("MainWindow", "Add"))
        self.removeDtcExBtn.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "DTC"))
        self.saveAsBtn.setText(_translate("MainWindow", "Save As"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.exitButton.setText(_translate("MainWindow", "Continue"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpenConfigFolder.setText(_translate("MainWindow", "Open Config Folder"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionShow_Debug_Messages.setText(_translate("MainWindow", "Show Debug Messages"))

import xmlconfig_rc
