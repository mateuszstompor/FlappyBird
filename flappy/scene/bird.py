from flappy.gmath.rect import Rect
from flappy.misc.representable import Representable
from flappy.animation.sequence import SequenceAnimation
from flappy.core.observer.passthrough import PassthroughSubject


class Bird(Representable):
    def __init__(self, frame: Rect,
                 flap_velocity: float,
                 horizontal_velocity: float,
                 vertical_velocity: float,
                 animation: SequenceAnimation):
        self.frame = frame
        self.flap_velocity = flap_velocity
        self.horizontal_velocity = horizontal_velocity
        self.vertical_velocity = vertical_velocity
        self.distance_travelled = 0
        self.animation = animation
        self.flaps = PassthroughSubject()
        self.current_angle = 0
        self.maximal_angle = 40

    def flap(self):
        self.vertical_velocity = self.flap_velocity
        self.animation.rewind()
        self.flaps.notify(None)
