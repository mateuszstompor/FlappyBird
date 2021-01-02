import pygame

from flappy.core.choice import WheelChoice
from flappy.ui.view.landing import LandingView
from flappy.ui.system.presenter import Presenter
from flappy.animation.store import AnimationStore
from flappy.textures.library import TextureLibrary
from flappy.ui.controller.general import ViewController
from flappy.ui.controller.play import PlayViewController
from flappy.ui.interaction.mouse import TapHandler, MouseActionDelegate
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class LandingViewController(ViewController, KeyboardActionDelegate, MouseActionDelegate):
    def __init__(self, presenter: Presenter):
        self.__keyboard = KeyboardProcessor(self)
        self.__presenter = presenter
        animation_store = AnimationStore()
        images = TextureLibrary.load_images(['background-day.png', 'background-night.png'])
        self.__backgrounds = WheelChoice(images)
        self.__bird_animations = WheelChoice([animation_store.blue_bird(),
                                              animation_store.red_bird(),
                                              animation_store.yellow_bird()])
        self.__view = LandingView(self.__bird_animations.item(), self.__backgrounds.item())
        self.__mouse = TapHandler(self.__view.play_view, delegate=self)

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard, self.__mouse]

    def move_to_next(self):
        animation = self.__bird_animations.item()
        animation.repeat = False
        background = self.__backgrounds.item()
        self.__presenter.push(PlayViewController(self.__presenter, animation, background))

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            self.move_to_next()
        elif key == pygame.K_1:
            self.__view.set_bird_animation(self.__bird_animations.next_item())
        elif key == pygame.K_2:
            self.__view.set_background(self.__backgrounds.next_item())
        elif key == pygame.K_q:
            self.__presenter.pop_all()

    def tapped(self):
        self.move_to_next()
