from PyQt6 import uic

from Views.View import View
from ViewModels.MenuViewModel import MenuViewModel

"""
View with main menu.
"""
class MenuView(View):
    def __init__(self, navigator):
        view_model = MenuViewModel(navigator)
        super().__init__(view_model)

        uic.loadUi("src/views/MenuView.ui", self)

        self.go_to_exercises_button.clicked.connect(view_model.navigate_to_exercises)
        self.go_to_settings_button.clicked.connect(view_model.navigate_to_settings)
