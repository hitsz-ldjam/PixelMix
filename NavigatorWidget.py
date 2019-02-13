from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class NavigatorWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("NavigatorWidget")

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(40, 40, 40, 40)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.defaultSize = QSize(300, 300)
        self.resize(self.defaultSize)
        self.setMinimumSize(self.defaultSize)

    def updateImage(self, canvas):
        tempPix = QPixmap(canvas.image).scaled(self.sizeHint(), Qt.KeepAspectRatio);

        self.label.setAlignment(Qt.AlignCenter);
        self.label.setPixmap(tempPix);

    def noImage(self):
        self.label.setText("No image")

    def sizeHint(self):
        return self.defaultSize


class NavigatorDockWidget(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.dockContent = NavigatorWidget(self)
        self.setWidget(self.dockContent)
        self.setWindowTitle("Navigator")
