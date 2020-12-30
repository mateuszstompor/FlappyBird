from abc import ABC, abstractmethod

from pygame.surface import Surface


class View(ABC):  # pylint: disable=R0903
    @abstractmethod
    def draw(self, surface: Surface):
        pass
