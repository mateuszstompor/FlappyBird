from abc import ABC
from typing import Optional

import pygame

from flappy.ui.interaction.general import InteractionProcessor


class KeyboardActionDelegate(ABC):
    """
    Interface of optional methods that a delegate
    can implement in order to be informed about
    keyboard events
    """
    def key_pressed(self, key):
        pass

    def key_released(self, key):
        pass


class KeyboardProcessor(InteractionProcessor):
    """
    Responsible for handling keyboard events. If an event
    is recognized as supported the delegate is notified
    """
    def __init__(self, delegate: Optional[KeyboardActionDelegate]):
        self.delegate = delegate

    def allows_other(self) -> bool:
        return True

    def responds(self, events) -> bool:
        supported = [event for event in events if event.type in [pygame.KEYDOWN, pygame.KEYUP]]
        for event in supported:
            if self.delegate:
                if event.type == pygame.KEYUP:
                    self.delegate.key_released(event.key)
                else:
                    self.delegate.key_pressed(event.key)
            return True
        return False
