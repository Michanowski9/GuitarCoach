
from ViewModels.ViewModel import ViewModel

"""
ViewModel with list off all loaded exercises.
"""
class ExercisesViewModel(ViewModel):
    def __init__(self, navigator):
        super().__init__(navigator)

    """
    function to go back to main menu.
    """
    def navigate_to_menu(self):
        self.navigate_to("Menu")

    """
    getter for exercises names list.
    """
    def get_exercises_names(self):
        result = []
        result.append("Exercise 1")
        result.append("Exercise 2")
        return result
