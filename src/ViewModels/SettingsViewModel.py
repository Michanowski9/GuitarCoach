
from ViewModels.ViewModel import ViewModel

"""
ViewModel with main settings in application.
"""
class SettingsViewModel(ViewModel):
    def __init__(self, navigator):
        super().__init__(navigator)

    def navigate_to_menu(self):
        self.navigate_to("Menu")
