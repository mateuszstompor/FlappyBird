import pygame

from flappy.ui.presenter import Presenter
from flappy.core.choice import WheelChoice
from flappy.ui.view.landing import LandingView
from flappy.animation.store import AnimationStore
from flappy.textures.library import TextureLibrary
from flappy.ui.controller.general import ViewController
from flappy.ui.controller.play import PlayViewController
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class LandingViewController(ViewController, KeyboardActionDelegate):
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

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            animation = self.__bird_animations.item()
            animation.repeat = False
            background = self.__backgrounds.item()
            self.__presenter.push(PlayViewController(self.__presenter, animation, background))
        elif key == pygame.K_1:
            self.__view.change_bird_animation(self.__bird_animations.next())
        elif key == pygame.K_2:
            self.__view.background = self.__backgrounds.next()
        elif key == pygame.K_q:
            self.__presenter.pop_all()
