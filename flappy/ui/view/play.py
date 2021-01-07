from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.visualizer.drawer import Drawer
from flappy.visualizer.score import ScoreDrawer
from flappy.ui.view.blueprint import BlueprintView


class PlayView(BlueprintView):
    """
    Presented when the game is started. Composes
    image consisting of a bird, background, obstacles
    and user's score
    """
    def __init__(self, background, game):
        super().__init__(None, Point(0, 0))
        self.game = game
        self.background = background
        self.score_drawer = ScoreDrawer()
        self.board_drawer = Drawer()

    def draw(self, surface: Surface):
        self.board_drawer.draw(surface, self.game.board)
        self.score_drawer.draw(surface, self.game.score_counter.score())
        return surface

    def compose(self) -> Optional[Surface]:
        return self.draw(self.background.copy())
