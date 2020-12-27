from flappy.gmath.rect import Rect
from flappy.misc.representable import Representable


class Bird(Representable):
    def __init__(self, frame: Rect, flap_velocity: float, horizontal_velocity: float, vertical_velocity: float):
        self.frame = frame
        self.flap_velocity = flap_velocity
        self.horizontal_velocity = horizontal_velocity
        self.vertical_velocity = vertical_velocity
        self.distance_travelled = 0

    def flap(self):
        self.vertical_velocity = self.flap_velocity
