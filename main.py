import sys
from PySide2.QtWidgets import *
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("resources/qdarkstyle/style.qss", "r", encoding="utf-8") as style:
        import resources.qdarkstyle.pyside2_style_rc
        app.setStyleSheet(style.read())

    mainWindow = MainWindow()
    sys.exit(app.exec_())
