import pygame
import pytest

from flappy.ui.layout.composer import Layout


@pytest.fixture
def rect():
    return pygame.rect.Rect(0, 0, 2, 2)


def test_center(rect):
    rect = Layout(rect).center(pygame.rect.Rect(0, 0, 10, 10)).rect
    assert rect[0] == 4 == rect[1]
    assert rect[2] == 2 == rect[3]


def test_offset(rect):
    rect = Layout(rect).offset(20, 21).rect
    assert rect[0] == 20
    assert rect[1] == 21
    assert rect[2] == rect[3] == 2
