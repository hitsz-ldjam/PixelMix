import PySide2.QtCore as QtC
import PySide2.QtWidgets as QtW
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtW.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi("MainWindow.ui", self)

        qr = self.frameGeometry()
        cp = QtW.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # dock window
        # self.__dockWindow={}
        # self.__dockWindow["Untitled"]

        self.show()

    @QtC.Slot()
    def on_menuFileOpen_triggered(self):
        path = QtW.QFileDialog.getOpenFileName(caption="Open File",
                                               filter="JPEG (*.jpg);;PNG (*.png);;All File Formats (*.*)",
                                               selectedFilter="PNG (*.png)")

    @QtC.Slot()
    def on_menuFileCreate_triggered(self):
        # todo
        print("Create")

    @QtC.Slot()
    def on_menuFileSave_triggered(self):
        # todo
        print("Save")

    @QtC.Slot()
    def on_menuFileSaveAs_triggered(self):
        # todo
        print("SaveAs")

    @QtC.Slot()
    def on_menuFileQuit_triggered(self):
        self.close()

    @QtC.Slot()
    def on_menuHelpAbout_triggered(self):
        dialog = QtW.QDialog(self)
        dialog.setWindowTitle("About")
        dialog.setWindowModality(QtC.Qt.ApplicationModal)
        dialog.show()
        dialog.exec_()
