from __future__ import annotations

from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.layout.composer import Layout
from flappy.ui.view.blueprint import BlueprintView


class SpriteView(BlueprintView):
    """
    View capable of presenting still sprite
    """
    def __init__(self, parent: Optional[View], offset: Point, image: Surface):
        super().__init__(parent, offset)
        self.image = image

    def compose(self) -> Surface:
        return self.image

    @staticmethod
    def centered_in(view: View, image: Surface, offset: Point) -> SpriteView:
        background = view.compose()
        rect = Layout(image.get_rect()).center(background.get_rect()).rect
        return SpriteView(view, Point(*rect[:2]) + offset, image)
