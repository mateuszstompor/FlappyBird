import pygame

from flappy.ui.presenter import Presenter
from flappy.ui.view.landing import LandingView
from flappy.ui.controller.general import ViewController
from flappy.ui.controller.play import PlayViewController
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class LandingViewController(ViewController, KeyboardActionDelegate):
    def __init__(self, presenter: Presenter):
        self.__view = LandingView()
        self.__keyboard = KeyboardProcessor(self)
        self.__presenter = presenter

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            animation = self.__view.available_animations[self.__view.current]
            animation.repeat = False
            background = self.__view.backgrounds[self.__view.chosen_background]
            self.__presenter.push(PlayViewController(self.__presenter, animation, background))
        elif key == pygame.K_1:
            self.__view.current = (self.__view.current + 1) % 3
            self.__view.change_bird_animation(self.__view.available_animations[self.__view.current])
        elif key == pygame.K_2:
            self.__view.chosen_background = (self.__view.chosen_background + 1) % 2
        elif key == pygame.K_q:
            self.__presenter.pop_all()
