import pygame

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.view.sprite import SpriteView
from flappy.ui.system.presenter import Presenter
from flappy.textures.library import TextureLibrary
from flappy.ui.controller.general import ViewController
from flappy.ui.interaction.mouse import TapHandler, MouseActionDelegate
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class ToastViewController(ViewController, KeyboardActionDelegate, MouseActionDelegate):
    def __init__(self, presenter: Presenter, image_name: str, parent: View):
        self.__image = TextureLibrary.load_images([image_name])[0]
        self.__view = SpriteView.centered_in(parent, self.__image, Point(0, 0))
        self.__keyboard = KeyboardProcessor(self)
        self.__presenter = presenter
        self.__mouse = TapHandler(self.__view, self)

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard, self.__mouse]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            self.__presenter.pop()
        elif key == pygame.K_q:
            self.__presenter.pop_all()

    def tapped(self):
        self.__presenter.pop()
