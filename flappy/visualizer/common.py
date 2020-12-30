from pygame.surface import Surface
from flappy.gmath.point import Point
from flappy.extensions.rect import adding, center


def render_centered(image: Surface, surface: Surface, offset: Point = Point(0, 0)):
    centered = center(image.get_rect(), surface.get_rect(), x=True, y=True)
    rect = adding(centered, y_delta=offset.y, x_delta=offset.x)
    surface.blit(image, rect)
