# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'outputWindowzDgfVE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_outDialog(object):
    def setupUi(self, outDialog):
        if not outDialog.objectName():
            outDialog.setObjectName(u"outDialog")
        outDialog.resize(850, 600)
        self.verticalLayout_2 = QVBoxLayout(outDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(outDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.outputTextEdit = QTextEdit(self.groupBox)
        self.outputTextEdit.setObjectName(u"outputTextEdit")
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        self.outputTextEdit.setFont(font)
        self.outputTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.outputTextEdit)

        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(outDialog)

        QMetaObject.connectSlotsByName(outDialog)
    # setupUi

    def retranslateUi(self, outDialog):
        outDialog.setWindowTitle(QCoreApplication.translate("outDialog", u"Bash \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.groupBox.setTitle("")
        self.saveButton.setText(QCoreApplication.translate("outDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

