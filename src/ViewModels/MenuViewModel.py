
from ViewModels.ViewModel import ViewModel

"""
ViewModel with main menu in application.
"""
class MenuViewModel(ViewModel):
    def __init__(self, navigator):
        super().__init__(navigator)

    """
    switchs view via navigator.
    """
    def navigate_to_exercises(self):
        self.navigate_to("Exercises")

    """
    switchs view via navigator.
    """
    def navigate_to_settings(self):
        self.navigate_to("Settings")
