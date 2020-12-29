from pygame.surface import Surface
from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def draw(self, surface: Surface):
        pass
