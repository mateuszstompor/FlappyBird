from flappy.misc.representable import Representable


class Point(Representable):
    def __init__(self, x: float, y: float):
        self.x = x  # pylint: disable=C0103
        self.y = y  # pylint: disable=C0103

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
