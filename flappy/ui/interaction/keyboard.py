from abc import ABC
from typing import Optional, List, Any

import pygame

from flappy.ui.interaction.general import InteractionProcessor


class KeyboardActionDelegate(ABC):
    def key_pressed(self, key):
        pass

    def key_released(self, key):
        pass


class KeyboardProcessor(InteractionProcessor):  # pylint: disable=R0903
    def __init__(self, delegate: Optional[KeyboardActionDelegate]):
        self.delegate = delegate

    def process(self, events: List[Any]):
        if not self.delegate:
            return
        supported = [event for event in events if event.type == pygame.KEYDOWN]
        for event in supported:
            self.delegate.key_pressed(event.key)
