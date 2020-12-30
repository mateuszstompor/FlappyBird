from pygame.rect import Rect
from flappy.gmath.point import Point


def x_centered(rect: Rect, inside: Rect) -> Rect:
    return Rect(inside[2] / 2 - rect[2]/2, *rect[1:])


def y_centered(rect: Rect, inside: Rect) -> Rect:
    return Rect(rect[0], inside[3] / 2 - rect[3] / 2, *rect[2:])


def x_adding(rect: Rect, delta: float) -> Rect:
    return Rect(rect[0] + delta, *rect[1:])


def y_adding(rect: Rect, delta: float) -> Rect:
    return Rect(rect[0], rect[1] + delta, *rect[2:])


def adding(rect: Rect, point: Point):
    return x_adding(y_adding(rect, point.y), point.x)


def center(rect: Rect, inside: Rect, x_axis: bool = False, y_axis: bool = False):
    rect = x_centered(rect, inside) if x_axis else rect
    return y_centered(rect, inside) if y_axis else rect
