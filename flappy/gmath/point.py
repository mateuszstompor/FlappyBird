from __future__ import annotations

from typing import Any


class Point:
    def __init__(self, x: float, y: float):
        self.x = x  # pylint: disable=C0103
        self.y = y  # pylint: disable=C0103

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def offset(self, x_offset: float = 0, y_offset: float = 0):
        return Point(self.x + x_offset, self.y + y_offset)

    def __sub__(self, other: Point):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: Any):
        return isinstance(other, Point) and other.x == self.x and other.y == self.y
