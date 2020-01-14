import combinator
import gui
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gInt = gui.guiInterface()
    sys.exit(app.exec_())
