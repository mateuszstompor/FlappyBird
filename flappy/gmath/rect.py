from __future__ import annotations

from typing import List

from pygame.rect import Rect as PRect

from flappy.gmath.ftypes import Size
from flappy.gmath.point import Point


class Rect:
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def edge_points(self) -> List[Point]:
        return [self.origin,
                self.origin + Point(self.size.width, 0),
                self.origin + Point(self.size.width, self.size.height),
                self.origin + Point(0, self.size.height)]

    def is_overlapping(self, rect) -> bool:
        return any(map(self.contains, rect.edge_points())) or \
               any(map(rect.contains, self.edge_points()))

    def contains(self, point: Point) -> bool:
        return self.origin.x + self.size.width >= point.x >= self.origin.x and \
               self.origin.y + self.size.height >= point.y >= self.origin.y

    class Converter:
        @staticmethod
        def to_pygame(rect: Rect) -> PRect:
            return PRect(rect.origin.x, rect.origin.y, rect.size.width, rect.size.height)

        @staticmethod
        def from_pygame(rect: PRect) -> Rect:
            return Rect(Point(*rect[:2]), Size(*rect[2:]))

    class Positioner:
        @staticmethod
        def to_pygame(rect: Rect, screen: PRect) -> PRect:
            width, height = screen[2:]
            return PRect(rect.origin.x * width,
                         rect.origin.y * height,
                         rect.size.width * width,
                         rect.size.height * height)

        @staticmethod
        def from_pygame(rect: PRect, screen: PRect) -> Rect:
            width, height = screen[2:]
            return Rect(Point(rect[0] / width, rect[1] / height),
                        Size(rect[2] / width, rect[3] / height))
