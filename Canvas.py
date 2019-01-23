from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Canvas(QDockWidget):
    def __init__(self, initImg, *, title, parent):
        super().__init__(title, parent)

        # image used to present
        self.image = initImg

        # double buffer
        self.tempImage = QImage(self.image)

        self.__dockContent = QWidget()

        self.frame = QFrame(self.__dockContent)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.installEventFilter(self)

        self.__gridLayout = QGridLayout(self.__dockContent)
        self.__gridLayout.setContentsMargins(2, 2, 2, 2)
        self.__gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.setWidget(self.__dockContent)
        parent.addDockWidget(Qt.LeftDockWidgetArea, self)

        # capture Canvas widget event
        self.frame.installEventFilter(parent)
        self.frame.setMouseTracking(True)

        # change dock widget back ground color
        __defaultWindowBackColor = QColor(150, 150, 150)
        pal = QPalette(self.palette())
        pal.setColor(QPalette.Background, __defaultWindowBackColor)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.__painter = QPainter()

        self.__begin = False

    @classmethod
    def new(cls, width, height, imgFormat=QImage.Format_RGB888, initColor=Qt.white, *, title, parent):
        image = QImage(width, height, imgFormat)
        image.fill(initColor)
        return cls(image, title=title, parent=parent)

    @classmethod
    def open(cls, path, *, title, parent):
        image = QImage(path)
        return cls(image, title=title, parent=parent)

    def eventFilter(self, watched, event):
        if watched == self.frame and event.type() == QEvent.Paint:
            self.__painter.begin(self.frame)

            if self.__begin:
                self.__painter.drawImage(1, 1, self.tempImage)
                self.tempImage = self.image.copy()
            else:
                self.__painter.drawImage(1, 1, self.image)

            self.__painter.end()
        return False

    def beginDblBuffer(self):
        self.__begin = True

    def endDblBuffer(self):
        self.__begin = False

    def getImage(self):
        if self.__begin:
            return self.tempImage
        else:
            return self.image
