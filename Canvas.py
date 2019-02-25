from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import numpy as np

from Preferences import Preferences


class Canvas(QWidget):
    def __init__(self, initImg, *, title, parent):
        super().__init__(parent)

        self.setWindowTitle(title)

        # canvas states
        # index in tab widget
        self.tabWidget = parent
        self.fileName = title
        self.filePath = ""
        self.isSaved = True

        # image used to present
        self.image = initImg
        # todo add different format support
        if self.image.format() != QImage.Format_RGB32:
            self.image = self.image.convertToFormat(QImage.Format_RGB32)
        self.mat = Canvas.generateMat(self.image)
        # invertible
        # self.__realMat = self.mat.astype(np.uint32)

        # double buffer
        self.tempImage = QImage(self.image)
        self.tempMat = Canvas.generateMat(self.tempImage)

        self.__dockContent = QWidget()

        self.frame = QLabel(self)
        self.frame.installEventFilter(self)
        self.frame.setMouseTracking(True)

        self.scrollArea = QScrollArea(self)
        self.frame.resize(self.image.size())
        self.scrollArea.setWidget(self.frame)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.__gridLayout = QGridLayout(self)
        self.__gridLayout.setContentsMargins(2, 2, 2, 2)
        self.__gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        # change dock widget back ground color
        __defaultWindowBackColor = QColor(150, 150, 150)
        pal = QPalette(self.palette())
        pal.setColor(QPalette.Background, __defaultWindowBackColor)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.__painter = QPainter()

        self.__begin = False

    @classmethod
    def new(cls, width, height, imgFormat=QImage.Format_RGB32, initColor=Qt.white, *, title, parent):
        image = QImage(width, height, imgFormat)
        image.fill(initColor)
        return cls(image, title=title, parent=parent)

    @classmethod
    def open(cls, path, *, title, parent):
        image = QImage(path)
        # todo add different format support
        if image.format() != QImage.Format_RGB32:
            image = image.convertToFormat(QImage.Format_RGB32)
        temp = cls(image, title=title, parent=parent)
        temp.filePath = path
        return temp

    def save(self):
        # todo fix this shit
        options = QFileDialog.DontUseNativeDialog if Preferences.getS("preferences.xml",
                                                                      "UseNativeDialog") == "False" else 0
        if self.filePath == "":
            # if the file is not opened from disk
            self.filePath, _ = QFileDialog.getSaveFileName(self,
                                                           self.tr("Save"),
                                                           ".\\" + self.fileName + ".jpg",
                                                           "JPEG (*.jpg *.jpeg);;PNG (*.png);;All File Formats (*.*)",
                                                           "JPEG (*.jpg *.jpeg)",
                                                           options)
        # if canceled
        if self.filePath != "":
            imgFormat = self.filePath.rpartition(".")[2].upper()
            self.image.save(self.filePath, imgFormat)
            self.saved()

    def saveAs(self):
        # todo fix this shit
        options = QFileDialog.DontUseNativeDialog if Preferences.getS("preferences.xml",
                                                                      "UseNativeDialog") == "False" else 0
        filePath, _ = QFileDialog.getSaveFileName(self,
                                                  self.tr("Save"),
                                                  self.filePath.rpartition(".")[0] + "jpg",
                                                  "JPEG (*.jpg *.jpeg);;PNG (*.png);;All File Formats (*.*)",
                                                  "JPEG (*.jpg *.jpeg)",
                                                  options)
        if filePath != "":
            imgFormat = filePath.rpartition(".")[2].upper()
            self.image.save(filePath, imgFormat)
            self.saved()

    def eventFilter(self, watched, event):
        if watched == self.frame and event.type() == QEvent.Paint:
            self.__painter.begin(self.frame)

            if self.__begin:
                self.__painter.drawImage(0, 0, self.tempImage)
                self.copyImageToTempImage()
            else:
                self.__painter.drawImage(0, 0, self.image)

            self.__painter.end()

        return False

    def beginDblBuffer(self):
        self.__begin = True

    def endDblBuffer(self):
        self.__begin = False
        self.copyTempImageToImage()

    def getImage(self):
        self.updated()

        if self.__begin:
            return self.tempImage
        else:
            return self.image

    def copyImageToTempImage(self):
        self.tempImage = self.image.copy()
        self.tempMat = Canvas.generateMat(self.tempImage)

    def copyTempImageToImage(self):
        self.image = self.tempImage.copy()
        self.mat = Canvas.generateMat(self.image)

    def updated(self):
        if self.isSaved is True:
            self.isSaved = False
            self.tabWidget.setTabText(self.tabWidget.indexOf(self), self.fileName + " *")

    def saved(self):
        if self.isSaved is False:
            self.isSaved = True
            self.tabWidget.setTabText(self.tabWidget.indexOf(self), self.fileName)

    def closeEvent(self, event):
        if not self.isSaved:
            button = QMessageBox.warning(self.parent(),
                                         "Save changes?",
                                         self.fileName + " has been modified, save changes?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            # cancel
            if button == QMessageBox.Cancel:
                event.ignore()

            # no
            if button == QMessageBox.No:
                self.tabWidget.removeCanvas(self)
                event.accept()

            # yes
            if button == QMessageBox.Yes:
                self.save()
                self.tabWidget.removeCanvas(self)
                event.accept()

        else:
            self.tabWidget.removeCanvas(self)

    def update(self):
        self.frame.repaint()

    @staticmethod
    # QImage format must be RGB32
    def generateMat(image: QImage) -> np.ndarray:
        return np.ndarray(shape=(image.height(), image.width(), image.depth() // 8),
                          dtype=np.uint8,
                          buffer=image.bits())

    def resizeImage(self, width: int, height: int):
        # resize image and tempImage
        self.image = self.image.scaled(width,
                                       height,
                                       Qt.IgnoreAspectRatio)
        self.mat = Canvas.generateMat(self.image)
        self.copyImageToTempImage()

        # resize frame
        self.frame.resize(width, height)
