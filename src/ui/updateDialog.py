# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerHHuhtT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_updateDialog(object):
    def setupUi(self, updateWidget):
        if not updateWidget.objectName():
            updateWidget.setObjectName(u"updateWidget")
        updateWidget.resize(500, 300)
        self.verticalLayout = QVBoxLayout(updateWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.updateTextBrowser = QTextBrowser(updateWidget)
        self.updateTextBrowser.setObjectName(u"updateTextEdit")
        self.updateTextBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.updateTextBrowser)


        self.retranslateUi(updateWidget)

        QMetaObject.connectSlotsByName(updateWidget)
    # setupUi

    def retranslateUi(self, updateWidget):
        updateWidget.setWindowTitle(QCoreApplication.translate("updateWidget", u"Доступно обновление!", None))
    # retranslateUi

