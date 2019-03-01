from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from Canvas import Canvas
from CvQtBridge import CvQtBridge

from Ui_CanvasSizeDialog import Ui_CanvasSizeDialog


class CanvasSizeDialog(QDialog, Ui_CanvasSizeDialog):
    def __init__(self, parent: QWidget, canvas: Canvas):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.canvas = canvas

        # todo try to draw rect on image
        self.painter = QPainter()

        # store width and height of the canvas
        self.imageOriginalWidth = self.canvas.image.width()
        self.imageOriginalHeight = self.canvas.image.height()

        # set original size label
        self.originalSizeLabel.setText("Original Size: "
                                       + str(self.imageOriginalWidth)
                                       + " * "
                                       + str(self.imageOriginalHeight))

        # set initial value for spin boxes
        self.xSpinBox.setMaximum(self.imageOriginalWidth - 1)
        self.ySpinBox.setMaximum(self.imageOriginalHeight - 1)

        self.xSpinBox.setValue(0)
        self.ySpinBox.setValue(0)

        self.widthSpinBox.setMaximum(self.imageOriginalWidth)
        self.heightSpinBox.setMaximum(self.imageOriginalHeight)

        self.widthSpinBox.setValue(self.imageOriginalWidth)
        self.heightSpinBox.setValue(self.imageOriginalHeight)

        self.show()

    @Slot(int)
    def on_xSpinBox_valueChanged(self, value):
        self.widthSpinBox.setMaximum(self.imageOriginalWidth - value)
        self.updateScissorRect()

    @Slot(int)
    def on_ySpinBox_valueChanged(self, value):
        self.heightSpinBox.setMaximum(self.imageOriginalHeight - value)
        self.updateScissorRect()
        pass

    @Slot(int)
    def on_widthSpinBox_valueChanged(self, value):
        self.updateScissorRect()
        pass

    @Slot(int)
    def on_heightSpinBox_valueChanged(self, value):
        self.updateScissorRect()
        pass

    @Slot(QAbstractButton)
    def on_buttonBox_clicked(self, button):
        self.canvas.endDraw()
        if button == self.buttonBox.button(QDialogButtonBox.Apply):
            self.canvas.image = self.canvas.image.copy(self.xSpinBox.value(),
                                                       self.ySpinBox.value(),
                                                       self.widthSpinBox.value(),
                                                       self.heightSpinBox.value())
            self.canvas.mat = CvQtBridge.qImageToSharedMat(self.canvas.image)
            self.canvas.copyImageToTempImage()
            self.canvas.frame.resize(self.canvas.image.width(), self.canvas.image.height())
            self.accept()

        elif button == self.buttonBox.button(QDialogButtonBox.Discard):
            self.reject()

    def updateScissorRect(self):
        rect = QRect(self.xSpinBox.value(),
                     self.ySpinBox.value(),
                     self.widthSpinBox.value(),
                     self.heightSpinBox.value())

        self.canvas.beginDraw(True)
        self.painter.begin(self.canvas.getImage())
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 0))
        self.painter.setPen(pen)
        self.painter.drawRect(rect)
        self.painter.end()
        self.canvas.update()
