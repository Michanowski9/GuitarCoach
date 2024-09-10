from PyQt6 import uic

from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

from Views.View import View
from ViewModels.SettingsViewModel import SettingsViewModel

"""
View with main settings of the application.
"""
class SettingsView(View):
    def __init__(self, navigator):
        view_model = SettingsViewModel(navigator)
        super().__init__(view_model)

        uic.loadUi("src/views/SettingsView.ui", self)

        self.go_to_menu_button.clicked.connect(view_model.navigate_to_menu)
        self.go_to_menu_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
