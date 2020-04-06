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
      

        self.btn = QPushButton('Сформировать', self)
        self.btn.clicked.connect(self.create_template_folder)

        self.rbtn = QPushButton('Обзор', self)
        self.rbtn.clicked.connect(self.getPath)

        self.qbtn = QPushButton('Выход', self)
        self.qbtn.clicked.connect(self.close)

        self.le = QLineEdit(self)
        self.le.setText("E:/work/parallax/catalog/1517")
        self.prgBar = QProgressBar(self)
        self.prgBar.setMaximum(100)        
        
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Готово")

        gridPath = QGridLayout()
        gridPath.addWidget(self.le, 1, 0)
        gridPath.addWidget(self.rbtn, 1, 1)
        self.grpboxPath.setLayout(gridPath)


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.prgBar, 2, 0, 1, 2)
        grid.addWidget(self.grpboxPath, 3, 0, 1, 2)

        grid.addWidget(self.btn, 7, 0)
        grid.addWidget(self.qbtn, 7, 1)
        self.setLayout(grid)

        self.show()

    def getPath(self):
        path = QFileDialog.getExistingDirectory()
        self.le.setText(path)



    def create_template_folder(self):
        combinator.create_html_and_dir(self.le.text())
        self.prgBar.setValue(30)
        os.chdir(self.le.text())
        divlist = combinator.create_list_div()
        self.prgBar.setValue(50)
        combinator.insert_div_in_html(divlist)
        self.prgBar.setValue(100)
        self.msgBox.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    gInt = guiInterface()
    sys.exit(app.exec_())
