import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                             QLineEdit, QGridLayout)
import previewer


class guiInterface(QWidget):
    """docstring for  guiInterface"""
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.btn = QPushButton('Старт', self)
        self.rbtn = QPushButton('Обзор', self)
        self.qbtn = QPushButton('Выход', self)
        self.le = QLineEdit(self)
        self.rbtn.clicked.connect(self.getPath)
        self.qbtn.clicked.connect(self.close)
        self.btn.clicked.connect(self.generatePreview)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.le, 1, 0)
        grid.addWidget(self.rbtn, 1, 1)
        grid.addWidget(self.btn, 2, 0)
        grid.addWidget(self.qbtn, 2, 1)
        self.setLayout(grid)
        self.setWindowTitle('Превьювер')
        self.show()

    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)

    def generatePreview(self):
        previewer.pyMain(self.le.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())
