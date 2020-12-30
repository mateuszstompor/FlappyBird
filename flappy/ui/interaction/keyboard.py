import pygame

from abc import ABC, abstractmethod
from typing import Optional, List, Any
from flappy.ui.interaction.general import InteractionProcessor


class KeyboardActionDelegate(ABC):
    @abstractmethod
    def key_pressed(self, key):
        pass


class KeyboardProcessor(InteractionProcessor):
    def __init__(self, delegate: Optional[KeyboardActionDelegate]):
        self.delegate = delegate

    def process(self, events: List[Any]):
        if not self.delegate:
            return
        supported = [event for event in events if event.type == pygame.KEYDOWN]
        for event in supported:
            self.delegate.key_pressed(event.key)
