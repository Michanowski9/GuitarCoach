from PyQt6.QtWidgets import QWidget

"""
Base class for all views.
"""
class View(QWidget):
    def __init__(self, view_model):
        super().__init__()
        
        self.view_model = view_model
