from __future__ import annotations

from typing import Optional, List

from abc import ABC, abstractmethod

from pygame.surface import Surface

from flappy.gmath.point import Point


class View(ABC):
    """
    Interface of a view that can be rendered onto the screen.
    Root view is the one that has no parent. A view can have
    arbitrary number of children
    """
    @abstractmethod
    def compose(self) -> Optional[Surface]:
        pass

    @abstractmethod
    def subviews(self) -> List[View]:
        pass

    @abstractmethod
    def add_subview(self, view):
        pass

    @abstractmethod
    def offset(self) -> Point:
        pass

    @abstractmethod
    def parent_view(self) -> Optional[View]:
        pass
