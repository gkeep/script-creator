# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowyRZEht.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(710, 210))
        MainWindow.setMaximumSize(QSize(710, 210))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ekd_ca_layout = QHBoxLayout()
        self.ekd_ca_layout.setObjectName(u"ekd_ca_layout")
        self.checkBox_ca = QCheckBox(self.centralwidget)
        self.checkBox_ca.setObjectName(u"checkBox_ca")

        self.ekd_ca_layout.addWidget(self.checkBox_ca)

        self.scriptInputButton_ca = QPushButton(self.centralwidget)
        self.scriptInputButton_ca.setObjectName(u"scriptInputButton_ca")
        self.scriptInputButton_ca.setEnabled(False)

        self.ekd_ca_layout.addWidget(self.scriptInputButton_ca)


        self.verticalLayout.addLayout(self.ekd_ca_layout)

        self.ekd_ekd_layout = QHBoxLayout()
        self.ekd_ekd_layout.setObjectName(u"ekd_ekd_layout")
        self.checkBox_ekd = QCheckBox(self.centralwidget)
        self.checkBox_ekd.setObjectName(u"checkBox_ekd")

        self.ekd_ekd_layout.addWidget(self.checkBox_ekd)

        self.scriptInputButton_ekd = QPushButton(self.centralwidget)
        self.scriptInputButton_ekd.setObjectName(u"scriptInputButton_ekd")
        self.scriptInputButton_ekd.setEnabled(False)

        self.ekd_ekd_layout.addWidget(self.scriptInputButton_ekd)


        self.verticalLayout.addLayout(self.ekd_ekd_layout)

        self.ekd_id_layout = QHBoxLayout()
        self.ekd_id_layout.setObjectName(u"ekd_id_layout")
        self.checkBox_id = QCheckBox(self.centralwidget)
        self.checkBox_id.setObjectName(u"checkBox_id")

        self.ekd_id_layout.addWidget(self.checkBox_id)

        self.scriptInputButton_id = QPushButton(self.centralwidget)
        self.scriptInputButton_id.setObjectName(u"scriptInputButton_id")
        self.scriptInputButton_id.setEnabled(False)

        self.ekd_id_layout.addWidget(self.scriptInputButton_id)


        self.verticalLayout.addLayout(self.ekd_id_layout)

        self.ekd_file_layout = QHBoxLayout()
        self.ekd_file_layout.setObjectName(u"ekd_file_layout")
        self.checkBox_file = QCheckBox(self.centralwidget)
        self.checkBox_file.setObjectName(u"checkBox_file")

        self.ekd_file_layout.addWidget(self.checkBox_file)

        self.scriptInputButton_file = QPushButton(self.centralwidget)
        self.scriptInputButton_file.setObjectName(u"scriptInputButton_file")
        self.scriptInputButton_file.setEnabled(False)

        self.ekd_file_layout.addWidget(self.scriptInputButton_file)


        self.verticalLayout.addLayout(self.ekd_file_layout)

        self.ekd_file_proc_layout = QHBoxLayout()
        self.ekd_file_proc_layout.setObjectName(u"ekd_file_proc_layout")
        self.checkBox_file_proc = QCheckBox(self.centralwidget)
        self.checkBox_file_proc.setObjectName(u"checkBox_file_proc")

        self.ekd_file_proc_layout.addWidget(self.checkBox_file_proc)

        self.scriptInputButton_file_proc = QPushButton(self.centralwidget)
        self.scriptInputButton_file_proc.setObjectName(u"scriptInputButton_file_proc")
        self.scriptInputButton_file_proc.setEnabled(False)

        self.ekd_file_proc_layout.addWidget(self.scriptInputButton_file_proc)


        self.verticalLayout.addLayout(self.ekd_file_proc_layout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ekd_ftp_layout = QHBoxLayout()
        self.ekd_ftp_layout.setObjectName(u"ekd_ftp_layout")
        self.checkBox_ftp = QCheckBox(self.centralwidget)
        self.checkBox_ftp.setObjectName(u"checkBox_ftp")

        self.ekd_ftp_layout.addWidget(self.checkBox_ftp)

        self.scriptInputButton_ftp = QPushButton(self.centralwidget)
        self.scriptInputButton_ftp.setObjectName(u"scriptInputButton_ftp")
        self.scriptInputButton_ftp.setEnabled(False)

        self.ekd_ftp_layout.addWidget(self.scriptInputButton_ftp)


        self.verticalLayout_2.addLayout(self.ekd_ftp_layout)

        self.ekd_notification_layout = QHBoxLayout()
        self.ekd_notification_layout.setObjectName(u"ekd_notification_layout")
        self.checkBox_notification = QCheckBox(self.centralwidget)
        self.checkBox_notification.setObjectName(u"checkBox_notification")

        self.ekd_notification_layout.addWidget(self.checkBox_notification)

        self.scriptInputButton_notification = QPushButton(self.centralwidget)
        self.scriptInputButton_notification.setObjectName(u"scriptInputButton_notification")
        self.scriptInputButton_notification.setEnabled(False)

        self.ekd_notification_layout.addWidget(self.scriptInputButton_notification)


        self.verticalLayout_2.addLayout(self.ekd_notification_layout)

        self.ekd_request_logger_layout = QHBoxLayout()
        self.ekd_request_logger_layout.setObjectName(u"ekd_request_logger_layout")
        self.checkBox_req = QCheckBox(self.centralwidget)
        self.checkBox_req.setObjectName(u"checkBox_req")

        self.ekd_request_logger_layout.addWidget(self.checkBox_req)

        self.scriptInputButton_req = QPushButton(self.centralwidget)
        self.scriptInputButton_req.setObjectName(u"scriptInputButton_req")
        self.scriptInputButton_req.setEnabled(False)

        self.ekd_request_logger_layout.addWidget(self.scriptInputButton_req)


        self.verticalLayout_2.addLayout(self.ekd_request_logger_layout)

        self.ekd_session_layout = QHBoxLayout()
        self.ekd_session_layout.setObjectName(u"ekd_session_layout")
        self.checkBox_session = QCheckBox(self.centralwidget)
        self.checkBox_session.setObjectName(u"checkBox_session")

        self.ekd_session_layout.addWidget(self.checkBox_session)

        self.scriptInputButton_session = QPushButton(self.centralwidget)
        self.scriptInputButton_session.setObjectName(u"scriptInputButton_session")
        self.scriptInputButton_session.setEnabled(False)

        self.ekd_session_layout.addWidget(self.scriptInputButton_session)


        self.verticalLayout_2.addLayout(self.ekd_session_layout)

        self.ekd_metadata_layout = QHBoxLayout()
        self.ekd_metadata_layout.setObjectName(u"ekd_metadata_layout")
        self.checkBox_metadata = QCheckBox(self.centralwidget)
        self.checkBox_metadata.setObjectName(u"checkBox_metadata")

        self.ekd_metadata_layout.addWidget(self.checkBox_metadata)

        self.scriptInputButton_metadata = QPushButton(self.centralwidget)
        self.scriptInputButton_metadata.setObjectName(u"scriptInputButton_metadata")
        self.scriptInputButton_metadata.setEnabled(False)

        self.ekd_metadata_layout.addWidget(self.scriptInputButton_metadata)


        self.verticalLayout_2.addLayout(self.ekd_metadata_layout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createScriptButton = QPushButton(self.centralwidget)
        self.createScriptButton.setObjectName(u"createScriptButton")

        self.horizontalLayout_2.addWidget(self.createScriptButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Script-creator", None))
        self.checkBox_ca.setText(QCoreApplication.translate("MainWindow", u"ekd_ca", None))
        self.scriptInputButton_ca.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_ekd.setText(QCoreApplication.translate("MainWindow", u"ekd_ekd", None))
        self.scriptInputButton_ekd.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_id.setText(QCoreApplication.translate("MainWindow", u"ekd_id", None))
        self.scriptInputButton_id.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_file.setText(QCoreApplication.translate("MainWindow", u"ekd_file", None))
        self.scriptInputButton_file.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_file_proc.setText(QCoreApplication.translate("MainWindow", u"ekd_file_processing", None))
        self.scriptInputButton_file_proc.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_ftp.setText(QCoreApplication.translate("MainWindow", u"ekd_ftp_uploader", None))
        self.scriptInputButton_ftp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_notification.setText(QCoreApplication.translate("MainWindow", u"ekd_notification", None))
        self.scriptInputButton_notification.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_req.setText(QCoreApplication.translate("MainWindow", u"ekd_request_logger", None))
        self.scriptInputButton_req.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_session.setText(QCoreApplication.translate("MainWindow", u"ekd_session", None))
        self.scriptInputButton_session.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.checkBox_metadata.setText(QCoreApplication.translate("MainWindow", u"ekd_metadata", None))
        self.scriptInputButton_metadata.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 SQL \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.createScriptButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u0440\u0430\u0442\u044c bash \u0441\u043a\u0440\u0438\u043f\u0442", None))
    # retranslateUi

