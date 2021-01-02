from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.ui.view.general import View


class BlueprintView(View):
    def __init__(self, parent: Optional[View], offset: Point):
        self._offset = offset
        self._parent = parent
        self._subviews = []

    def subviews(self):
        return self._subviews

    def add_subview(self, view):
        self._subviews.append(view)

    def compose(self) -> Optional[Surface]:
        return None

    def offset(self) -> Point:
        return self._offset

    def parent(self):
        return self._parent