import sys

from ui_helper import UIMain
from PySide2.QtWidgets import QMainWindow, QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    content = UIMain(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
