import sys
import PySide2.QtWidgets as QtW
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
