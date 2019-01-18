from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from enum import Enum, unique

if __name__ == "__main__":
    pass


@unique
class PaintMode(Enum):
    Line = 1
    Rect = 2
    Ellipse = 3


class Canvas(object):
    def __init__(self, width, height, imgFormat, parent, title):
        self.image = QImage(width, height, imgFormat)
        self.widget = QDockWidget(parent)
        self.widget.setWindowTitle(title)
        self.widget.setAllowedAreas(Qt.AllDockWidgetAreas)


class Painter(QPainter):
    def __init__(self):
        super().__init__()
