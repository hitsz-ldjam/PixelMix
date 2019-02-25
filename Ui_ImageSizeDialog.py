# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageSizeDialog.ui',
# licensing of 'ImageSizeDialog.ui' applies.
#
# Created: Mon Feb 25 21:43:12 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ImageSize(object):
    def setupUi(self, ImageSize):
        ImageSize.setObjectName("ImageSize")
        ImageSize.setWindowModality(QtCore.Qt.ApplicationModal)
        ImageSize.resize(510, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageSize.sizePolicy().hasHeightForWidth())
        ImageSize.setSizePolicy(sizePolicy)
        ImageSize.setMinimumSize(QtCore.QSize(510, 200))
        ImageSize.setMaximumSize(QtCore.QSize(510, 200))
        self.formLayout = QtWidgets.QFormLayout(ImageSize)
        self.formLayout.setObjectName("formLayout")
        self.originalSizeLabel = QtWidgets.QLabel(ImageSize)
        self.originalSizeLabel.setObjectName("originalSizeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.originalSizeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ImageSize)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widthSpinBox = QtWidgets.QSpinBox(ImageSize)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthSpinBox.sizePolicy().hasHeightForWidth())
        self.widthSpinBox.setSizePolicy(sizePolicy)
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(16777215)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.horizontalLayout.addWidget(self.widthSpinBox)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.lockAspect = QtWidgets.QRadioButton(ImageSize)
        self.lockAspect.setText("")
        self.lockAspect.setIconSize(QtCore.QSize(20, 20))
        self.lockAspect.setChecked(True)
        self.lockAspect.setObjectName("lockAspect")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lockAspect)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(ImageSize)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.heightSpinBox = QtWidgets.QSpinBox(ImageSize)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightSpinBox.sizePolicy().hasHeightForWidth())
        self.heightSpinBox.setSizePolicy(sizePolicy)
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(16777215)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.horizontalLayout_2.addWidget(self.heightSpinBox)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ImageSize)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Discard)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(ImageSize)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ImageSize.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ImageSize.reject)
        QtCore.QMetaObject.connectSlotsByName(ImageSize)

    def retranslateUi(self, ImageSize):
        ImageSize.setWindowTitle(QtWidgets.QApplication.translate("ImageSize", "Image Size", None, -1))
        self.originalSizeLabel.setText(QtWidgets.QApplication.translate("ImageSize", "Original Size:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ImageSize", "Width ", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ImageSize", "Height", None, -1))

