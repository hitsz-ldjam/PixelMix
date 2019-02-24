from PySide2.QtCore import *
from PySide2.QtWidgets import *

import Effect

from Ui_BrightnessContrastDialog import Ui_BrightnessContrastDialog


class BrightnessContrastDialog(QDialog, Ui_BrightnessContrastDialog):
    def __init__(self, parent, canvas):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.canvas = canvas
        self.bufMat = self.canvas.mat.copy()

        self.show()

    @Slot(int)
    def on_brightnessSlider_valueChanged(self, brightness):
        self.brightnessSpinBox.setValue(brightness)
        contrast = self.contrastSlider.value() / 400 + 1

        Effect.brightness_contrast(self.bufMat, brightness, contrast, self.canvas.mat)
        self.canvas.update()

    @Slot(int)
    def on_brightnessSpinBox_valueChanged(self, brightness):
        if self.focusWidget() is self.sender():
            self.brightnessSlider.setValue(brightness)

    @Slot(int)
    def on_contrastSlider_valueChanged(self, contrast):
        self.contrastSpinBox.setValue(contrast)
        brightness = self.brightnessSlider.value()
        contrast = contrast / 400 + 1

        Effect.brightness_contrast(self.bufMat, brightness, contrast, self.canvas.mat)
        self.canvas.update()

    @Slot(int)
    def on_contrastSpinBox_valueChanged(self, contrast):
        if self.focusWidget() is self.sender():
            self.contrastSlider.setValue(contrast)

    @Slot(QAbstractButton)
    def on_buttonBox_clicked(self, button):
        if button == self.buttonBox.button(QDialogButtonBox.Apply):
            self.canvas.updated()

            self.accept()

        elif button == self.buttonBox.button(QDialogButtonBox.Discard):
            Effect.brightness_contrast(self.bufMat, 0, 1, self.canvas.mat)
            self.canvas.update()

            self.reject()
