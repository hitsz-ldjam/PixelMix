import sys
from PySide2.QtWidgets import *
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
