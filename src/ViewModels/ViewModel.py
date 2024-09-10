
"""
Base class for all ViewModels.
"""
class ViewModel:
    def __init__(self, navigator):
        self.navigator = navigator

    """
    function to change view via navigator
    """
    def navigate_to(self, view_name):
        self.navigator.navigate(view_name)