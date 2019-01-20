from enum import Enum, unique
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import Tool

# main window UI
from Ui_MainWindow import Ui_MainWindow

g_defaultWindowBackColor = QColor(150, 150, 150)


class Canvas(QDockWidget):

    def __init__(self, width, height, imgFormat, initColor=Qt.white, *, title, parent):
        super().__init__(title, parent)

        # image used to present
        self.image = QImage(width, height, imgFormat)
        self.image.fill(initColor)

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

        # capture Canvas widget mouse event
        self.frame.installEventFilter(parent)
        self.frame.setMouseTracking(True)

        self.__painter = QPainter()

        self.__begin = False

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


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # hide default central widget
        self.centralwidget.hide()
        self.setDockNestingEnabled(True)

        # tracking mouse
        self.setMouseTracking(True)

        # move the main window to the center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # create a canvas list
        self.__canvases = []
        # record current canvas
        self.__currCanvas = None
        # create a tool dock list
        self.__toolDocks = []

        # add a default canvas
        self.addCanvas(400, 600, QImage.Format_RGB888, "Untitled")
        self.__currCanvas = self.__canvases[0]

        # create a painter
        self.__painter = QPainter()
        # Antialias
        self.__painter.setRenderHint(QPainter.Antialiasing, True)

        # test (add some tool docks)
        for i in range(1):
            self.addToolDock(Qt.RightDockWidgetArea, "Tool_" + str(i + 1))

        # drawing
        # self.__isDrawing = False
        # self.__currTool = ToolType.Line
        # self.__points = []
        # create a tool list
        self.__tools = []
        # record current tool
        self.__currTool = None

        self.initTools()

        self.show()

    def addCanvas(self, width, height, imgFormat, title, color=g_defaultWindowBackColor):
        # set background color
        canvas = Canvas(width, height, imgFormat, title=title, parent=self)
        pal = QPalette(canvas.palette())
        pal.setColor(QPalette.Background, color)
        canvas.setAutoFillBackground(True)
        canvas.setPalette(pal)

        self.__canvases.append(canvas)
        return canvas

    def addToolDock(self, area, title):
        dock = QDockWidget(title)
        self.addDockWidget(area, dock)
        self.__toolDocks.append(dock)
        return dock

    def initTools(self):
        self.__tools.append(Tool.Line(self.__painter))
        self.__tools.append(Tool.Rect(self.__painter))
        self.__currTool = self.__tools[1]
        self.__currTool.setTarget(self.__currCanvas)

    @Slot()
    def on_menuFileOpen_triggered(self):
        path = QFileDialog.getOpenFileName(self, "Open File", "C:/", "All File Formats (*.*)", "")
        print(path)

    @Slot()
    def on_menuFileCreate_triggered(self):
        # todo
        print("Create")

    @Slot()
    def on_menuFileSave_triggered(self):
        # todo
        print("Save")

    @Slot()
    def on_menuFileSaveAs_triggered(self):
        # todo
        print("SaveAs")

    @Slot()
    def on_menuFileQuit_triggered(self):
        self.close()

    @Slot()
    def on_menuEditPreferences_triggered(self):
        print("Preferences")
        dialog = QDialog(self)
        dialog.setWindowTitle("Preferences")
        dialog.show()
        dialog.exec_()
        # todo

    @Slot()
    def on_menuHelpAbout_triggered(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("About")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.show()
        dialog.exec_()

    def paintEvent(self, event):
        pass

    def eventFilter(self, watched, event):
        if self.__currCanvas is None:
            return False

        if watched == self.__currCanvas.frame:
            self.__currTool.process(event)
        # if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
        #     # draw line
        #     if self.__currTool == ToolType.Line:
        #         if self.__isDrawing:
        #             self.__currCanvas.endDblBuffer()
        #             self.__painter.begin(self.__currCanvas.getImage())
        #             self.__painter.setPen(QPen(Qt.green, 3))
        #             self.__painter.drawLine(self.__points[0], self.__points[1])
        #             self.__painter.end()
        #             self.__currCanvas.update()
        #
        #             self.__points.clear()
        #             self.__isDrawing = False
        #         else:
        #             self.__points.append(event.pos())
        #             self.__points.append(QPoint(0, 0))
        #             self.__currCanvas.beginDblBuffer()
        #             self.__isDrawing = True
        #
        # if event.type() == QEvent.MouseMove:
        #     # draw line
        #     if self.__currTool == ToolType.Line:
        #         if self.__isDrawing:
        #             self.__painter.begin(self.__currCanvas.getImage())
        #             self.__painter.setPen(QPen(Qt.green, 3))
        #             self.__painter.drawLine(self.__points[0], event.pos())
        #             self.__points[1] = event.pos()
        #             self.__painter.end()
        #             self.__currCanvas.update()

        return False
