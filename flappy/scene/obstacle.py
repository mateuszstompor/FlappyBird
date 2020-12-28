from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.gmath.point import Point
from flappy.misc.representable import Representable


class Obstacle(Representable):
    def __init__(self, gap: Rect):
        self.walls = Obstacle.upper_wall(gap), Obstacle.lower_wall(gap)
        self.gap = gap

    @staticmethod
    def upper_wall(gap: Rect):
        origin = Point(gap.origin.x, 0.0)
        size = Size(gap.size.width, 1.0 - gap.origin.y)
        return Rect(origin, size)

    @staticmethod
    def lower_wall(gap: Rect):
        origin = Point(gap.origin.x, 1.0 - gap.origin.y + gap.size.height)
        size = Size(gap.size.width, gap.origin.y - gap.size.height)
        return Rect(origin, size)
