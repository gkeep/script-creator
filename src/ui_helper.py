from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

from ui.inputDialog import Ui_inDialog
from ui.mainWindow import Ui_MainWindow
from ui.outputWindow import Ui_outDialog

from constructor import Constructor


def toggle_button(state, button):
    if state:
        button.setEnabled(True)
        return
    button.setEnabled(False)


class UIMain(Ui_MainWindow):
    data = {}

    def __init__(self, main_window):
        super().setupUi(main_window)

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
        self.checkBox_notification.stateChanged.connect(
            lambda: toggle_button(self.checkBox_notification.isChecked(), self.scriptInputButton_notification))
        self.checkBox_req.stateChanged.connect(
            lambda: toggle_button(self.checkBox_req.isChecked(), self.scriptInputButton_req))
        self.checkBox_metadata.stateChanged.connect(
            lambda: toggle_button(self.checkBox_metadata.isChecked(), self.scriptInputButton_metadata))
        self.checkBox_session.stateChanged.connect(
            lambda: toggle_button(self.checkBox_session.isChecked(), self.scriptInputButton_session))
        self.checkBox_repeat.stateChanged.connect(
            lambda: toggle_button(self.checkBox_repeat.isChecked(), self.scriptInputButton_repeat))
        self.checkBox_calendar.stateChanged.connect(
            lambda: toggle_button(self.checkBox_calendar.isChecked(), self.scriptInputButton_calendar))
        self.checkBox_chat.stateChanged.connect(
            lambda: toggle_button(self.checkBox_chat.isChecked(), self.scriptInputButton_chat))
        self.checkBox_showcase.stateChanged.connect(
            lambda: toggle_button(self.checkBox_showcase.isChecked(), self.scriptInputButton_showcase))

        self.scriptInputButton_ca.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_ca", data=self.data))
        self.scriptInputButton_ekd.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_ekd", data=self.data))
        self.scriptInputButton_id.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_id", data=self.data))
        self.scriptInputButton_file.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_file", data=self.data))
        self.scriptInputButton_file_proc.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_file_processing", data=self.data))
        self.scriptInputButton_notification.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_notification", data=self.data))
        self.scriptInputButton_req.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_request_logger", data=self.data))
        self.scriptInputButton_session.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_session", data=self.data))
        self.scriptInputButton_metadata.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_metadata", data=self.data))
        self.scriptInputButton_repeat.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_repeat_notification", data=self.data))
        self.scriptInputButton_calendar.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_calendar", data=self.data))
        self.scriptInputButton_chat.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_chat", data=self.data))
        self.scriptInputButton_showcase.clicked.connect(lambda: self.open_input_dialog(db_name="ekd_showcase", data=self.data))

        self.createScriptButton.clicked.connect(lambda: self.__open_output_dialog(self.data))

    def open_input_dialog(self, db_name, data):
        dialog = QDialog()
        dl = InputDialog(dialog, db_name, data)
        dialog.show()
        dialog.exec()

        new_data: dict = dl.get_data()
        for key, val in new_data.items():
            self.data[key] = {
                "body": val[0],
                "outfile": val[1],
                "separator": val[2]
            }

    def __open_output_dialog(self, data):
        dialog = QDialog()

        enabled_tables = []

        if self.checkBox_ca.isChecked(): enabled_tables.append("ekd_ca")
        if self.checkBox_ekd.isChecked(): enabled_tables.append("ekd_ekd")
        if self.checkBox_id.isChecked(): enabled_tables.append("ekd_id")
        if self.checkBox_file.isChecked(): enabled_tables.append("ekd_file")
        if self.checkBox_file_proc.isChecked(): enabled_tables.append("ekd_file_processing")
        if self.checkBox_notification.isChecked(): enabled_tables.append("ekd_notification")
        if self.checkBox_req.isChecked(): enabled_tables.append("ekd_request_logger")
        if self.checkBox_session.isChecked(): enabled_tables.append("ekd_session")
        if self.checkBox_metadata.isChecked(): enabled_tables.append("ekd_metadata")
        if self.checkBox_repeat.isChecked(): enabled_tables.append("ekd_repeat_notification")
        if self.checkBox_calendar.isChecked(): enabled_tables.append("ekd_calendar")
        if self.checkBox_chat.isChecked(): enabled_tables.append("ekd_chat")
        if self.checkBox_showcase.isChecked(): enabled_tables.append("ekd_showcase")

        new_data = data.copy()
        keys = data.keys()
        for key in keys:
            if key not in enabled_tables:
                new_data.pop(key)
        data = new_data
        del new_data

        OutputDialog(dialog, data)
        dialog.show()
        dialog.exec()


class InputDialog(Ui_inDialog):
    def __init__(self, window, db, data):
        super().setupUi(window)

        self.groupBox.setTitle(db)
        self.textEdit.setStyleSheet("font-family: 'Monaco', 'Ubuntu Mono', 'Courier New', monospace;")
        self.data = data
        self.window = window

        self.saveButton.clicked.connect(lambda: self.__save_data(db))
        self.cancelButton.clicked.connect(lambda: self.window.close())
        self.outputToFile.clicked.connect(lambda: self.toggle_output_to_file())

        if data != {} and db in data.keys():
            self.textEdit.setText(data[db]["body"])
            if data[db]["outfile"]:
                self.outputToFile.setChecked(True)
                self.outputFileName.setEnabled(True)
                self.outputFileName.setText(data[db]["outfile"])

    def get_data(self) -> {}:
        return self.data

    def toggle_output_to_file(self):
        if self.outputToFile.isChecked():
            self.outputFileName.setEnabled(True)
            self.separatorSelector.setEnabled(True)
            self.separatorSelector.setEnabled(True)

    def __save_data(self, db_name):
        outfile = self.outputFileName.text()
        if self.data != "":
            self.data = {
                db_name: [self.textEdit.toPlainText(), outfile, self.separatorSelector.currentIndex()],
            }

        self.window.close()


class OutputDialog(Ui_outDialog):
    def __init__(self, window, data):
        super().setupUi(window)

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
