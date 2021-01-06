from __future__ import annotations

from typing import Optional, List

from abc import ABC, abstractmethod

from pygame.surface import Surface

from flappy.gmath.point import Point


class View(ABC):
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
