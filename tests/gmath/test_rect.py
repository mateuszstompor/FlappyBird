import pytest

from flappy.gmath.rect import Rect
from flappy.gmath.ftypes import Size
from flappy.gmath.point import Point


@pytest.fixture
def square():
    return Rect(Point(0, 0), Size(1, 1))


@pytest.mark.parametrize('point', [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
def test_edge_points(square, point):
    assert point in square.edge_points()


class TestIn:
    def test_not(self, square):
        assert not square.contains(Point(2, 2))

    def test_edge(self, square):
        assert square.contains(Point(1, 1))

    def test_inside(self, square):
        assert square.contains(Point(0.5, 0.5))


class TestOverlap:
    def test_not(self, square):
        assert not Rect(Point(2, 2), Size(1, 1)).is_overlapping(square)

    def test_exact_match(self, square):
        assert Rect(Point(0, 0), Size(1, 1)).is_overlapping(square)

    def test_partial_overlap(self, square):
        assert Rect(Point(0.5, 0.5), Size(1, 1)).is_overlapping(square)
