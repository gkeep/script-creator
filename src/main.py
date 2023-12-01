import sys

from ui_helper import UIMain
from PySide2.QtWidgets import QMainWindow, QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if len(sys.argv) > 1:
        db = sys.argv[1]
        script_path = sys.argv[2]

        from constructor import Constructor
        cstr = Constructor()

        cstr.build_specific(db, script_path)
        sys.exit()

    MainWindow = QMainWindow()
    content = UIMain(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())