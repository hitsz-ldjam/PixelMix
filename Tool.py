from enum import Enum, unique
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


@unique
class ToolType(Enum):
    Null = 0
    StraightLine = 1
    Rect = 2
    Ellipse = 3
    Line = 4


class ToolBase(object):
    def __init__(self, painter, canvas=None):
        super().__init__()
        self.type = ToolType.Null
        self.isDrawing = False
        self.painter = painter
        self.canvas = canvas
        self.cursor = Qt.ArrowCursor

    def setTarget(self, canvas):
        self.canvas = canvas
        self.canvas.setCursor(self.cursor)

    def process(self, pen, event):
        pass

    @staticmethod
    def calculateRect(pos1, pos2):
        topLeft = QPoint()
        bottomRight = QPoint()
        topLeft.setX(min(pos1.x(), pos2.x()))
        topLeft.setY(min(pos1.y(), pos2.y()))
        bottomRight.setX(max(pos1.x(), pos2.x()))
        bottomRight.setY(max(pos1.y(), pos2.y()))
        return QRect(topLeft, bottomRight)


class StraightLine(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.StraightLine
        self.cursor = Qt.CrossCursor
        self.beginPoint = QPoint()
        self.endPoint = QPoint()

    def process(self, pen, event):
        # begin / end drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            if not self.isDrawing:
                # begin drawing
                self.beginPoint = event.pos()
                self.canvas.beginDblBuffer()
                self.isDrawing = True

            else:
                # end drawing
                self.canvas.endDblBuffer()
                self.painter.begin(self.canvas.getImage())
                self.painter.setPen(pen)
                
                self.painter.drawLine(self.beginPoint, self.endPoint)

                self.painter.end()
                self.canvas.update()

                self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())
            self.painter.setPen(pen)

            self.painter.drawLine(self.beginPoint, event.pos())
            self.endPoint = event.pos()

            self.painter.end()
            self.canvas.update()


class Rect(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.Rect
        self.cursor = Qt.CrossCursor
        self.beginPoint = QPoint()
        self.endPoint = QPoint()

    def process(self, pen, event):
        # begin / end drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            if not self.isDrawing:
                # begin drawing
                self.beginPoint = event.pos()
                self.canvas.beginDblBuffer()
                self.isDrawing = True

            else:
                # end drawing
                self.canvas.endDblBuffer()
                self.painter.begin(self.canvas.getImage())
                self.painter.setPen(pen)

                self.painter.drawRect(self.calculateRect(self.beginPoint, self.endPoint))

                self.painter.end()
                self.canvas.update()

                self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())
            self.painter.setPen(pen)

            self.painter.drawRect(self.calculateRect(self.beginPoint, event.pos()))
            self.endPoint = event.pos()

            self.painter.end()
            self.canvas.update()


class Ellipse(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.Ellipse
        self.cursor = Qt.CrossCursor
        self.beginPoint = QPoint()
        self.endPoint = QPoint()

    def process(self, pen, event):
        # begin / end drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            if not self.isDrawing:
                # begin drawing
                self.beginPoint = event.pos()
                self.canvas.beginDblBuffer()
                self.isDrawing = True

            else:
                # end drawing
                self.canvas.endDblBuffer()
                self.painter.begin(self.canvas.getImage())
                self.painter.setPen(pen)

                self.painter.drawEllipse(self.calculateRect(self.beginPoint, self.endPoint))

                self.painter.end()
                self.canvas.update()

                self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())
            self.painter.setPen(pen)

            self.painter.drawEllipse(self.calculateRect(self.beginPoint, event.pos()))
            self.endPoint = event.pos()

            self.painter.end()
            self.canvas.update()


class Line(ToolBase):
    def __init__(self, painter, canvas=None):
        super().__init__(painter, canvas)
        self.type = ToolType.Line
        self.cursor = Qt.CrossCursor
        self.lastPoint = QPoint()

    def process(self, pen, event):
        # begin drawing
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            if not self.isDrawing:
                
                self.lastPoint = event.pos()
                self.isDrawing = True
        # end drawing
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            self.isDrawing = False

        # while drawing
        if event.type() == QEvent.MouseMove and self.isDrawing:
            self.painter.begin(self.canvas.getImage())
            self.painter.setPen(pen)

            self.painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()

            self.painter.end()
            self.canvas.update()
