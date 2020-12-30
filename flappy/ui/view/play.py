import pygame

from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.visualizer.drawer import Drawer
from flappy.visualizer.score import ScoreDrawer


class PlayView(View):
    def __init__(self, background, game):
        self.game = game
        self.background = background
        self.score_drawer = ScoreDrawer()
        self.board_drawer = Drawer()

    def draw(self, surface: Surface):
        surface.blit(self.background, surface.get_rect())
        self.board_drawer.draw(surface, self.game.board)
        self.score_drawer.draw(surface, self.game.score_counter.score())
        pygame.display.flip()
