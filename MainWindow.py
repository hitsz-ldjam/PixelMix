from collections import namedtuple

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import Tool
from Canvas import Canvas
from Preferences import Preferences
from SliderProxyStyle import SliderProxyStyle

from ColorWidget import ColorDockWidget
from NavigatorWidget import NavigatorDockWidget
from TabWidget import TabWidget

from BrightnessContrastDialog import BrightnessContrastDialog
from CreateImageDialog import CreateImageDialog
from ImageSizeDialog import ImageSizeDialog
from CanvasSizeDialog import CanvasSizeDialog

from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # fetch preferences
        self.__preferences = Preferences("preferences.xml")

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
        self.__pen.setCapStyle(Qt.RoundCap)
        self.__pen.setJoinStyle(Qt.RoundJoin)

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

        # initialize main tool bar
        self.__mainToolBarWidgets = []
        self.initMainToolBar()

        # add a default canvas
        canvas = Canvas.new(600, 480, title="Untitled", parent=self.__tabWidget)
        self.addCanvas(canvas)

        self.showMaximized()

    def addCanvas(self, canvas):
        canvas.frame.installEventFilter(self)
        self.__tabWidget.addCanvas(canvas)
        # focus on new canvas
        self.setCurrCanvas(canvas)

    def removeCanvas(self, canvas):
        self.__tabWidget.removeCanvas(canvas.index)

    def setCurrCanvas(self, canvas):
        if canvas is not None:
            self.__currTool.setTarget(canvas)

    def initToolDock(self):
        # navigator
        navigatorDockWidget = NavigatorDockWidget(self)
        self.addDockWidget(Qt.RightDockWidgetArea, navigatorDockWidget)
        self.__toolDocks["navigatorDockWidget"] = navigatorDockWidget

        # palette
        colorDockWidget = ColorDockWidget(self)
        colorDockWidget.dockContent.colorChangedSignal.connect(self.colorChanged)
        self.addDockWidget(Qt.RightDockWidgetArea, colorDockWidget)
        self.__toolDocks["colorDockWidget"] = colorDockWidget

    def initTools(self):
        self.__tools.append(Tool.Brush(self.__painter))
        self.__tools.append(Tool.Eraser(self.__painter))
        self.__tools.append(Tool.StraightLine(self.__painter))
        self.__tools.append(Tool.Rect(self.__painter))
        self.__tools.append(Tool.Ellipse(self.__painter))
        self.__currTool = self.__tools[0]

    def initSideToolBar(self):
        btnInfo = namedtuple("btnInfo", "type icon")
        toolBtnInfo = [btnInfo(Tool.ToolType.Brush, "resources/BrushTool.svg"),
                       btnInfo(Tool.ToolType.Eraser, "resources/EraserTool.svg"),
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

    def initMainToolBar(self):
        label = QLabel(self)
        label.setText("Pen size: ")
        self.__mainToolBarWidgets.append(label)
        self.mainToolBar.addWidget(label)

        slider = QSlider(self)
        slider.setMaximumWidth(300)
        slider.setObjectName("penSizeSlider")
        slider.setOrientation(Qt.Horizontal)
        slider.setSliderPosition(2)
        slider.setStyle(SliderProxyStyle(slider.style()))
        slider.setRange(1, 100)
        slider.valueChanged.connect(self.on_penSizeSlider_valueChanged)
        self.__mainToolBarWidgets.append(slider)
        self.mainToolBar.addWidget(slider)

        spinBox = QSpinBox(self)
        spinBox.setObjectName("penSizeSpinBox")
        spinBox.setRange(1, 100)
        spinBox.setValue(2)
        spinBox.valueChanged.connect(self.on_penSizeSpinBox_valueChanged)
        self.__mainToolBarWidgets.append(spinBox)
        self.mainToolBar.addWidget(spinBox)

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
        options |= QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self,
                                              caption="Open File",
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
        dialog = QDialog(self)

        cb = QCheckBox("Use native dialog", dialog)
        cb.move(5, 10)
        if self.__preferences.get("UseNativeDialog") == "True":
            cb.toggle()
        cb.stateChanged.connect(self.updateUseNativeDialog)

        dialog.setWindowTitle("Preferences")
        dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)
        dialog.setModal(True)
        dialog.resize(280, 200)
        dialog.show()
        dialog.exec_()

    def updateUseNativeDialog(self, state):
        self.__preferences.set("UseNativeDialog", state == Qt.Checked)
        self.__preferences.saveAll()

    @Slot()
    def on_menuEffectBrightnessContrast_triggered(self):
        dialog = BrightnessContrastDialog(self, self.__tabWidget.currCanvas)
        dialog.setModal(True)
        dialog.exec_()

    @Slot()
    def on_menuHelpAbout_triggered(self):
        dialog = QDialog(self)

        textBrowser = QTextBrowser(dialog)
        textBrowser.setSource(QUrl("./resources/AboutWidget.html"))
        textBrowser.setOpenExternalLinks(True)

        # add a layout to store QTextBrowser
        layout = QGridLayout(dialog)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(textBrowser)

        dialog.setWindowTitle("About")
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, on=False)

        dialog.resize(600, 480)
        dialog.setMinimumSize(600, 480)
        dialog.setMaximumSize(600, 480)
        dialog.show()
        dialog.exec_()

    @Slot()
    def colorChanged(self, color):
        self.__pen.setColor(color)

    @Slot(int)
    def on_penSizeSlider_valueChanged(self, size):
        # magic
        self.__mainToolBarWidgets[2].setValue(size)
        self.__pen.setWidth(size)

    @Slot(int)
    def on_penSizeSpinBox_valueChanged(self, size):
        if self.focusWidget() is self.sender():
            # magic
            self.__mainToolBarWidgets[1].setValue(size)

    @Slot()
    def on_menuImageSize_triggered(self):
        dialog = ImageSizeDialog(self, self.__tabWidget.currCanvas)
        dialog.exec_()

    @Slot()
    def on_menuCanvasSize_triggered(self):
        dialog = CanvasSizeDialog(self, self.__tabWidget.currCanvas)
        dialog.exec_()

    @Slot()
    def closeEvent(self, event):
        allSaved = True
        for canvas in self.__tabWidget.canvases:
            if not canvas.isSaved:
                allSaved = False
                break

        if not allSaved:
            button = QMessageBox.warning(self,
                                         "Save changes?",
                                         "There are files that have been modified, save changes?",
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
