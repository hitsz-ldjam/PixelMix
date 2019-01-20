from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

# main window UI
from Ui_MainWindow import Ui_MainWindow

g_defaultWindowBackColor = QColor(150, 150, 150)


class Canvas(QDockWidget):
    def __init__(self, width, height, imgFormat, initColor=Qt.white, *, title, parent):
        super().__init__(title, parent)
        self.image = QImage(width, height, imgFormat)
        self.image.fill(initColor)

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

    def eventFilter(self, watched, event):
        if watched == self.frame and event.type() == QEvent.Paint:
            self.__painter.begin(self.frame)
            self.__painter.drawImage(1, 1, self.image)
            self.__painter.end()
        return False


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
        self.addCanvas(300, 300, QImage.Format_RGB888, "Untitled")
        self.__currCanvas = self.__canvases[0]

        # create a painter
        self.__painter = QPainter()

        # test (add some tool docks)
        for i in range(4):
            self.addToolDock(Qt.RightDockWidgetArea, "Tool_" + str(i + 1))

        self.setDockLayout()
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

    def setDockLayout(self):
        self.addDockWidget(Qt.LeftDockWidgetArea, self.__canvases[0])

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
    def on_menuHelpAbout_triggered(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("About")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.show()
        dialog.exec_()

    def paintEvent(self, event):
        self.__painter.begin(self.__currCanvas.image)
        self.__painter.setPen(QPen(Qt.green, 3))
        self.__painter.drawLine(0, 0, 100, 100)
        self.__painter.end()

    def mouseMoveEvent(self, event):
        print("Main Window mouse move")

    def eventFilter(self, watched, event):
        if self.__currCanvas is None:
            return False

        if watched == self.__currCanvas.frame and event.type() == QEvent.MouseMove:
            print("x : %d, y : %d" % (event.x(), event.y()))
            # todo to press mouse event
        return False
