import os.path
import time
from calendar import timegm

import requests
from PySide6 import QtWidgets, QtUiTools
from PySide6.QtWidgets import QDialog
from markdown import markdown

from constructor import Constructor

Ui_MainWindow, QMainWindowBase = QtUiTools.loadUiType("src/ui/mainWindow.ui")
Ui_inDialog, QInputDialogBase = QtUiTools.loadUiType("src/ui/inputDialog.ui")
Ui_outDialog, QOutputDialogBase = QtUiTools.loadUiType("src/ui/outputWindow.ui")
Ui_updateDialog, QUpdateDialogBase = QtUiTools.loadUiType("src/ui/updateDialog.ui")


def toggle_button(state, button):
    if state:
        button.setEnabled(True)
        return
    button.setEnabled(False)


class UIMain(QtWidgets.QMainWindow, Ui_MainWindow):
    data = {}

    def __init__(self, main_window):
        self.__check_for_updates()

        super().__init__()
        self.setupUi(main_window)

        # bind all buttons to checkboxes
        self.checkBox_ca.stateChanged.connect(
            lambda: toggle_button(self.checkBox_ca.isChecked(), self.scriptInputButton_ca))
        self.checkBox_ekd.stateChanged.connect(
            lambda: toggle_button(self.checkBox_ekd.isChecked(), self.scriptInputButton_ekd))
        self.checkBox_id.stateChanged.connect(
            lambda: toggle_button(self.checkBox_id.isChecked(), self.scriptInputButton_id))
        self.checkBox_file.stateChanged.connect(
            lambda: toggle_button(self.checkBox_file.isChecked(), self.scriptInputButton_file))
        self.checkBox_file_proc.stateChanged.connect(
            lambda: toggle_button(self.checkBox_file_proc.isChecked(), self.scriptInputButton_file_proc))
        self.checkBox_ftp.stateChanged.connect(
            lambda: toggle_button(self.checkBox_ftp.isChecked(), self.scriptInputButton_ftp))
        self.checkBox_notification.stateChanged.connect(
            lambda: toggle_button(self.checkBox_notification.isChecked(), self.scriptInputButton_notification))
        self.checkBox_req.stateChanged.connect(
            lambda: toggle_button(self.checkBox_req.isChecked(), self.scriptInputButton_req))
        self.checkBox_session.stateChanged.connect(
            lambda: toggle_button(self.checkBox_session.isChecked(), self.scriptInputButton_session))
        self.checkBox_metadata.stateChanged.connect(
            lambda: toggle_button(self.checkBox_metadata.isChecked(), self.scriptInputButton_metadata))

        self.scriptInputButton_ca.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_ca", data=self.data))
        self.scriptInputButton_ekd.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_ekd", data=self.data))
        self.scriptInputButton_id.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_id", data=self.data))
        self.scriptInputButton_file.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_file", data=self.data))
        self.scriptInputButton_file_proc.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_file_processing", data=self.data))
        self.scriptInputButton_ftp.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_ftp_uploader", data=self.data))
        self.scriptInputButton_notification.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_notification", data=self.data))
        self.scriptInputButton_req.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_request_logger", data=self.data))
        self.scriptInputButton_session.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_session", data=self.data))
        self.scriptInputButton_metadata.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_metadata", data=self.data))

        self.createScriptButton.clicked.connect(lambda: self.__open_output_dialog(self.data))

    def open_input_dialog(self, db_name, data):
        dialog = QDialog()
        dl = InputDialog(dialog, db_name, data)
        dialog.show()
        dialog.exec()

        new_data: dict = dl.get_data()
        for key, val in new_data.items():
            body = val[0].replace('$', '\\$').replace('"', '\\\"')  # screening
            outfile = val[1]

            self.data[key] = {
                "body": body,
                "outfile": outfile
            }

    @staticmethod
    def __check_for_updates():
        response = requests.get("https://api.github.com/repos/gkeep/script-creator/releases/latest").json()

        new_publish_date = timegm(time.strptime(response["published_at"], "%Y-%m-%dT%H:%M:%SZ"))
        mod_date = os.path.getctime(os.path.abspath(__file__ + "/.."))

        is_new_version_available = new_publish_date > mod_date
        if is_new_version_available:
            dialog = QDialog()
            UpdateDialog(dialog, response["name"], time.ctime(new_publish_date), response["body"])
            dialog.show()
            dialog.exec()

    def __open_output_dialog(self, data):
        dialog = QDialog()

        enabled_tables = []

        if self.checkBox_ca.isChecked(): enabled_tables.append("ekd_ca")
        if self.checkBox_ekd.isChecked(): enabled_tables.append("ekd_ekd")
        if self.checkBox_id.isChecked(): enabled_tables.append("ekd_id")
        if self.checkBox_file.isChecked(): enabled_tables.append("ekd_file")
        if self.checkBox_file_proc.isChecked(): enabled_tables.append("ekd_file_processing")
        if self.checkBox_ftp.isChecked(): enabled_tables.append("ekd_ftp_uploader")
        if self.checkBox_notification.isChecked(): enabled_tables.append("ekd_notification")
        if self.checkBox_req.isChecked(): enabled_tables.append("ekd_request_logger")
        if self.checkBox_session.isChecked(): enabled_tables.append("ekd_session")
        if self.checkBox_metadata.isChecked(): enabled_tables.append("ekd_metadata")

        new_data = data.copy()
        keys = data.keys()
        for key in keys:
            if key not in enabled_tables:
                new_data.pop(key)
        data = new_data
        del new_data

        OutputDialog(dialog, data)
        dialog.show()
        dialog.exec_()


class InputDialog(Ui_inDialog):
    def __init__(self, window, db, data):
        super().__init__()
        self.setupUi(window)

        self.groupBox.setTitle(db)
        self.textEdit.setStyleSheet("font-family: 'Monaco', 'Ubuntu Mono', 'Courier New', monospace;")
        self.data = data
        self.window = window

        self.saveButton.clicked.connect(lambda: self.__save_data(db))
        self.cancelButton.clicked.connect(lambda: self.window.close())
        self.outputToFile.clicked.connect(lambda: self.toggle_output_to_file())

    def get_data(self) -> {}:
        return self.data

    def toggle_output_to_file(self):
        if self.outputToFile.isChecked():
            self.outputFileName.setEnabled(True)

    def __save_data(self, db_name):
        outfile = self.outputFileName.text()
        if self.data != "":
            self.data = {
                db_name: [self.textEdit.toPlainText(), outfile]
            }

        self.window.close()


class OutputDialog(Ui_outDialog):
    def __init__(self, window, data):
        super().__init__()
        self.setupUi(window)

        cst = Constructor()
        out = cst.make_script(sql_scripts=data)

        self.outputTextEdit.setStyleSheet("font-family: 'Monaco', 'Ubuntu Mono', 'Courier New', monospace;")
        self.outputTextEdit.setText(out)

        self.saveButton.clicked.connect(lambda: self.__save_file())

    def __save_file(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Сохранить скрипт",
                                                            filter='Bash скрипт (*.sh)')
        if ".sh" not in filename: filename += ".sh"
        if filename:
            with open(filename, 'w') as file:
                file.write(self.outputTextEdit.toPlainText())


class UpdateDialog(Ui_updateDialog):
    def __init__(self, window, version, v_time, body):
        super().__init__()
        self.setupUi(window)

        formatted_body = markdown(body)

        self.textBrowser.setHtml(f"<b>Доступно новое обновление - {version} ({v_time})</b><br>"
                                    f"<br>{formatted_body}<br><br>"
                                    f"Скачать можно по <a href='https://github.com/gkeep/script-creator/releases/latest'>ссылке</a> (GitHub)")
