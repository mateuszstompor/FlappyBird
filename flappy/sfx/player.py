from __future__ import annotations

from typing import Dict

import pygame

from flappy.assets.pathfinder import PathFinder


class Player:
    """
    Takes care of loading sounds from the assets and
    providing a way to play them
    """
    def __init__(self, data: Dict[str, pygame.mixer.Sound]):
        self.__data = data

    def play(self, sound: str):
        pygame.mixer.Sound.play(self.__data[sound])

    @staticmethod
    def with_sounds(names) -> Player:
        data = {}
        for name in names:
            path = PathFinder.audio(name)
            data[name] = pygame.mixer.Sound(path)
        return Player(data)
