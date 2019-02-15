from PySide2.QtWidgets import *

class TabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)

        # connect signal and slot
        self.tabCloseRequested.connect(self.canvasCloseRequest)
        self.currentChanged.connect(self.currentCanvasChanged)

        self.canvases = []
        self.currCanvas = None

    def addCanvas(self, canvas):
        self.addTab(canvas, canvas.windowTitle())
        self.currCanvas = canvas
        self.canvases.append(canvas)
        self.setCurrentIndex(self.indexOf(canvas))

    def removeCanvas(self, canvas):
        self.removeTab(self.indexOf(canvas))
        self.canvases.remove(canvas)
        canvas.deleteLater()

    def canvasCloseRequest(self, index):
        self.widget(index).close()

    def currentCanvasChanged(self, index):
        self.currCanvas = self.widget(index)
        self.parent().setCurrCanvas(self.currCanvas)
