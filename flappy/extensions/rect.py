from pygame.rect import Rect


def x_centered(rect: Rect, inside: Rect) -> Rect:
    return Rect(inside[2] / 2 - rect[2]/2, *rect[1:])


def y_centered(rect: Rect, inside: Rect) -> Rect:
    return Rect(rect[0], inside[3] / 2 - rect[3] / 2, *rect[2:])


def x_adding(rect: Rect, delta: float) -> Rect:
    return Rect(rect[0] + delta, *rect[1:])


def y_adding(rect: Rect, delta: float) -> Rect:
    return Rect(rect[0], rect[1] + delta, *rect[2:])


def adding(rect: Rect, x_delta: float = 0, y_delta: float = 0):
    return x_adding(y_adding(rect, y_delta), x_delta)


def center(rect: Rect, inside: Rect, x: bool = False, y: bool = False):
    rect = x_centered(rect, inside) if x else rect
    return y_centered(rect, inside) if y else rect
