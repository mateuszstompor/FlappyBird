from __future__ import annotations

from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.layout.composer import Layout
from flappy.ui.view.blueprint import BlueprintView
from flappy.animation.sequence import SequenceAnimation


class AnimatedView(BlueprintView):
    """
    View capable of presenting animated sprite
    """
    def __init__(self, parent: Optional[View], offset: Point, animation: SequenceAnimation):
        super().__init__(parent, offset)
        self.__parent = parent
        self.__offset = offset
        self.animation = animation

    def compose(self) -> Optional[Surface]:
        return self.animation.data()

    @staticmethod
    def centered_in(view: View, animation: SequenceAnimation, offset: Point) -> AnimatedView:
        background = view.compose()
        rect = Layout(animation.data().get_rect()).center(background.get_rect()).rect
        return AnimatedView(view, Point(*rect[:2]) + offset, animation)
