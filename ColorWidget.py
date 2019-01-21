from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Ui_ColorWidget import Ui_ColorWidget


class ColorWidget(QWidget, Ui_ColorWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.colorRect.installEventFilter(self)

        self.__hue = 0

        self.image = QImage(self.colorRect.width(), self.colorRect.height(), QImage.Format_RGB888)
        self.setColorRectImage()

        self.__painter = QPainter()

    def setColorRectImage(self):
        width = self.colorRect.width()
        height = self.colorRect.height()

        for x in range(width):
            for y in range(height):
                color = QColor.fromHsv(self.__hue,
                                       x / width * 255,
                                       (1 - y / width) * 255)
                self.image.setPixelColor(x, y, color)
        self.colorRect.update()

    def eventFilter(self, watched, event):
        if watched == self.colorRect and event.type() == QEvent.Paint:
            self.__painter.begin(self.colorRect)
            self.__painter.drawImage(0, 0, self.image)
            self.__painter.end()
        return False

    @Slot("int")
    def on_hueSlider_sliderMoved(self, value):
        self.__hue = value
        self.setColorRectImage()


class ColorDockWidget(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.__dockContent = ColorWidget(self)
        self.setWidget(self.__dockContent)
