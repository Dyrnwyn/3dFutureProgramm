import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout, QProgressBar, QMessageBox,
                             QGroupBox, QMenuBar, QCheckBox)
import combinator
import os


# 11
class guiInterface(QWidget):
    """docstring for  guiInterface"""

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(0, 0, 400, 100)
        self.setWindowTitle("Комбинатор фото")
        self.move(650, 490)

        self.grpboxPath = QGroupBox("Выберите объект", self)
        self.grpboxObjectName = QGroupBox("Выберите размер для компоновки", self)

        self.btn = QPushButton('Компоновка', self)
        self.rbtn = QPushButton('Обзор', self)
        self.qbtn = QPushButton('Выход', self)
        self.sbtn = QPushButton('Сортировка', self)

        self.opt10 = QCheckBox('10x15')
        self.opt15 = QCheckBox('15x20')
        self.opt20 = QCheckBox('20x30')

        self.le = QLineEdit(self)
        self.prgBar = QProgressBar(self)
        self.prgBar.setMaximum(100)
        self.rbtn.clicked.connect(self.getPath)
        self.qbtn.clicked.connect(self.close)
        self.btn.clicked.connect(self.generatePreview)
        self.sbtn.clicked.connect(self.sortphoto)
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Готово")
        self.allertBox = QMessageBox(self)
        

        gridPath = QGridLayout()
        gridPath.addWidget(self.le, 1, 0)
        gridPath.addWidget(self.rbtn, 1, 1)
        self.grpboxPath.setLayout(gridPath)

        gridObjectName = QGridLayout()
        gridObjectName.addWidget(self.opt10, 1, 0)
        gridObjectName.addWidget(self.opt15, 1, 1)
        gridObjectName.addWidget(self.opt20, 1, 2)
        self.grpboxObjectName.setLayout(gridObjectName)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.prgBar, 2, 0, 1, 3)
        grid.addWidget(self.grpboxPath, 3, 0, 1, 3)
        grid.addWidget(self.grpboxObjectName, 4, 0, 1, 3)
        grid.addWidget(self.btn, 7, 1)
        grid.addWidget(self.sbtn, 7, 0)
        grid.addWidget(self.qbtn, 7, 2)
        self.setLayout(grid)

        self.show()

    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)

    def getObjectName(self):
        path = self.le.text()
        self.leObjectName.setText(path.split("\\")[-1])

    def generatePreview(self):
        """Функция комбинирования фотографий"""
        folder = self.le.text()
        try:
            os.chdir(folder)
            self.prgBar.setValue(5)
            txtFl = combinator.searchFl("txt", folder)
            self.prgBar.setValue(10)
            size10, size15, size20 = combinator.createListsOfPhotoFile(txtFl)
            self.prgBar.setValue(25)
            if self.opt10.checkState():
                combinator.pagesize10(size10, '10x15')
            self.prgBar.setValue(50)
            if self.opt15.checkState():
                combinator.pagesize15(size15, '15x20')
            self.prgBar.setValue(75)
            if self.opt20.checkState():
                combinator.pagesize20(size20, '20x30')
            self.prgBar.setValue(100)
            self.msgBox.exec_()
        except OSError:
            self.allertBox.setText("Выберите обьект")
            self.allertBox.exec_()
        except IndexError:
            self.allertBox.setText("Нет выгруженного файла")
            self.allertBox.exec_()
            self.prgBar.setValue(0)


    def sortphoto(self):
        """Функция сортировки фотографий"""
        folder = self.le.text()
        try:
            os.chdir(folder)
            self.prgBar.setValue(5)
            txtFl = combinator.searchFl("txt", folder)
            self.prgBar.setValue(10)
            size10, size15, size20 = combinator.createListsOfPhotoFile(txtFl)
            self.prgBar.setValue(25)
            combinator.sortphoto10(size10, '10x15')
            self.prgBar.setValue(50)
            combinator.sortphoto15(size15, '15x20')
            self.prgBar.setValue(75)
            combinator.sortphoto20(size20, '20x30')
            self.prgBar.setValue(100)
            self.msgBox.exec_()
        except FileExistsError:
            self.allertBox.setText("Удали папки")
            self.allertBox.exec_()
            self.prgBar.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())