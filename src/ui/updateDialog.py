# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateDialogtYDckv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_updateDialog(object):
    def setupUi(self, updateDialog):
        if not updateDialog.objectName():
            updateDialog.setObjectName(u"updateDialog")
        updateDialog.resize(750, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(updateDialog.sizePolicy().hasHeightForWidth())
        updateDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(updateDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(updateDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.retranslateUi(updateDialog)

        QMetaObject.connectSlotsByName(updateDialog)
    # setupUi

    def retranslateUi(self, updateDialog):
        updateDialog.setWindowTitle(QCoreApplication.translate("updateDialog", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435!", None))
    # retranslateUi

