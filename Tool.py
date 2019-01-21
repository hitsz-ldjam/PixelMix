from enum import Enum, unique
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


@unique
class ToolType(Enum):
    Null = 0
    Line = 1
    Rect = 2
    Ellipse = 3


class ToolBase(object):
    def __init__(self, painter, canvas=None):
        super().__init__()
        self.type = ToolType.Null
        self.isDrawing = False
        self.painter = painter
        self.canvas = canvas

    def setTarget(self, canvas):
        self.canvas = canvas

    def process(self, event):
        pass


class Line(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.Line
        self.beginPoint = QPoint()
        self.endPoint = QPoint()

    def process(self, event):
        # begin drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton and not self.isDrawing:
                self.beginPoint = event.pos()
                self.canvas.beginDblBuffer()
                self.isDrawing = True

        # end drawing
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton and self.isDrawing:
                self.canvas.endDblBuffer()
                self.painter.begin(self.canvas.getImage())

                self.endPoint = event.pos()
                if self.endPoint != self.beginPoint:
                    self.painter.drawLine(self.beginPoint, self.endPoint)

                self.painter.end()
                self.canvas.update()

                self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())

            self.endPoint = event.pos()
            self.painter.drawLine(self.beginPoint, self.endPoint)

            self.painter.end()
            self.canvas.update()


class Rect(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.Rect
        self.beginPoint = QPoint()
        self.endPoint = QPoint()

    def process(self, event):
        # begin drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton and not self.isDrawing:
                self.beginPoint = event.pos()
                self.canvas.beginDblBuffer()
                self.isDrawing = True

        # end drawing
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton and self.isDrawing:
            self.canvas.endDblBuffer()
            self.painter.begin(self.canvas.getImage())

            self.endPoint = event.pos()
            if self.endPoint != self.beginPoint:
                self.painter.drawRect(self.calculateRect(self.beginPoint, self.endPoint))

            self.painter.end()
            self.canvas.update()

            self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())

            self.endPoint = event.pos()
            self.painter.drawRect(self.calculateRect(self.beginPoint, self.endPoint))

            self.painter.end()
            self.canvas.update()

    @staticmethod
    def calculateRect(pos1, pos2):
        topLeft = QPoint()
        bottomRight = QPoint()
        topLeft.setX(min(pos1.x(), pos2.x()))
        topLeft.setY(min(pos1.y(), pos2.y()))
        bottomRight.setX(max(pos1.x(), pos2.x()))
        bottomRight.setY(max(pos1.y(), pos2.y()))
        return QRect(topLeft, bottomRight)
