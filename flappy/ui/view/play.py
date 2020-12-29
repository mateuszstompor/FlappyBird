import pygame

from flappy.game import Game
from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.visualizer.drawer import Drawer
from flappy.visualizer.score import ScoreDrawer


class PlayView(View):
    def __init__(self, bird_animation, background):
        self.game = Game(bird_animation)
        self.background = background
        self.score_drawer = ScoreDrawer()
        self.board_drawer = Drawer()

    def draw(self, surface: Surface):
        self.game.update()
        self.board_drawer.draw(surface, self.game.board, self.background)
        self.score_drawer.draw(surface, self.game.score_counter.score())
        pygame.display.flip()
