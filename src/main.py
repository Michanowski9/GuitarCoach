import sys

from PyQt6.QtWidgets import QApplication

from gui.MainWindow import MainWindow

def main():
    app = QApplication([])
    mainWindow = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()