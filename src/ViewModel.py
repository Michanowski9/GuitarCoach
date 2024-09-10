
"""
The base class for ViewModels
"""
class ViewModel:
    def __init__(self, navigator):
        self.navigator = navigator

    """
    This function is used to tell navigator to change view.

    :param view_name: The name of the view you want to switch to.
    """
    def navigate_to(self, view_name):
        self.navigator.navigate(view_name)