from typing import NamedTuple

from flappy.gmath.rect import Rect
from flappy.gmath.ftypes import Size
from flappy.gmath.point import Point


WallPart = NamedTuple('WallPart', [('upper', Rect), ('lower', Rect)])


class Obstacle:
    def __init__(self, gap: Rect):
        self.wall = WallPart(Obstacle.upper(gap), Obstacle.lower(gap))
        self.gap = gap

    @staticmethod
    def upper(gap: Rect) -> Rect:
        origin = Point(gap.origin.x, 0.0)
        size = Size(gap.size.width, 1.0 - gap.origin.y)
        return Rect(origin, size)

    @staticmethod
    def lower(gap: Rect) -> Rect:
        origin = Point(gap.origin.x, 1.0 - gap.origin.y + gap.size.height)
        size = Size(gap.size.width, gap.origin.y - gap.size.height)
        return Rect(origin, size)
