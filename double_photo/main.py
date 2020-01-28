import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout, QProgressBar, QMessageBox,
                             QGroupBox, QMenuBar)
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
        self.grpboxObjectName = QGroupBox("Имя объекта для вывода в pdf", self)

        self.btn = QPushButton('Компоновка', self)
        self.rbtn = QPushButton('Обзор', self)
        self.qbtn = QPushButton('Разрезать', self)
        self.le = QLineEdit(self)
        self.leObjectName = QLineEdit(self)
        self.prgBar = QProgressBar(self)
        self.prgBar.setMaximum(100)
        self.rbtn.clicked.connect(self.getPath)
        self.qbtn.clicked.connect(self.cropImg)
        self.btn.clicked.connect(self.generatePreview)
        self.le.textChanged.connect(self.getObjectName)
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Готово")

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
        self.prgBar.setValue(5)
        jpgFl = combinator.searchFl("jpg", folder)
        self.prgBar.setValue(10)
        photoH,photoV = combinator.listHVPhoto(jpgFl)
        combinator.createFileForRemoveBGH(photoH)
        self.prgBar.setValue(50)
        combinator.createFileForRemoveBGV(photoV)
        self.prgBar.setValue(100)
        self.msgBox.exec_()

    def cropImg(self):
        folder = self.le.text()
        os.chdir(folder)
        self.prgBar.setValue(5)
        jpgFl = combinator.searchFl("png", folder)
        self.prgBar.setValue(10)
        photoH,photoV = combinator.listHVPhotoForCrop(jpgFl)
        self.prgBar.setValue(20)
        combinator.cropImage(photoH, photoV)
        self.prgBar.setValue(100)
        self.msgBox.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())
