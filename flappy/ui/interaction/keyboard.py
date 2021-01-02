from abc import ABC
from typing import Optional

import pygame

from flappy.ui.interaction.general import InteractionProcessor


class KeyboardActionDelegate(ABC):
    def key_pressed(self, key):
        pass

    def key_released(self, key):
        pass


class KeyboardProcessor(InteractionProcessor):
    def __init__(self, delegate: Optional[KeyboardActionDelegate]):
        self.delegate = delegate

    def allows_other(self) -> bool:
        return True

    def responds(self, events) -> bool:
        if self.delegate:
            supported = [event for event in events if event.type == pygame.KEYDOWN]
            for event in supported:
                self.delegate.key_pressed(event.key)
                return True
        return False
