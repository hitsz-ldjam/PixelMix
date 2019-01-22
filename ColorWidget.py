from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Ui_ColorWidget import Ui_ColorWidget


class ColorWidget(QWidget, Ui_ColorWidget):
    colorChangedSignal = Signal(QColor)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.colorRect.installEventFilter(self)
        self.colorRect.setMouseTracking(True)

        self.__hue = 0
        self.__rectWidth = self.colorRect.width()
        self.__rectHeight = self.colorRect.height()

        self.image = QImage(self.__rectWidth, self.__rectHeight, QImage.Format_RGB888)

        self.__painter = QPainter()
        self.__selectedPos = QPoint(0, 0)
        self.__selectedColor = QColor(Qt.black)
        self.__isSelecting = False

        # color changed signal

        self.setColorRectImage()

    def setColorRectImage(self):

        for x in range(self.__rectWidth):
            for y in range(self.__rectHeight):
                self.image.setPixel(x, y, QColor.fromHsv(self.__hue,
                                                         x / self.__rectWidth * 255,
                                                         (1 - y / self.__rectHeight) * 255).rgb())

    def eventFilter(self, watched, event):
        if watched == self.colorRect:
            if event.type() == QEvent.Paint:
                self.__painter.begin(self.colorRect)
                self.__painter.drawImage(0, 0, self.image)
                if self.__selectedColor.saturation() < 70 and self.__selectedColor.value() > 180:
                    self.__painter.setPen(QPen(Qt.black))
                else:
                    self.__painter.setPen(QPen(Qt.white))
                self.__painter.drawEllipse(self.__selectedPos, 5, 5)
                self.__painter.end()

            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.__isSelecting = True
                self.setSelectedPos(event.pos())
                self.colorRect.update()
                self.setSpinBox(self.__selectedColor)

            if event.type() == QEvent.MouseMove and self.__isSelecting:
                self.setSelectedPos(event.pos())
                self.colorRect.update()
                self.setSpinBox(self.__selectedColor)

            if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.__isSelecting = False

        return False

    # calculate HSV color from mouse position
    def calculateHsvFromCoord(self, pos):
        return QColor.fromHsv(self.__hue,
                              pos.x() / self.__rectWidth * 255,
                              (1 - pos.y() / self.__rectHeight) * 255)

    # change the spin box
    def setSpinBox(self, color):
        self.hSpinBox.setValue(color.hue())
        self.sSpinBox.setValue(color.saturation() / 255 * 100)
        self.vSpinBox.setValue(color.value() / 255 * 100)

        self.rSpinBox.setValue(color.red())
        self.gSpinBox.setValue(color.green())
        self.bSpinBox.setValue(color.blue())

    # set the pos that been selected
    def setSelectedPos(self, pos):
        if 0 <= pos.x() <= self.__rectWidth:
            self.__selectedPos.setX(pos.x())

        if 0 <= pos.y() <= self.__rectHeight:
            self.__selectedPos.setY(pos.y())

        self.__selectedColor = self.calculateHsvFromCoord(self.__selectedPos)
        self.colorChangedSignal.emit(self.__selectedColor)

    @Slot(int)
    def on_hueSlider_valueChanged(self, value):
        self.__hue = value
        self.__selectedColor = self.calculateHsvFromCoord(self.__selectedPos)
        self.colorChangedSignal.emit(self.__selectedColor)
        self.setColorRectImage()
        self.colorRect.update()


class ColorDockWidget(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.dockContent = ColorWidget(self)
        self.setWidget(self.dockContent)
