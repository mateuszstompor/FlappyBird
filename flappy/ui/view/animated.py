from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.view.blueprint import BlueprintView
from flappy.extensions.surface import centered_rect
from flappy.animation.sequence import SequenceAnimation


class AnimatedView(BlueprintView):
    def __init__(self, parent: Optional[View], offset: Point, animation: SequenceAnimation):
        super().__init__(parent, offset)
        self.__parent = parent
        self.__offset = offset
        self.animation = animation

    def compose(self) -> Optional[Surface]:
        return self.animation.data()

    @staticmethod
    def centered_in(view: View, animation: SequenceAnimation, offset: Point):
        background = view.compose()
        rect = centered_rect(animation.data(), background.get_rect(), x_axis=True, y_axis=True)
        return AnimatedView(view, Point(*rect[:2]) + offset, animation)
