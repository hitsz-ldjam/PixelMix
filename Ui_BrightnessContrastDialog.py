# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\BrightnessContrastDialog.ui',
# licensing of '.\resources\BrightnessContrastDialog.ui' applies.
#
# Created: Sun Feb 17 23:58:22 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BrightnessContrastDialog(object):
    def setupUi(self, BrightnessContrastDialog):
        BrightnessContrastDialog.setObjectName("BrightnessContrastDialog")
        BrightnessContrastDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        BrightnessContrastDialog.resize(500, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BrightnessContrastDialog.sizePolicy().hasHeightForWidth())
        BrightnessContrastDialog.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(BrightnessContrastDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(19)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(BrightnessContrastDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.brightnessSpinBox = QtWidgets.QSpinBox(BrightnessContrastDialog)
        self.brightnessSpinBox.setMinimum(-100)
        self.brightnessSpinBox.setMaximum(100)
        self.brightnessSpinBox.setObjectName("brightnessSpinBox")
        self.gridLayout.addWidget(self.brightnessSpinBox, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(BrightnessContrastDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.contrastSlider = QtWidgets.QSlider(BrightnessContrastDialog)
        self.contrastSlider.setMinimum(-100)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.gridLayout.addWidget(self.contrastSlider, 1, 1, 1, 1)
        self.contrastSpinBox = QtWidgets.QSpinBox(BrightnessContrastDialog)
        self.contrastSpinBox.setMinimum(-100)
        self.contrastSpinBox.setMaximum(100)
        self.contrastSpinBox.setObjectName("contrastSpinBox")
        self.gridLayout.addWidget(self.contrastSpinBox, 1, 2, 1, 1)
        self.brightnessSlider = QtWidgets.QSlider(BrightnessContrastDialog)
        self.brightnessSlider.setMinimum(-100)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.gridLayout.addWidget(self.brightnessSlider, 0, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(BrightnessContrastDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Discard)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(BrightnessContrastDialog)
        QtCore.QMetaObject.connectSlotsByName(BrightnessContrastDialog)

    def retranslateUi(self, BrightnessContrastDialog):
        BrightnessContrastDialog.setWindowTitle(QtWidgets.QApplication.translate("BrightnessContrastDialog", "Brightness & Contrast", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("BrightnessContrastDialog", "Contrast", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("BrightnessContrastDialog", "Brightness", None, -1))

