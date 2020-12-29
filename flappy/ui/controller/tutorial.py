import pygame

from flappy.ui.presenter import Presenter
from flappy.ui.view.tutorial import TutorialView
from flappy.ui.controller.general import ViewController
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class TutorialViewController(ViewController, KeyboardActionDelegate):
    def __init__(self, presenter: Presenter):
        self.__view = TutorialView()
        self.__keyboard = KeyboardProcessor(self)
        self.__presenter = presenter

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            self.__presenter.pop()
        elif key == pygame.K_q:
            self.__presenter.pop_all()