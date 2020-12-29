import pygame

from abc import ABC, abstractmethod
from flappy.ui.interaction.general import InteractionProcessor


class KeyboardActionDelegate(ABC):
    @abstractmethod
    def key_pressed(self, key):
        pass


class KeyboardProcessor(InteractionProcessor):
    def __init__(self, delegate: KeyboardActionDelegate):
        self.delegate = delegate

    def process(self, events):
        if not self.delegate:
            return
        analysable_events = [event for event in events if event.type == pygame.KEYDOWN]
        for event in analysable_events:
            self.delegate.key_pressed(event.key)
