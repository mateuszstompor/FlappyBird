import pygame

from pygame.surface import Surface

from flappy.ui.view.general import View


class ViewDrawer:
    """
    Class responsible for composing a flat surface that
    can be rendered onto the screen based on the view hierarchy
    """
    def __init__(self, root: Surface):
        self.__root = root

    def draw_recursively(self, view: View):
        surface, offset = view.compose(), view.offset()
        current_rect = surface.get_rect()
        rect = pygame.rect.Rect(current_rect[0] + offset.x, current_rect[1] + offset.y,
                                current_rect[2], current_rect[3])
        self.__root.blit(surface, rect)
        for subview in view.subviews():
            self.draw_recursively(subview)

    def draw_hierarchy(self, view: View):
        self.__root.fill((0, 0, 0))
        self.draw_recursively(view)
        pygame.display.flip()
