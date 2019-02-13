# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColorWidget.ui',
# licensing of 'ColorWidget.ui' applies.
#
# Created: Wed Feb 13 12:27:07 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ColorWidget(object):
    def setupUi(self, ColorWidget):
        ColorWidget.setObjectName("ColorWidget")
        ColorWidget.resize(866, 502)
        self.colorRect = QtWidgets.QWidget(ColorWidget)
        self.colorRect.setGeometry(QtCore.QRect(11, 11, 230, 230))
        self.colorRect.setObjectName("colorRect")
        self.hueSlider = QtWidgets.QSlider(ColorWidget)
        self.hueSlider.setGeometry(QtCore.QRect(250, 11, 22, 230))
        self.hueSlider.setMaximum(359)
        self.hueSlider.setProperty("value", 0)
        self.hueSlider.setSliderPosition(0)
        self.hueSlider.setOrientation(QtCore.Qt.Vertical)
        self.hueSlider.setObjectName("hueSlider")
        self.gridLayoutWidget = QtWidgets.QWidget(ColorWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 10, 101, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.G = QtWidgets.QLabel(self.gridLayoutWidget)
        self.G.setObjectName("G")
        self.gridLayout.addWidget(self.G, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.V = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V.setObjectName("V")
        self.gridLayout.addWidget(self.V, 2, 0, 1, 1)
        self.B = QtWidgets.QLabel(self.gridLayoutWidget)
        self.B.setObjectName("B")
        self.gridLayout.addWidget(self.B, 6, 0, 1, 1)
        self.H = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H.setObjectName("H")
        self.gridLayout.addWidget(self.H, 0, 0, 1, 1)
        self.R = QtWidgets.QLabel(self.gridLayoutWidget)
        self.R.setObjectName("R")
        self.gridLayout.addWidget(self.R, 4, 0, 1, 1)
        self.S = QtWidgets.QLabel(self.gridLayoutWidget)
        self.S.setObjectName("S")
        self.gridLayout.addWidget(self.S, 1, 0, 1, 1)
        self.hSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.hSpinBox.setMaximum(359)
        self.hSpinBox.setObjectName("hSpinBox")
        self.gridLayout.addWidget(self.hSpinBox, 0, 1, 1, 1)
        self.sSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sSpinBox.setMaximum(100)
        self.sSpinBox.setObjectName("sSpinBox")
        self.gridLayout.addWidget(self.sSpinBox, 1, 1, 1, 1)
        self.vSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.vSpinBox.setMaximum(100)
        self.vSpinBox.setObjectName("vSpinBox")
        self.gridLayout.addWidget(self.vSpinBox, 2, 1, 1, 1)
        self.rSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.rSpinBox.setMaximum(255)
        self.rSpinBox.setObjectName("rSpinBox")
        self.gridLayout.addWidget(self.rSpinBox, 4, 1, 1, 1)
        self.gSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.gSpinBox.setMaximum(255)
        self.gSpinBox.setObjectName("gSpinBox")
        self.gridLayout.addWidget(self.gSpinBox, 5, 1, 1, 1)
        self.bSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.bSpinBox.setMaximum(255)
        self.bSpinBox.setObjectName("bSpinBox")
        self.gridLayout.addWidget(self.bSpinBox, 6, 1, 1, 1)

        self.retranslateUi(ColorWidget)
        QtCore.QMetaObject.connectSlotsByName(ColorWidget)

    def retranslateUi(self, ColorWidget):
        ColorWidget.setWindowTitle(QtWidgets.QApplication.translate("ColorWidget", "Form", None, -1))
        self.G.setText(QtWidgets.QApplication.translate("ColorWidget", "G :", None, -1))
        self.V.setText(QtWidgets.QApplication.translate("ColorWidget", "V :", None, -1))
        self.B.setText(QtWidgets.QApplication.translate("ColorWidget", "B :", None, -1))
        self.H.setText(QtWidgets.QApplication.translate("ColorWidget", "H :", None, -1))
        self.R.setText(QtWidgets.QApplication.translate("ColorWidget", "R :", None, -1))
        self.S.setText(QtWidgets.QApplication.translate("ColorWidget", "S :", None, -1))

