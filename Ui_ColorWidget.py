# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColorWidget.ui',
# licensing of 'ColorWidget.ui' applies.
#
# Created: Mon Jan 21 17:10:13 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ColorWidget(object):
    def setupUi(self, ColorWidget):
        ColorWidget.setObjectName("ColorWidget")
        ColorWidget.resize(866, 502)
        self.verticalLayoutWidget = QtWidgets.QWidget(ColorWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 10, 71, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.H = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.H.setObjectName("H")
        self.verticalLayout.addWidget(self.H)
        self.S = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.S.setObjectName("S")
        self.verticalLayout.addWidget(self.S)
        self.V = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.V.setObjectName("V")
        self.verticalLayout.addWidget(self.V)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.R = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.R.setObjectName("R")
        self.verticalLayout.addWidget(self.R)
        self.G = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.G.setObjectName("G")
        self.verticalLayout.addWidget(self.G)
        self.B = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.B.setObjectName("B")
        self.verticalLayout.addWidget(self.B)
        self.colorRect = QtWidgets.QWidget(ColorWidget)
        self.colorRect.setGeometry(QtCore.QRect(11, 11, 260, 260))
        self.colorRect.setObjectName("colorRect")
        self.hueSlider = QtWidgets.QSlider(ColorWidget)
        self.hueSlider.setGeometry(QtCore.QRect(278, 11, 22, 260))
        self.hueSlider.setMaximum(359)
        self.hueSlider.setProperty("value", 0)
        self.hueSlider.setSliderPosition(0)
        self.hueSlider.setOrientation(QtCore.Qt.Vertical)
        self.hueSlider.setObjectName("hueSlider")

        self.retranslateUi(ColorWidget)
        QtCore.QMetaObject.connectSlotsByName(ColorWidget)

    def retranslateUi(self, ColorWidget):
        ColorWidget.setWindowTitle(QtWidgets.QApplication.translate("ColorWidget", "Form", None, -1))
        self.H.setText(QtWidgets.QApplication.translate("ColorWidget", "H :", None, -1))
        self.S.setText(QtWidgets.QApplication.translate("ColorWidget", "S :", None, -1))
        self.V.setText(QtWidgets.QApplication.translate("ColorWidget", "V :", None, -1))
        self.R.setText(QtWidgets.QApplication.translate("ColorWidget", "R :", None, -1))
        self.G.setText(QtWidgets.QApplication.translate("ColorWidget", "G :", None, -1))
        self.B.setText(QtWidgets.QApplication.translate("ColorWidget", "B :", None, -1))

