from typing import Any

import pygame

from flappy.game import Game
from flappy.ui.view.play import PlayView
from flappy.sfx.scene.game import GameAudio
from flappy.ui.system.presenter import Presenter
from flappy.core.observer.general import Observer
from flappy.ui.controller.general import ViewController
from flappy.ui.controller.toast import ToastViewController
from flappy.ui.interaction.mouse import MouseActionDelegate, TapHandler
from flappy.ui.interaction.keyboard import KeyboardProcessor, KeyboardActionDelegate


class PlayViewController(ViewController, KeyboardActionDelegate, MouseActionDelegate, Observer):
    def __init__(self, presenter: Presenter, bird_animation, background):
        self.__game = Game(bird_animation)
        self.__view = PlayView(background, self.__game)
        collision_subject = self.__game.collision_detector.collision_notifier
        self.__audio = GameAudio(flap_subject=self.__game.board.bird.flaps,
                                 collision_subject=collision_subject,
                                 score_subject=self.__game.score_counter.point_gained)
        self.__game.collision_detector.collision_notifier.attach(self)
        self.__processors = [KeyboardProcessor(self), TapHandler(self.__view, self)]
        self.__presenter = presenter
        self.__first_time = True
        self.__in_focus = False

    def view(self):
        return self.__view

    def interaction_processors(self):
        return self.__processors

    def key_pressed(self, key):
        if key == pygame.K_SPACE:
            self.__view.game.board.bird.flap()
        elif key == pygame.K_q:
            self.__presenter.pop_all()

    def received_focus(self):
        if self.__first_time:
            self.__presenter.push(ToastViewController(self.__presenter, 'message.png', self.__view))
            self.__first_time = False
        self.__view.game.reset()
        self.__in_focus = True

    def lost_focus(self):
        self.__in_focus = False

    def update(self, subject, event: Any):
        self.__presenter.push(ToastViewController(self.__presenter, 'gameover.png', self.__view))

    def view_redrawn(self):
        if self.__in_focus:
            self.__game.update()

    def tapped(self, sender: TapHandler):
        self.__view.game.board.bird.flap()
