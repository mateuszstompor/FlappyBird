from pygame.rect import Rect
from pygame.surface import Surface

from flappy.extensions.rect import center


def centered_rect(surface: Surface, in_rect: Rect,
                  x_axis: bool = False, y_axis: bool = False) -> Rect:
    return center(surface.get_rect(), in_rect, x_axis, y_axis)
