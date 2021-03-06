# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\MainWindow.ui',
# licensing of '.\resources\MainWindow.ui' applies.
#
# Created: Tue Feb 26 19:57:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEffects = QtWidgets.QMenu(self.menubar)
        self.menuEffects.setObjectName("menuEffects")
        self.menuColor_Correction = QtWidgets.QMenu(self.menuEffects)
        self.menuColor_Correction.setObjectName("menuColor_Correction")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setMinimumSize(QtCore.QSize(30, 30))
        self.mainToolBar.setStyleSheet("")
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.sideToolBar = QtWidgets.QToolBar(MainWindow)
        self.sideToolBar.setMinimumSize(QtCore.QSize(30, 30))
        self.sideToolBar.setStyleSheet("")
        self.sideToolBar.setObjectName("sideToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.sideToolBar)
        self.menuFileCreate = QtWidgets.QAction(MainWindow)
        self.menuFileCreate.setObjectName("menuFileCreate")
        self.menuFileOpen = QtWidgets.QAction(MainWindow)
        self.menuFileOpen.setObjectName("menuFileOpen")
        self.menuFileSave = QtWidgets.QAction(MainWindow)
        self.menuFileSave.setObjectName("menuFileSave")
        self.menuFileSaveAs = QtWidgets.QAction(MainWindow)
        self.menuFileSaveAs.setObjectName("menuFileSaveAs")
        self.menuFileQuit = QtWidgets.QAction(MainWindow)
        self.menuFileQuit.setObjectName("menuFileQuit")
        self.menuHelpAbout = QtWidgets.QAction(MainWindow)
        self.menuHelpAbout.setCheckable(False)
        self.menuHelpAbout.setObjectName("menuHelpAbout")
        self.menuEditPreferences = QtWidgets.QAction(MainWindow)
        self.menuEditPreferences.setObjectName("menuEditPreferences")
        self.menuEffectBrightnessContrast = QtWidgets.QAction(MainWindow)
        self.menuEffectBrightnessContrast.setObjectName("menuEffectBrightnessContrast")
        self.menuImageSize = QtWidgets.QAction(MainWindow)
        self.menuImageSize.setObjectName("menuImageSize")
        self.menuCanvasSize = QtWidgets.QAction(MainWindow)
        self.menuCanvasSize.setObjectName("menuCanvasSize")
        self.menuFile.addAction(self.menuFileCreate)
        self.menuFile.addAction(self.menuFileOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFileSave)
        self.menuFile.addAction(self.menuFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFileQuit)
        self.menuEdit.addAction(self.menuEditPreferences)
        self.menuHelp.addAction(self.menuHelpAbout)
        self.menuColor_Correction.addAction(self.menuEffectBrightnessContrast)
        self.menuEffects.addAction(self.menuColor_Correction.menuAction())
        self.menuImage.addAction(self.menuImageSize)
        self.menuImage.addAction(self.menuCanvasSize)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuEffects.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Pixel Sketch", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuEffects.setTitle(QtWidgets.QApplication.translate("MainWindow", "Effect", None, -1))
        self.menuColor_Correction.setTitle(QtWidgets.QApplication.translate("MainWindow", "Color Correction", None, -1))
        self.menuImage.setTitle(QtWidgets.QApplication.translate("MainWindow", "Image", None, -1))
        self.mainToolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "main tool bar", None, -1))
        self.sideToolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "side tool bar", None, -1))
        self.menuFileCreate.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.menuFileCreate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.menuFileCreate.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.menuFileOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.menuFileOpen.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.menuFileOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.menuFileSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.menuFileSave.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.menuFileSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.menuFileSaveAs.setText(QtWidgets.QApplication.translate("MainWindow", "Save as ...", None, -1))
        self.menuFileSaveAs.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.menuFileQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.menuFileQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.menuHelpAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.menuEditPreferences.setText(QtWidgets.QApplication.translate("MainWindow", "Preferences", None, -1))
        self.menuEditPreferences.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Alt+;", None, -1))
        self.menuEffectBrightnessContrast.setText(QtWidgets.QApplication.translate("MainWindow", "Brightness && Contrast", None, -1))
        self.menuImageSize.setText(QtWidgets.QApplication.translate("MainWindow", "Image Size", None, -1))
        self.menuImageSize.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Alt+I", None, -1))
        self.menuCanvasSize.setText(QtWidgets.QApplication.translate("MainWindow", "Canvas Size", None, -1))
        self.menuCanvasSize.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Alt+C", None, -1))

