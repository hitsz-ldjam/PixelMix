# -*- coding: utf-8 -*-

import PyQt5.QtCore as QtC
import PyQt5.QtWidgets as QtW
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtW.QMainWindow):
    def __init__(self, title="Pixel Mix"):
        super().__init__()
        super().setWindowTitle(title)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        # dock window
        self.__dockWindow={}
        self.__dockWindow["Untitled"]


    @QtC.pyqtSlot()
    def on_menuFileOpen_triggered(self):
        path = QtW.QFileDialog.getOpenFileName(self, "打开文件",
                                               filter="JPEG Files(*.jpg);;PNG Files(*.png)",
                                               initialFilter="JPEG Files(*jpg)")

    @QtC.pyqtSlot()
    def on_menuFileCreate_triggered(self):
        # todo
        print("Create")

    @QtC.pyqtSlot()
    def on_menuFileSave_triggered(self):
        # todo
        print("Save")

    @QtC.pyqtSlot()
    def on_menuFileSaveAs_triggered(self):
        # todo
        print("SaveAs")

    @QtC.pyqtSlot()
    def on_menuHelpAbout_triggered(self):
        dialog = QtW.QDialog(self)
        dialog.setWindowTitle("关于")
        dialog.setWindowModality(QtC.Qt.ApplicationModal)
        dialog.show()
        dialog.exec_()
