import pygame

from flappy.ui.presenter import Presenter
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
        library = TextureLibrary.with_images(['background-day.png', 'background-night.png'])
        self.__backgrounds = [library['background-day.png'], library['background-night.png']]
        self.__bird_animations = [animation_store.blue_bird(),
                                  animation_store.red_bird(),
                                  animation_store.yellow_bird()]
        self.__chosen_background = 0
        self.__chosen_animation = 0
        self.__view = LandingView(self.current_bird_animation(), self.current_background())

    def view(self):
        return self.__view

    def current_background(self):
        return self.__backgrounds[self.__chosen_background]

    def current_bird_animation(self):
        return self.__bird_animations[self.__chosen_animation]

    def interaction_processors(self):
        return [self.__keyboard]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            animation = self.current_bird_animation()
            animation.repeat = False
            background = self.current_background()
            self.__presenter.push(PlayViewController(self.__presenter, animation, background))
        elif key == pygame.K_1:
            self.__chosen_animation = (self.__chosen_animation + 1) % 3
            self.__view.change_bird_animation(self.current_bird_animation())
        elif key == pygame.K_2:
            self.__chosen_background = (self.__chosen_background + 1) % 2
            self.__view.background = self.current_background()
        elif key == pygame.K_q:
            self.__presenter.pop_all()
