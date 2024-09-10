from PyQt6 import uic
from PyQt6.QtWidgets import QPushButton

from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

from Views.View import View
from ViewModels.ExercisesViewModel import ExercisesViewModel

"""
View with list of all loaded exercises.
"""
class ExercisesView(View):
    def __init__(self, navigator):
        view_model = ExercisesViewModel(navigator)
        super().__init__(view_model)

        uic.loadUi("src/views/ExercisesView.ui", self)

        for exercise in view_model.get_exercises_names():
            self.exercises_button_list.addWidget(QPushButton(exercise))

        self.back_button = QPushButton("Back")
        self.exercises_button_list.addWidget(self.back_button)

        self.go_to_menu_button.clicked.connect(view_model.navigate_to_menu)
        self.back_button.clicked.connect(view_model.navigate_to_menu)
        self.go_to_menu_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
