import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout, QProgressBar, QMessageBox,
                             QGroupBox, QMenuBar)
import os
import combinator


class guiInterface(QWidget):

    """docstring for  guiInterface"""
    def __init__(self):
        super().__init__()
        self.initUi()
        

    def initUi(self):
        
        self.setGeometry(0, 0, 400, 100)
        self.setWindowTitle("Вырезка элемента")
        self.move(650, 490)

        self.grpboxPath = QGroupBox("Выберите объект", self)
        self.grpboxObjectName = QGroupBox("Cюда не смотрим, вообще, просто тыкаем на кнопки", self)

        self.btn = QPushButton('Начать', self)
        self.rbtn = QPushButton('Обзор', self)
        self.qbtn = QPushButton('Выход', self)
        self.le = QLineEdit(self)
        self.leObjectName = QLineEdit(self)
        self.prgBar = QProgressBar(self)
        self.prgBar.setMaximum(100)
        self.rbtn.clicked.connect(self.getPath)
        self.qbtn.clicked.connect(self.close)
        self.btn.clicked.connect(self.generatePreview)
        self.le.textChanged.connect(self.getObjectName)
        self.msgBox = QMessageBox(self)
        

        gridPath = QGridLayout()
        gridPath.addWidget(self.le, 1, 0)
        gridPath.addWidget(self.rbtn, 1, 1)
        self.grpboxPath.setLayout(gridPath)

        gridObjectName = QGridLayout()
        gridObjectName.addWidget(self.leObjectName, 2, 0)
        self.grpboxObjectName.setLayout(gridObjectName)

        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.prgBar, 2, 0, 1, 2)
        grid.addWidget(self.grpboxPath, 3, 0, 1, 2)
        grid.addWidget(self.grpboxObjectName, 4, 0, 1, 2)
        grid.addWidget(self.btn, 7, 0)
        grid.addWidget(self.qbtn, 7, 1)
        self.setLayout(grid)

        self.show()

    def setTextMsg(self):
        self.msgBox.setText("Количество шаблонов с вырезкой: " + str(combinator.count))
        combinator.count = 0


    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)
        self.leObjectName.setText(path.split("/")[-1])

    def getObjectName(self):
        path = self.le.text()
        self.leObjectName.setText(path.split("\\")[-1])

    def generatePreview(self):
        folder = self.le.text()
        os.chdir(folder)
        #combinator.createCupDir()        
        self.prgBar.setValue(5)
        psdFl = combinator.searchFl("psd", folder)
        self.prgBar.setValue(10)
        
        count = combinator.findCutTemplate(psdFl)
        self.setTextMsg()
        self.prgBar.setValue(15)
        # combinator.convertPsd(cupFl, combinator.cup_dir)
        # self.prgBar.setValue(60)
        # pngCupFl = combinator.searchFl("png", combinator.cup_dir)
        # self.prgBar.setValue(70)
        # dictOfClass = combinator.createDictClass(pngCupFl)
        # self.prgBar.setValue(80)
        # combinator.generatePngForPrint(dictOfClass, self.leObjectName.text())
        # self.prgBar.setValue(95)
        # combinator.delOldPng(pngCupFl)
        self.prgBar.setValue(100)
        self.msgBox.exec_()
