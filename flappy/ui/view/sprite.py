from __future__ import annotations

from typing import Optional

from pygame.surface import Surface

from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.ui.view.blueprint import BlueprintView
from flappy.extensions.surface import centered_rect


class SpriteView(BlueprintView):
    def __init__(self, parent: Optional[View], offset: Point, image: Surface):
        super().__init__(parent, offset)
        self.image = image

    def compose(self) -> Surface:
        return self.image

    @staticmethod
    def centered_in(view: View, image: Surface, offset: Point) -> SpriteView:
        background = view.compose()
        rect = centered_rect(image, background.get_rect(), x_axis=True, y_axis=True)
        return SpriteView(view, Point(*rect[:2]) + offset, image)
