from PyQt6.QtWidgets import QWidget

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Guitar Coach")
        self.resize(500,500)

        self.show()