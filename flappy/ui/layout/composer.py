from pygame.rect import Rect as PRect


class Layout:
    """
    Manipulates rect position according to the
    user's - programmer - guidance
    """
    def __init__(self, rect: PRect):
        self.rect = rect

    def center(self, inside: PRect):
        rect = PRect(inside[2] / 2 - self.rect[2] / 2,
                     inside[3] / 2 - self.rect[3] / 2, *self.rect[2:])
        return Layout(rect)

    def offset(self, x_delta: float = 0, y_delta: float = 0):
        return Layout(PRect(self.rect[0] + x_delta, self.rect[1] + y_delta, *self.rect[2:]))
