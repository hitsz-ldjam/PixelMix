from collections import namedtuple

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import Tool
from Preferences import Preferences
from Canvas import Canvas
from ColorWidget import ColorDockWidget
from NavigatorWidget import NavigatorDockWidget

# main window UI
from Ui_MainWindow import Ui_MainWindow
from Ui_CreateImageDialog import Ui_CreateImageDialog


class CreateImageDialog(QDialog, Ui_CreateImageDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

    @Slot(QAbstractButton)
    def on_buttonBox_clicked(self, button):
        if self.buttonBox.button(QDialogButtonBox.Ok) == button:
            if len(self.fileNameLine.text()) == 0:
                QMessageBox.warning(self,
                                    self.tr("Warning"),
                                    self.tr("File name should not be empty!"),
                                    QMessageBox.Yes)
            else:
                self.accept()

        if self.buttonBox.button(QDialogButtonBox.Cancel) == button:
            self.reject()

    @staticmethod
    def getImageInfo(parent):
        dialog = CreateImageDialog(parent)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.fileNameLine.text(), dialog.widthBox.value(), dialog.heightBox.value()
        else:
            return "", -1, -1


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


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # fetch preferences
        self.__preferences = Preferences("preferences.xml")

        # todo change canvas
        # hide default central widget
        # add tab widget to store canvas
        self.centralwidget.hide()
        self.__tabWidget = TabWidget(self)
        self.setCentralWidget(self.__tabWidget)

        # tracking mouse
        self.setMouseTracking(True)

        # move the main window to the center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # create a painter
        self.__painter = QPainter()
        self.__pen = QPen()
        self.__pen.setWidth(2)
        # anti aliasing
        self.__painter.setRenderHint(QPainter.Antialiasing, True)

        # create a tool dock list
        self.__toolDocks = {}

        # setup tool dock widgets
        self.initToolDock()

        # create a tool list
        self.__tools = []
        # record current tool
        self.__currTool = None

        self.initTools()

        # add paint tools to side bar
        self.__sideToolBtn = []
        self.initSideToolBar()

        # todo change canvas
        # add a default canvas
        canvas = Canvas.new(600, 480, title="Untitled", parent=self.__tabWidget)
        self.addCanvas(canvas)

        self.showMaximized()

    def addCanvas(self, canvas):
        # todo change canvas | addCanvas
        canvas.frame.installEventFilter(self)
        self.__tabWidget.addCanvas(canvas)
        # focus on new canvas
        self.setCurrCanvas(canvas)

    def removeCanvas(self, canvas):
        # todo change canvas
        self.__tabWidget.removeCanvas(canvas.index)

    def setCurrCanvas(self, canvas):
        if canvas is not None:
            self.__currTool.setTarget(canvas)

    def initToolDock(self):
        # navigator tool
        navigatorDockWidget = NavigatorDockWidget(self)
        self.addDockWidget(Qt.RightDockWidgetArea, navigatorDockWidget)
        self.__toolDocks["navigatorDockWidget"] = navigatorDockWidget

        # color tool
        colorDockWidget = ColorDockWidget(self)
        colorDockWidget.dockContent.colorChangedSignal.connect(self.colorChanged)
        self.addDockWidget(Qt.RightDockWidgetArea, colorDockWidget)
        self.__toolDocks["colorDockWidget"] = colorDockWidget

    def initTools(self):
        self.__tools.append(Tool.Brush(self.__painter))
        self.__tools.append(Tool.StraightLine(self.__painter))
        self.__tools.append(Tool.Rect(self.__painter))
        self.__tools.append(Tool.Ellipse(self.__painter))
        self.__currTool = self.__tools[0]

    def initSideToolBar(self):
        btnInfo = namedtuple("btnInfo", "type icon")
        toolBtnInfo = [btnInfo(Tool.ToolType.Brush, "resources/BrushTool.svg"),
                       btnInfo(Tool.ToolType.Null, ""),
                       btnInfo(Tool.ToolType.StraightLine, "resources/LineTool.svg"),
                       btnInfo(Tool.ToolType.Rect, "resources/RectangleTool.svg"),
                       btnInfo(Tool.ToolType.Ellipse, "resources/EllipseTool.svg")]

        for info in toolBtnInfo:
            if info.type == Tool.ToolType.Null:
                self.sideToolBar.addSeparator()
            else:
                btn = QToolButton(self)
                btn.setObjectName("PaintToolType" + str(info.type.value))
                btn.setIcon(QIcon(info.icon))
                btn.clicked.connect(self.switchTool)
                self.sideToolBar.addWidget(btn)
                self.__sideToolBtn.append(btn)

        self.__sideToolBtn[0].setDown(True)

    def switchTool(self):
        # magic
        prevTool = self.__currTool.type.value - 1
        currTool = int(self.sender().objectName()[13:]) - 1

        self.sender().setDown(True)
        if prevTool != currTool:
            self.__sideToolBtn[prevTool].setDown(False)

            self.__currTool = self.__tools[currTool]
            self.__currTool.setTarget(self.__tabWidget.currCanvas)

    def eventFilter(self, watched, event):
        if self.__tabWidget.currCanvas is not None:
            if watched == self.__tabWidget.currCanvas.frame:
                self.__currTool.process(self.__pen, event)
                self.__toolDocks["navigatorDockWidget"].dockContent.updateImage(self.__tabWidget.currCanvas)
        else:
            self.__toolDocks["navigatorDockWidget"].dockContent.noImage()

        return False

    @Slot()
    def on_menuFileOpen_triggered(self):
        options = QFileDialog.DontUseNativeDialog if self.__preferences.get("UseNativeDialog") == "False" else 0
        # options |= QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self,
                                              "Open File",
                                              filter="JPEG (*.jpg *.jpeg);;PNG (*.png);;All File Formats (*.*)",
                                              options=options)
        # if canceled
        if path is "":
            return

        title = path.rpartition("/")[2]
        canvas = Canvas.open(path, title=title, parent=self.__tabWidget)

        self.addCanvas(canvas)

    @Slot()
    def on_menuFileCreate_triggered(self):
        fileName, width, height = CreateImageDialog.getImageInfo(self)
        if width != -1:
            self.addCanvas(Canvas.new(width, height, title=fileName, parent=self.__tabWidget))

    @Slot()
    def on_menuFileSave_triggered(self):
        self.__tabWidget.currCanvas.save()

    @Slot()
    def on_menuFileSaveAs_triggered(self):
        self.__tabWidget.currCanvas.saveAs()

    @Slot()
    def on_menuFileQuit_triggered(self):
        self.close()

    @Slot()
    def on_menuEditPreferences_triggered(self):
        dialog = QDialog()

        cb = QCheckBox("Use native dialog", dialog)
        cb.move(5, 10)
        if self.__preferences.get("UseNativeDialog") == "True":
            cb.toggle()
        cb.stateChanged.connect(self.updateUseNativeDialog)

        dialog.setWindowTitle("Preferences")
        dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        dialog.resize(280, 200)
        dialog.show()
        dialog.exec_()

    def updateUseNativeDialog(self, state):
        self.__preferences.set("UseNativeDialog", state == Qt.Checked)
        self.__preferences.saveAll()

    @Slot()
    def on_menuHelpAbout_triggered(self):
        dialog = QDialog(self)

        # todo
        _credits = QLabel("Icons made by Flaticon", dialog)

        dialog.setWindowTitle("About")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.show()
        dialog.exec_()

    @Slot()
    def colorChanged(self, color):
        self.__pen.setColor(color)
        self.__pen.setWidth(2)

    def closeEvent(self, event):
        allSaved = True
        for canvas in self.__tabWidget.canvases:
            if not canvas.isSaved:
                allSaved = False
                break

        if not allSaved:
            button = QMessageBox.warning(self,
                                         "Warning",
                                         "There are files that have been modified but not saved,"
                                         "want to save now?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            # cancel
            if button == QMessageBox.Cancel:
                event.ignore()
            # no
            if button == QMessageBox.No:
                event.accept()

            # yes
            if button == QMessageBox.Yes:
                for canvas in self.__canvases:
                    if not canvas.isSaved:
                        canvas.save()
