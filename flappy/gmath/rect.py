from __future__ import annotations

from pygame.surface import Surface
from pygame.rect import Rect as PRect

from flappy.gmath.ftypes import Size
from flappy.gmath.point import Point


class Rect:
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def edge_points(self):
        return [self.origin,
                self.origin + Point(self.size.width, 0),
                self.origin + Point(self.size.width, self.size.height),
                self.origin + Point(0, self.size.height)]

    def is_overlapping(self, rect):
        return any(map(self.contains, rect.edge_points())) or \
               any(map(rect.contains, self.edge_points()))

    def contains(self, point: Point):
        return self.origin.x + self.size.width >= point.x >= self.origin.x and \
               self.origin.y + self.size.height >= point.y >= self.origin.y

    class Converter:
        @staticmethod
        def to_pygame(rect: Rect):
            return PRect(rect.origin.x, rect.origin.y, rect.size.width, rect.size.height)

        @staticmethod
        def from_pygame(rect: PRect):
            return Rect(Point(rect[0], rect[1]), Size(rect[2], rect[3]))

    class Positioner:
        @staticmethod
        def as_pygame(rect: Rect, screen: Surface) -> PRect:
            return PRect(rect.origin.x * screen.get_width(),
                         rect.origin.y * screen.get_height(),
                         rect.size.width * screen.get_width(),
                         rect.size.height * screen.get_height())

        @staticmethod
        def from_pygame(rect: PRect, screen: Surface) -> Rect:
            return Rect(Point(rect[0] / screen.get_width(), rect[1] / screen.get_height()),
                        Size(rect[2] / screen.get_width(), rect[3] / screen.get_height()))
