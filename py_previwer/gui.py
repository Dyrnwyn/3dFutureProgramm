import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout, QProgressBar, QMessageBox)
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
        self.btn = QPushButton('Старт', self)
        self.rbtn = QPushButton('Обзор', self)
        self.qbtn = QPushButton('Выход', self)
        self.le = QLineEdit(self)
        self.prgBar = QProgressBar(self)
        self.prgBar.setMaximum(100)
        self.rbtn.clicked.connect(self.getPath)
        self.qbtn.clicked.connect(self.close)
        self.btn.clicked.connect(self.generatePreview)
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Готово")

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.prgBar, 1, 0, 1, 2)
        grid.addWidget(self.le, 2, 0)
        grid.addWidget(self.rbtn, 2, 1)
        grid.addWidget(self.btn, 3, 0)
        grid.addWidget(self.qbtn, 3, 1)
        self.setLayout(grid)
        self.setWindowTitle('Превьювер')
        self.show()

    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)

    def generatePreview(self):
        #previewer.pyMain(self.le.text())
        folder = self.le.text()
        os.chdir(folder)
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
        previewer.generatePDF(dictOfClass)
        self.prgBar.setValue(95)
        previewer.removeTmpDir()
        self.prgBar.setValue(100)
        self.msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())
