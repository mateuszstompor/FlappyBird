from typing import Any

import pygame

from flappy.core.observer.general import Observer
from flappy.game import Game
from flappy.view.general import View
from flappy.sfx.scene.game import GameAudio
from flappy.view.lost import LostView
from flappy.visualizer.drawer import Drawer
from flappy.visualizer.score import ScoreDrawer


class PlayView(View, Observer):
    def update(self, subject, event: Any):
        self.failed = True

    def __init__(self, bird_animation, background):
        self.game = Game(bird_animation)
        self.failed = False
        self.game.collision_detector.collision_notifier.attach(self)
        self.audio = GameAudio(flap_subject=self.game.board.bird.flaps,
                               collision_subject=self.game.collision_detector.collision_notifier,
                               score_subject=self.game.score_counter.point_gained)
        self.background = background
        self.screen = pygame.display.set_mode([285, 500])
        self.score_drawer = ScoreDrawer(self.screen)
        self.board_drawer = Drawer(self.screen)

    def show(self):
        while True:
            if self.failed:
                LostView(self.screen).show()
                self.game.reset()
                self.failed = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game.board.bird.flap()
            self.game.update()
            self.board_drawer.draw(self.game.board, self.background)
            self.score_drawer.draw(self.game.score_counter.score)
            pygame.display.flip()
