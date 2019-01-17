import sys
import PyQt5.QtWidgets as QtW
from MainWindow import MainWindow

app = QtW.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
