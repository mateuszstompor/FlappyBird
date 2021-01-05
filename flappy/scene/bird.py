from flappy.gmath.rect import Rect
from flappy.scene.flight import FlightVelocity
from flappy.animation.sequence import SequenceAnimation
from flappy.core.observer.passthrough import PassthroughSubject


class State:  # pylint: disable=R0903
    def __init__(self, velocity: float = 0, angle: float = 0, distance: float = 0):
        self.velocity = velocity
        self.angle = angle
        self.distance = distance


class Bird:  # pylint: disable=R0903
    def __init__(self, frame: Rect,
                 flight_velocity: FlightVelocity,
                 animation: SequenceAnimation):
        self.state = State()
        self.frame = frame
        self.flight_velocity = flight_velocity
        self.animation = animation
        self.flaps = PassthroughSubject()
        self.maximal_angle = 40

    def flap(self):
        self.state.velocity = self.flight_velocity.vertical
        self.animation.rewind()
        self.flaps.notify(None)
