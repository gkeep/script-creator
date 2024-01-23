# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'outputWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_outDialog(object):
    def setupUi(self, outDialog):
        if not outDialog.objectName():
            outDialog.setObjectName(u"outDialog")
        outDialog.resize(1025, 600)
        outDialog.setMinimumSize(QSize(500, 300))
        outDialog.setMaximumSize(QSize(5000, 3000))
        self.verticalLayout_2 = QVBoxLayout(outDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(outDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.outputTextEdit = QTextEdit(self.groupBox)
        self.outputTextEdit.setObjectName(u"outputTextEdit")
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

