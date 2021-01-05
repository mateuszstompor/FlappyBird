import pytest
import pygame

from flappy.gmath.rect import Rect
from flappy.gmath.ftypes import Size
from flappy.gmath.point import Point


@pytest.fixture
def square():
    return Rect(Point(0, 0), Size(1, 1))


@pytest.fixture
def pygame_square():
    return pygame.rect.Rect(0, 0, 1, 1)


@pytest.fixture
def pygame_screen_rect():
    return pygame.rect.Rect(0, 0, 1920, 1080)


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


class TestConverter:
    def test_to_pygame(self, square):
        rect = Rect.Converter.to_pygame(square)
        assert 0 == rect[0] == rect[1]
        assert 1 == rect[2] == rect[3]

    def test_from_pygame(self, pygame_square):
        rect = Rect.Converter.from_pygame(pygame_square)
        assert rect.origin.x == 0 == rect.origin.y
        assert rect.size.width == rect.size.height == 1


class TestPositioner:
    def test_from_pygame(self, pygame_square, pygame_screen_rect):
        rect = Rect.Positioner.from_pygame(pygame_square, pygame_screen_rect)
        assert rect.origin.x == rect.origin.y == 0
        assert rect.size.width == 1/1920
        assert rect.size.height == 1/1080

    def test_to_pygame(self, square, pygame_screen_rect):
        rect = Rect.Positioner.to_pygame(square, pygame_screen_rect)
        assert rect[0] == rect[1] == 0
        assert rect[2] == 1920
        assert rect[3] == 1080
