from PySide2 import QtGui
from PySide2.QtWidgets import QDialog

from ui.mainWindow import Ui_MainWindow
from ui.inputDialog import Ui_inDialog
from ui.outputDialog import Ui_outDialog
from constructor import Constructor


def toggle_button(state, button):
    if state:
        button.setEnabled(True)
        return
    button.setEnabled(False)


class UIMain(Ui_MainWindow):
    data = {}

    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

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
        dialog.exec_()

        new_data: dict = dl.get_data()
        for key, val in new_data.items():
            self.data[key] = val

    def __open_output_dialog(self, data):
        dialog = QDialog()
        OutputDialog(dialog, data)
        dialog.show()
        dialog.exec_()


class InputDialog(Ui_inDialog):
    def __init__(self, window, db, data):
        super().setupUi(window)
        self.groupBox.setTitle(db)
        self.data = data
        self.window = window

        self.saveButton.clicked.connect(lambda: self.__save_data(db))

    def get_data(self) -> {}:
        return self.data

    def __save_data(self, db_name):
        self.data = {
            db_name: self.textEdit.toPlainText()
        }
        self.window.close()


class OutputDialog(Ui_outDialog):
    def __init__(self, window, data):
        super().setupUi(window)

        cst = Constructor()
        out = cst.make_script(sql_scripts=data)

        self.outputTextEdit.setText(out)
