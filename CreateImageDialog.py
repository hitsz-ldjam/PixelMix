from PySide2.QtCore import *
from PySide2.QtWidgets import *

from Ui_CreateImageDialog import Ui_CreateImageDialog


class CreateImageDialog(QDialog, Ui_CreateImageDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        self.show()

    @Slot(QAbstractButton)
    def on_buttonBox_clicked(self, button):
        if self.buttonBox.button(QDialogButtonBox.Ok) == button:
            if len(self.fileNameLine.text()) == 0:
                QMessageBox.warning(self,
                                    self.tr("Warning"),
                                    self.tr("File name is empty!"),
                                    QMessageBox.Yes)
            else:
                self.accept()

        if self.buttonBox.button(QDialogButtonBox.Cancel) == button:
            self.reject()

    @staticmethod
    def getImageInfo(parent):
        dialog = CreateImageDialog(parent)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.fileNameLine.text(), dialog.widthBox.value(), dialog.heightBox.value()
        else:
            return "", -1, -1
