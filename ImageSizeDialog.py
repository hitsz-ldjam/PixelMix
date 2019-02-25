from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from Canvas import Canvas

from Ui_ImageSizeDialog import Ui_ImageSize


class ImageSizeDialog(QDialog, Ui_ImageSize):
    def __init__(self, parent: QWidget, canvas):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.canvas = canvas

        # store width and height of the canvas
        self.imageOriginalWidth = self.canvas.image.width()
        self.imageOriginalHeight = self.canvas.image.height()

        # set original size label
        self.originalSizeLabel.setText("Original Size: "
                                       + str(self.imageOriginalWidth)
                                       + " * "
                                       + str(self.imageOriginalHeight))

        # store aspect radio (width / height)
        self.aspect = self.imageOriginalWidth / self.imageOriginalHeight

        # set initial value
        self.widthSpinBox.setValue(canvas.image.width())
        self.heightSpinBox.setValue(canvas.image.height())

        self.show()

    @Slot(int)
    def on_widthSpinBox_valueChanged(self, value):
        if self.focusWidget() == self.sender():
            if self.lockAspect.isChecked():
                self.heightSpinBox.setValue(value / self.aspect)

    @Slot(int)
    def on_heightSpinBox_valueChanged(self, value):
        if self.focusWidget() == self.sender():
            if self.lockAspect.isChecked():
                self.widthSpinBox.setValue(value * self.aspect)

    @Slot(bool)
    def on_lockAspect_toggled(self, checked):
        if checked:
            self.widthSpinBox.setValue(self.imageOriginalWidth)
            self.heightSpinBox.setValue(self.imageOriginalHeight)

    @Slot(QAbstractButton)
    def on_buttonBox_clicked(self, button):
        if button == self.buttonBox.button(QDialogButtonBox.Apply):
            self.canvas.resizeImage(self.widthSpinBox.value(),
                                    self.heightSpinBox.value())
            self.canvas.updated()
            self.accept()

        elif button == self.buttonBox.button(QDialogButtonBox.Discard):

            self.reject()
