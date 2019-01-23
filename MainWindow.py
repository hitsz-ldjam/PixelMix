from collections import namedtuple

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import Tool
from Preferences import Preferences
from Canvas import Canvas
from ColorWidget import ColorDockWidget

# main window UI
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # fetch preferences
        self.__preferences = Preferences("preferences.xml")

        # hide default central widget
        self.centralwidget.hide()

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

        # add a default canvas
        canvas = Canvas.new(854, 480, title="Untitled", parent=self)
        self.__canvases.append(canvas)
        self.__currCanvas = self.__canvases[0]

        # create a painter
        self.__painter = QPainter()
        self.__pen = QPen()
        # anti aliasing
        self.__painter.setRenderHint(QPainter.Antialiasing, True)

        # create a tool dock list
        self.__toolDocks = {}

        # test (add some tool docks)
        for i in range(1):
            self.addToolDock(Qt.RightDockWidgetArea, "Tool_" + str(i + 1))

        # add Color widget
        colorDockWidget = ColorDockWidget(self)
        colorDockWidget.dockContent.colorChangedSignal.connect(self.colorChanged)
        self.addDockWidget(Qt.RightDockWidgetArea, colorDockWidget)
        self.__toolDocks["colorDockWidget"] = colorDockWidget

        # create a tool list
        self.__tools = []
        # record current tool
        self.__currTool = None

        self.initTools()

        # add paint tools to side bar
        self.__sideToolBtn = []
        self.initSideToolBar()

        self.showMaximized()

    def addToolDock(self, area, title):
        dock = QDockWidget(title)
        self.addDockWidget(area, dock)
        self.__toolDocks[title] = dock
        return dock

    def initTools(self):
        self.__tools.append(Tool.Brush(self.__painter))
        self.__tools.append(Tool.StraightLine(self.__painter))
        self.__tools.append(Tool.Rect(self.__painter))
        self.__tools.append(Tool.Ellipse(self.__painter))
        self.__currTool = self.__tools[0]
        self.__currTool.setTarget(self.__currCanvas)

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
            self.__currTool.setTarget(self.__currCanvas)

    def eventFilter(self, watched, event):
        if self.__currCanvas is None:
            return False

        if watched == self.__currCanvas.frame:
            self.__currTool.process(self.__pen, event)

        return False

    @Slot()
    def on_menuFileOpen_triggered(self):
        options = QFileDialog.DontUseNativeDialog if self.__preferences.get("UseNativeDialog") == "False" else 0
        # options |= QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self,
                                              "Open File",
                                              filter="JPEG (*.jpg *.jpeg);;PNG (*.png);;All File Formats (*.*)",
                                              options=options)
        title = path.rpartition("/")[2]
        canvas = Canvas.open(path, title=title, parent=self)
        self.__canvases.append(canvas)
        # todo
        # switch focus canvas
        # delete these after test
        self.__currCanvas = canvas
        self.__currTool.setTarget(self.__currCanvas)

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
