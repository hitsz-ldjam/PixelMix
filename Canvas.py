from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import numpy as np

from CvQtBridge import CvQtBridge
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
        self.mat = CvQtBridge.qImageToSharedMat(self.image)
        # invertible
        # self.__realMat = self.mat.astype(np.uint32)

        # double buffer
        self.tempImage = QImage(self.image)
        self.tempMat = CvQtBridge.qImageToSharedMat(self.tempImage)

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

        self.__useDbBuffer = False

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
                                                  self.filePath.rpartition(".")[0] + ".jpg",
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

            if self.__useDbBuffer:
                self.__painter.drawImage(0, 0, self.tempImage)
                self.copyImageToTempImage()
            else:
                self.__painter.drawImage(0, 0, self.image)

            self.__painter.end()

        return False

    def beginDraw(self, useDbBuffer: bool):
        self.__useDbBuffer = useDbBuffer

    def endDraw(self):
        if self.__useDbBuffer:
            self.__useDbBuffer = False
            self.copyTempImageToImage()
        else:
            self.copyImageToTempImage()

    def getImage(self):
        self.updated()

        if self.__useDbBuffer:
            return self.tempImage
        else:
            return self.image

    def copyImageToTempImage(self):
        self.tempImage = self.image.copy()
        self.tempMat = CvQtBridge.qImageToSharedMat(self.tempImage)

    def copyTempImageToImage(self):
        self.image = self.tempImage.copy()
        self.mat = CvQtBridge.qImageToSharedMat(self.image)

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
                                         QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if button == QMessageBox.Cancel:
                event.ignore()

            if button == QMessageBox.Discard:
                self.tabWidget.removeCanvas(self)
                event.accept()

            if button == QMessageBox.Save:
                self.save()
                self.tabWidget.removeCanvas(self)
                event.accept()

        else:
            self.tabWidget.removeCanvas(self)

    def update(self):
        self.frame.repaint()

    def resizeImage(self, width: int, height: int):
        # resize image and tempImage
        self.image = self.image.scaled(width,
                                       height,
                                       Qt.IgnoreAspectRatio)
        self.mat = CvQtBridge.qImageToSharedMat(self.image)
        self.copyImageToTempImage()

        # resize frame
        self.frame.resize(width, height)
