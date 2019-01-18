from Painter import *

# main window UI
from Ui_MainWindow import Ui_MainWindow

g_defaultWindowBackColor = QColor(150, 150, 150)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # hide default central widget
        self.takeCentralWidget().hide()
        self.setDockNestingEnabled(True)

        # move the main window to the center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # create a canvas list
        self.__canvases = []
        # create a tool dock list
        self.__toolDocks = []

        # add a default canvas
        self.addCanvas(300, 300, QImage.Format_RGB888, "Untitled")

        # test (add some tool docks)
        for i in range(4):
            self.addToolDock(Qt.RightDockWidgetArea, "Tool_" + str(i + 1))

        self.setDockLayout()
        self.show()

    def addCanvas(self, width, height, imgFormat, title, color=QColor(255, 255, 255)):
        """
        add a canvas to main window
        each canvas includes an image and a dock widget
        """
        canvas = Canvas(width, height, imgFormat, self, title)
        canvas.image.fill(color)

        # set background color
        pal = QPalette(canvas.widget.palette())
        pal.setColor(QPalette.Background, g_defaultWindowBackColor)
        canvas.widget.setAutoFillBackground(True)
        canvas.widget.setPalette(pal)

        self.__canvases.append(canvas)
        return canvas

    def addToolDock(self, area, title):
        dock = QDockWidget(title)
        self.addDockWidget(area, dock)
        self.__toolDocks.append(dock)
        return dock

    def setDockLayout(self):
        self.setCentralWidget(self.__canvases[0].widget)

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
