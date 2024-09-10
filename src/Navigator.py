from Views.MenuView import MenuView
from Views.SettingsView import SettingsView
from Views.ExercisesView import ExercisesView

"""
This class allows for managing views.
"""
class Navigator():
    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget
        self.views = {
            "Menu": MenuView(self),
            "Settings": SettingsView(self),
            "Exercises": ExercisesView(self)
        }

    """
    This function is used to change view to another

    :param view_name: The name of the view you want to switch to.
    """
    def navigate(self, view_name):
        try:
            self.stacked_widget.addWidget(self.views[view_name])
            self.stacked_widget.setCurrentWidget(self.views[view_name])
        except:
            print("no view to show")
