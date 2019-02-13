from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Ui_ColorWidget import Ui_ColorWidget


class ColorWidget(QWidget, Ui_ColorWidget):
    # color changed signal
    colorChangedSignal = Signal(QColor)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.colorRect.installEventFilter(self)
        self.colorRect.setMouseTracking(True)

        self.defaultSize = QSize(400, 250)
        self.resize(self.defaultSize)
        self.setMinimumSize(self.defaultSize)

        # recording the value of slider
        self.__hue = 0
        self.__rectWidth = self.colorRect.width()
        self.__rectHeight = self.colorRect.height()

        # the image presented on colorRect
        self.image = QImage(self.__rectWidth, self.__rectHeight, QImage.Format_RGB888)

        self.__painter = QPainter()
        # pos selected by mouse
        self.__selectedPos = QPoint(0, self.__rectHeight)
        self.__selectedColor = QColor(Qt.black)
        self.__isSelecting = False

        # repaint the image on colorRect
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
                # if self.__selectedColor.saturation() < 70 and self.__selectedColor.value() > 180:
                #     self.__painter.setPen(QPen(Qt.black))
                # else:
                #     self.__painter.setPen(QPen(Qt.white))  (R*299 + G*587 + B*114 + 500) / 1000
                if (self.__selectedColor.red() * 299 +
                    self.__selectedColor.green() * 587 +
                    self.__selectedColor.blue() * 114 + 500) / 1000 > 150:
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

    def calculateCoordFromHsv(self, saturation, value):
        return QPoint(saturation / 255 * self.__rectWidth,
                      (1 - value / 255) * self.__rectHeight)

    # change the spinBox
    def setHsvSpinBox(self, color):
        self.hSpinBox.setValue(color.hue())
        self.sSpinBox.setValue(color.saturation() / 255 * 100)
        self.vSpinBox.setValue(color.value() / 255 * 100)

    def setRgbSpinBox(self, color):
        self.rSpinBox.setValue(color.red())
        self.gSpinBox.setValue(color.green())
        self.bSpinBox.setValue(color.blue())

    def setSpinBox(self, color):
        self.setHsvSpinBox(color)
        self.setRgbSpinBox(color)

    # set the pos that been selected
    def setSelectedPos(self, pos):
        if 0 <= pos.x() <= self.__rectWidth:
            self.__selectedPos.setX(pos.x())

        if 0 <= pos.y() <= self.__rectHeight:
            self.__selectedPos.setY(pos.y())

        self.__selectedColor = self.calculateHsvFromCoord(self.__selectedPos)
        self.colorChangedSignal.emit(self.__selectedColor)

    # set the color when spinBox changed
    def setSelectedColor(self, color):
        self.__selectedColor = color
        self.__selectedPos = self.calculateCoordFromHsv(color.saturation(), color.value())
        self.hueSlider.setValue(color.hue())
        self.colorChangedSignal.emit(self.__selectedColor)

    @Slot(int)
    def on_hueSlider_valueChanged(self, value):
        self.__hue = value
        self.__selectedColor = self.calculateHsvFromCoord(self.__selectedPos)
        self.colorChangedSignal.emit(self.__selectedColor)
        self.setColorRectImage()
        self.colorRect.update()
        self.setSpinBox(self.__selectedColor)

    # slots of spinBoxes
    @Slot(int)
    def on_hSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.hueSlider.setValue(self.hSpinBox.value())

    @Slot(int)
    def on_sSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.hsvSpinBoxChanged()

    @Slot(int)
    def on_vSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.hsvSpinBoxChanged()

    @Slot(int)
    def on_rSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.rgbSpinBoxChanged()

    @Slot(int)
    def on_gSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.rgbSpinBoxChanged()

    @Slot(int)
    def on_bSpinBox_valueChanged(self, value):
        if self.focusWidget() is self.sender():
            self.rgbSpinBoxChanged()

    # /slots of spinBoxes

    def hsvSpinBoxChanged(self):
        hsv = QColor.fromHsv(self.hSpinBox.value(),
                             self.sSpinBox.value() / 100 * 255,
                             self.vSpinBox.value() / 100 * 255)

        self.setRgbSpinBox(hsv)
        self.setSelectedColor(hsv)
        self.colorRect.update()

    def rgbSpinBoxChanged(self):
        rgb = QColor.fromRgb(self.rSpinBox.value(),
                             self.gSpinBox.value(),
                             self.bSpinBox.value())

        self.setHsvSpinBox(rgb)
        self.setSelectedColor(rgb)
        self.colorRect.update()

    def sizeHint(self):
        return self.defaultSize


class ColorDockWidget(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.dockContent = ColorWidget(self)
        self.setWidget(self.dockContent)
        self.setWindowTitle("Color tool")
