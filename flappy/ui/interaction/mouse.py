from abc import ABC
from typing import Optional

import pygame

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.visualizer.conversion.rect import RectConverter
from flappy.ui.interaction.general import InteractionProcessor


class MouseActionDelegate(ABC):
    def tapped(self):
        pass

    def released(self):
        pass


class TapHandler(InteractionProcessor):
    def __init__(self, view: View, delegate: Optional[MouseActionDelegate]):
        self.__view = view
        self.delegate = delegate

    def process(self, events):
        for event in events:
            if event.type in [pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
                position = pygame.mouse.get_pos()
                if self.interacts(Point(*position)):
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.delegate.released()
                    else:
                        self.delegate.tapped()

    def interacts(self, point: Point):
        tap_position = point - self.absolute_position(self.__view)
        rect = RectConverter.convert_from_pygame(self.__view.compose().get_rect())
        return rect.is_in(tap_position)

    @staticmethod
    def absolute_position(view: View):
        offset, current_view = Point(0, 0), view
        while current_view:
            offset += current_view.offset()
            current_view = current_view.parent()
        return offset
