#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import xml.etree.ElementTree as ET
from pathlib import Path
from xmlconfig import *
import sys
import os

dialogStyle = 'background-color: rgb(59, 56, 56); color: white;'



class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.debug = True
        self.changesSaved = True

        # set default xml config file path
        self.xmlConfigPath = Path('C:/DSConfig/config.xml')

        # create folder if not exists
        if not os.path.exists(self.xmlConfigPath.parent):
            os.mkdir(self.xmlConfigPath.parent)

        # create config file if not exists
        if not os.path.exists(self.xmlConfigPath):
            root = ET.Element('xmlconfig')
            xmlpath = ET.SubElement(root, 'xmlpath')
            xmlpath.text = str(self.xmlConfigPath)
            tree = ET.ElementTree(root)
            tree.write(self.xmlConfigPath, xml_declaration=True, encoding='utf-8')
                
        # read and parse xml config file if exists
        try:
            self.xmlTree = ET.parse(self.xmlConfigPath)
            self.xmlRoot = self.xmlTree.getroot()
            self.xmlPath = Path(self.xmlRoot.find('xmlpath').text)
            self.pathEdit.setText(str(self.xmlPath))
        except:
            self.statusbar.showMessage('XML config file does not exist')


        # signals and slots for menus, buttons, and edits
        self.pathEdit.textChanged.connect(self.pathChanged)
        self.browseButton.clicked.connect(self.openFileDialog)
        self.actionSave.triggered.connect(self.saveXmlFile)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
        self.exitButton.clicked.connect(self.exit)

    def pathChanged(self):
        self.changesSaved = False
        self.statusbar.showMessage('You have unsaved changes')

    def openFileDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "","XML Files (*.xml);;All Files (*)")
        self.xmlPath = Path(filePath)
        
        if filePath:
            print(filePath)
            self.pathEdit.setText(str(self.xmlPath))
            self.xmlRoot.find('xmlpath').text = filePath

    def saveXmlFile(self):
        self.xmlRoot.find('xmlpath').text = str(Path(self.pathEdit.text()))
        self.xmlTree.write(self.xmlConfigPath, xml_declaration=True, encoding='utf-8')
        self.statusbar.showMessage('Save...OK!')
        self.changesSaved = True

    def exit(self):
        if not self.changesSaved or self.xmlRoot.find('xmlpath').text != self.pathEdit.text():
            msgReply = QMessageBox.question(self, 'Save Changes', 'Would you like to save before exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if msgReply == QMessageBox.Yes:
                self.saveXmlFile()
                print('File saved')
        self.statusbar.showMessage('Exiting')
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
