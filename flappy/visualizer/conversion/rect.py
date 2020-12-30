from pygame.surface import Surface
from pygame.rect import Rect as PRect
from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.gmath.point import Point


class RectConverter:
    @staticmethod
    def as_pygame(rect: Rect, screen: Surface) -> PRect:
        return PRect(rect.origin.x * screen.get_width(),
                     rect.origin.y * screen.get_height(),
                     rect.size.width * screen.get_width(),
                     rect.size.height * screen.get_height())

    @staticmethod
    def from_pygame(rect: PRect, screen: Surface) -> Rect:
        return Rect(Point(rect[0] / screen.get_width(), rect[1] / screen.get_height()),
                    Size(rect[2] / screen.get_width(), rect[3] / screen.get_height()))
