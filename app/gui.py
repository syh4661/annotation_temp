import time

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .progress import long_operation
# from .ui.appgui import Ui_MainWindow
from .ui.maingui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_thebutton.pressed.connect(self.button_press)

    def button_press(self):
        # text = self.operation()
        text = "hello world"

        QMessageBox.information(self, "Message Box", text)

    # @long_operation("Calculation")
    # def operation(self):
    #     return self.app.calculation(3)

    def get_label(self):
        return self.rgb_frame, self.depth_frame
