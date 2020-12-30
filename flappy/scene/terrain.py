from random import uniform
from random import choice
from flappy.gmath.frange import Frange
from flappy.scene.obstacle import Obstacle


class TerrainGenerator:  # pylint: disable=R0903
    def __init__(self, y_delta: Frange, x_delta: float, bound: Frange):
        self.y_delta = y_delta
        self.x_delta = x_delta
        self.bound = bound

    def new(self, previous: Obstacle) -> Obstacle:
        new = previous.gap
        new.origin.x = max(new.origin.x + self.x_delta, 1.1)
        y_displacement = uniform(self.y_delta.low, self.y_delta.high)
        new.origin.y += choice([-1, 1]) * y_displacement
        new.origin.y = min(max(new.origin.y, self.bound.low), self.bound.high)
        return Obstacle(new)
