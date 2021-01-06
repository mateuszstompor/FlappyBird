from __future__ import annotations

from abc import ABC
from typing import Optional

import pygame

from flappy.gmath.rect import Rect
from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.interaction.general import InteractionProcessor


class MouseActionDelegate(ABC):
    def tapped(self, sender: TapHandler):
        pass

    def released(self, sender: TapHandler):
        pass


class TapHandler(InteractionProcessor):
    def __init__(self, view: View, delegate: Optional[MouseActionDelegate]):
        self.__view = view
        self.delegate = delegate

    def responds(self, events) -> bool:
        for event in events:
            if event.type in [pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
                position = pygame.mouse.get_pos()
                if self.interacts(Point(*position)):
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.delegate.released(self)
                    else:
                        self.delegate.tapped(self)
                    return True
        return False

    def allows_other(self) -> bool:
        return False

    def interacts(self, point: Point) -> int:
        tap_position = point - self.absolute_position(self.__view)
        rect = Rect.Converter.from_pygame(self.__view.compose().get_rect())
        return rect.contains(tap_position)

    @staticmethod
    def absolute_position(view: View) -> Point:
        offset, current_view = Point(0, 0), view
        while current_view:
            offset += current_view.offset()
            current_view = current_view.parent()
        return offset
