from abc import ABC, abstractmethod

from pygame.surface import Surface


class View(ABC):
    @abstractmethod
    def draw(self, surface: Surface):
        pass
