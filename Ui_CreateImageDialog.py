# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\CreateImageDialog.ui',
# licensing of '.\resources\CreateImageDialog.ui' applies.
#
# Created: Sun Feb 17 23:57:47 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CreateImageDialog(object):
    def setupUi(self, CreateImageDialog):
        CreateImageDialog.setObjectName("CreateImageDialog")
        CreateImageDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CreateImageDialog.resize(500, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateImageDialog.sizePolicy().hasHeightForWidth())
        CreateImageDialog.setSizePolicy(sizePolicy)
        CreateImageDialog.setMaximumSize(QtCore.QSize(500, 160))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CreateImageDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
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
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(CreateImageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.heightBox = QtWidgets.QSpinBox(CreateImageDialog)
        self.heightBox.setMinimum(1)
        self.heightBox.setMaximum(16777215)
        self.heightBox.setProperty("value", 480)
        self.heightBox.setObjectName("heightBox")
        self.horizontalLayout_3.addWidget(self.heightBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateImageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(CreateImageDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateImageDialog)

    def retranslateUi(self, CreateImageDialog):
        CreateImageDialog.setWindowTitle(QtWidgets.QApplication.translate("CreateImageDialog", "New file", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CreateImageDialog", "File name", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CreateImageDialog", "Width", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CreateImageDialog", "Height", None, -1))

