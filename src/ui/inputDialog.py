# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputDialogbMRcyi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_inDialog(object):
    def setupUi(self, inDialog):
        if not inDialog.objectName():
            inDialog.setObjectName(u"inDialog")
        inDialog.resize(800, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inDialog.sizePolicy().hasHeightForWidth())
        inDialog.setSizePolicy(sizePolicy)
        inDialog.setMinimumSize(QSize(800, 650))
        inDialog.setMaximumSize(QSize(800, 650))
        self.verticalLayout_2 = QVBoxLayout(inDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(inDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        self.textEdit.setFont(font)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveButton = QPushButton(inDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(inDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(inDialog)

        QMetaObject.connectSlotsByName(inDialog)
    # setupUi

    def retranslateUi(self, inDialog):
        inDialog.setWindowTitle(QCoreApplication.translate("inDialog", u"\u0412\u0432\u043e\u0434 SQL \u0441\u043a\u0440\u0438\u043f\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("inDialog", u"db_name", None))
        self.saveButton.setText(QCoreApplication.translate("inDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("inDialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

