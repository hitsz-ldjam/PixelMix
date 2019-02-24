# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateImageDialog.ui',
# licensing of 'CreateImageDialog.ui' applies.
#
# Created: Sun Feb 24 13:12:19 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CreateImageDialog(object):
    def setupUi(self, CreateImageDialog):
        CreateImageDialog.setObjectName("CreateImageDialog")
        CreateImageDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CreateImageDialog.resize(500, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateImageDialog.sizePolicy().hasHeightForWidth())
        CreateImageDialog.setSizePolicy(sizePolicy)
        CreateImageDialog.setMinimumSize(QtCore.QSize(500, 160))
        CreateImageDialog.setMaximumSize(QtCore.QSize(500, 160))
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateImageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CreateImageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fileNameLine = QtWidgets.QLineEdit(CreateImageDialog)
        self.fileNameLine.setObjectName("fileNameLine")
        self.horizontalLayout.addWidget(self.fileNameLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CreateImageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.widthBox = QtWidgets.QSpinBox(CreateImageDialog)
        self.widthBox.setMinimum(1)
        self.widthBox.setMaximum(16777215)
        self.widthBox.setProperty("value", 600)
        self.widthBox.setObjectName("widthBox")
        self.horizontalLayout_2.addWidget(self.widthBox)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(CreateImageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.heightBox = QtWidgets.QSpinBox(CreateImageDialog)
        self.heightBox.setMinimum(1)
        self.heightBox.setMaximum(16777215)
        self.heightBox.setProperty("value", 480)
        self.heightBox.setObjectName("heightBox")
        self.horizontalLayout_2.addWidget(self.heightBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateImageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreateImageDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateImageDialog)

    def retranslateUi(self, CreateImageDialog):
        CreateImageDialog.setWindowTitle(QtWidgets.QApplication.translate("CreateImageDialog", "New file", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CreateImageDialog", "File name", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CreateImageDialog", "Width", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CreateImageDialog", "Height", None, -1))

