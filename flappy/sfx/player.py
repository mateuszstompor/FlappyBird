import pygame

from flappy.assets.pathfinder import PathFinder


class Player:
    def __init__(self, data):
        self.__data = data

    def play(self, sound):
        pygame.mixer.Sound.play(self.__data[sound])

    @staticmethod
    def with_sounds(names):
        data = {}
        for name in names:
            path = PathFinder.audio(name)
            data[name] = pygame.mixer.Sound(path)
        return Player(data)
