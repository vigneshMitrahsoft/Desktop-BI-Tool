from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction

from project import Ui_MainWindow


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bi - Demo")