from random import uniform, choice

from flappy.gmath.rect import Rect
from flappy.gmath.ftypes import Bound
from flappy.scene.obstacle import Obstacle


class TerrainGenerator:
    def __init__(self, y_delta: Bound, x_delta: float, bound: Bound):
        self.y_delta = y_delta
        self.x_delta = x_delta
        self.bound = bound

    def generate_gap(self, previous: Rect) -> Rect:
        new = previous
        new.origin.x = max(new.origin.x + self.x_delta, 1.1)
        y_displacement = uniform(self.y_delta.low, self.y_delta.high)
        new.origin.y += choice([-1, 1]) * y_displacement
        new.origin.y = min(max(new.origin.y, self.bound.low), self.bound.high)
        return new

    def new(self, previous: Obstacle) -> Obstacle:
        return Obstacle(self.generate_gap(previous.gap))
