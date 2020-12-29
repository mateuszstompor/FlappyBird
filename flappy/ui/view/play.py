import pygame

from flappy.game import Game
from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.visualizer.drawer import Drawer
from flappy.sfx.scene.game import GameAudio
from flappy.visualizer.score import ScoreDrawer


class PlayView(View):
    def __init__(self, bird_animation, background):
        self.game = Game(bird_animation)
        self.failed = False
        self.audio = GameAudio(flap_subject=self.game.board.bird.flaps,
                               collision_subject=self.game.collision_detector.collision_notifier,
                               score_subject=self.game.score_counter.point_gained)
        self.background = background
        self.screen = pygame.display.set_mode([285, 500])
        self.score_drawer = ScoreDrawer(self.screen)
        self.board_drawer = Drawer(self.screen)

    def draw(self, surface: Surface):
        self.game.update()
        self.board_drawer.draw(self.game.board, self.background)
        self.score_drawer.draw(self.game.score_counter.score)
        pygame.display.flip()
