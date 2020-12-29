import pygame

from typing import Any
from flappy.ui.presenter import Presenter
from flappy.ui.view.play import PlayView
from flappy.sfx.scene.game import GameAudio
from flappy.core.observer.general import Observer
from flappy.ui.controller.general import ViewController
from flappy.ui.controller.lost import LostViewController
from flappy.ui.controller.tutorial import TutorialViewController
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class PlayViewController(ViewController, KeyboardActionDelegate, Observer):
    def __init__(self, presenter: Presenter, bird_animation, background):
        self.__view = PlayView(bird_animation, background)
        self.__audio = GameAudio(flap_subject=self.__view.game.board.bird.flaps,
                                 collision_subject=self.__view.game.collision_detector.collision_notifier,
                                 score_subject=self.__view.game.score_counter.point_gained)
        self.__view.game.collision_detector.collision_notifier.attach(self)
        self.__keyboard = KeyboardProcessor(self)
        self.__presenter = presenter
        self.__first_time = True

    def view(self):
        return self.__view

    def interaction_processors(self):
        return [self.__keyboard]

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            self.__view.game.board.bird.flap()
        elif key == pygame.K_q:
            self.__presenter.pop_all()

    def received_focus(self):
        if self.__first_time:
            self.__presenter.push(TutorialViewController(self.__presenter))
            self.__first_time = False
        self.__view.game.reset()

    def update(self, subject, event: Any):
        self.__presenter.push(LostViewController(self.__presenter))
