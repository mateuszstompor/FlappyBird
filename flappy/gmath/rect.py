from flappy.gmath.size import Size
from flappy.gmath.point import Point
from flappy.misc.representable import Representable


class Rect(Representable):
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def edge_points(self):
        return [self.origin,
                self.origin + Point(self.size.width, 0),
                self.origin + Point(self.size.width, self.size.height),
                self.origin + Point(0, self.size.height)]

    def is_in(self, point: Point):
        return self.origin.x + self.size.width >= point.x >= self.origin.x and \
               self.origin.y + self.size.height >= point.y >= self.origin.y

    def is_overlapping(self, rect):
        return any(map(lambda p: self.is_in(p), rect.edge_points())) or \
               any(map(lambda p: rect.is_in(p), self.edge_points()))
