import pygame

from typing import Dict
from flappy.assets.pathfinder import PathFinder


class TextureLibrary:
    def __init__(self, data: Dict[str, pygame.Surface]):
        self.__data = data

    def __getitem__(self, item):
        return self.image(item)

    def image(self, name) -> pygame.Surface:
        return self.__data[name]

    @staticmethod
    def with_images(names):
        data = {}
        for name in names:
            path = PathFinder.sprite(name)
            data[name] = pygame.image.load(path)
        return TextureLibrary(data)

    @staticmethod
    def load_images(names):
        loader = TextureLibrary.with_images(names)
        return [loader[name] for name in names]
