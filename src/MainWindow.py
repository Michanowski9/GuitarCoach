from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6 import QtGui

from Navigator import Navigator

"""
The class that holds a reference to the main part of the application and navigator. Also is used as main window.
stacked_widget is holding all used views.
"""
class MainWindow(QMainWindow):
    _instance = None
    def __init__(self):
        super().__init__()

        # singleton
        if self._instance is not None:
            raise Exception("An instance of this class already exists")
        self._instance = self

        self.setWindowIcon(QtGui.QIcon('resources/Icon.png'))
        self.setWindowTitle("Guitar Coach")
        self.resize(800,600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.navigator = Navigator(self.stacked_widget)

        self.navigator.navigate("Menu")

        self.show()