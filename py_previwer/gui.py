import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout, QProgressBar, QMessageBox,
                             QGroupBox)
import previewer
import os

class guiInterface(QWidget):
    """docstring for  guiInterface"""
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(0, 0, 400, 100)
        self.setWindowTitle("Превьювер")
        self.move(650, 490)
        self.grpboxPath = QGroupBox("Выберите объект", self)
        self.grpboxObjectName = QGroupBox("Имя объекта для вывода в pdf", self)
        self.btn = QPushButton('Старт', self)
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
        grid.addWidget(self.prgBar, 1, 0, 1, 2)
        grid.addWidget(self.grpboxPath, 2, 0, 1, 2)
        grid.addWidget(self.grpboxObjectName, 3, 0, 1, 2)
        grid.addWidget(self.btn, 6, 0)
        grid.addWidget(self.qbtn, 6, 1)
        self.setLayout(grid)

        self.show()

    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)
        self.leObjectName.setText(path.split("/")[-1])

    def getObjectName(self):
        path = self.le.text()
        self.leObjectName.setText(path.split("/")[-1])

    def generatePreview(self):
        folder = self.le.text()
        os.chdir(folder)
        previewer.removeOldPdf(self.le.text().split("/")[-1] + ".pdf", folder)
        previewer.createTmpDir()
        self.prgBar.setValue(5)
        psdFl = previewer.searchFl("psd", folder)
        self.prgBar.setValue(10)
        previewer.convertPsd(psdFl, previewer.tmpDir)
        self.prgBar.setValue(60)
        jpgFl = previewer.searchFl("jpeg", previewer.tmpDir)
        self.prgBar.setValue(70)
        dictOfClass = previewer.createDictClass(jpgFl)
        self.prgBar.setValue(80)
        previewer.generatePDF(dictOfClass, self.leObjectName.text())
        self.prgBar.setValue(95)
        previewer.removeTmpDir()
        self.prgBar.setValue(100)
        self.msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())
