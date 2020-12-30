from pygame.surface import Surface
from flappy.gmath.point import Point
from flappy.extensions.rect import adding, center


def render_centered(image: Surface, surface: Surface, offset: Point = Point(0, 0)):
    centered = center(image.get_rect(), surface.get_rect(), x_axis=True, y_axis=True)
    rect = adding(centered, offset)
    surface.blit(image, rect)
