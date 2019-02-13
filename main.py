import sys
from PySide2.QtWidgets import *
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("resources/style.qss", "r", encoding="utf-8") as style:
        app.setStyleSheet(style.read())

    mainWindow = MainWindow()
    sys.exit(app.exec_())
