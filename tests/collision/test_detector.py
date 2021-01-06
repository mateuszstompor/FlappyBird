import pytest

from flappy.gmath.rect import Rect
from flappy.scene.bird import Bird
from flappy.gmath.point import Point
from flappy.gmath.ftypes import Size
from flappy.scene.board import Board
from flappy.scene.obstacle import Obstacle
from flappy.scene.flight import FlightVelocity
from flappy.animation.sequence import SequenceAnimation
from flappy.collision.detector import CollisionDetector


@pytest.fixture
def board():
    return Board(Bird(Rect(Point(0, 0), Size(1, 1)), FlightVelocity(1, 1), SequenceAnimation([])),
                 [Obstacle(Rect(Point(0.4, 0.4), Size(0.2, 0.2)))])


class TestIsColliding:
    def test_no_collision(self):
        rect_a, rect_b = Rect(Point(0, 0), Size(1, 1)), Rect(Point(3, 3), Size(1, 1))
        assert not CollisionDetector.is_colliding(rect_a, [rect_b])

    def test_single_collision(self):
        rect_a, rect_b = Rect(Point(0, 0), Size(1, 1)), Rect(Point(0, 0), Size(1, 1))
        assert CollisionDetector.is_colliding(rect_a, [rect_b])
