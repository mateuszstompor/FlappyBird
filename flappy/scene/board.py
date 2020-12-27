from typing import List
from flappy.scene.bird import Bird
from flappy.scene.obstacle import Obstacle
from flappy.misc.representable import Representable


class Board(Representable):
    def __init__(self, bird: Bird, obstacles: List[Obstacle]):
        self.bird = bird
        self.obstacles = obstacles
