import pygame

from flappy.assets.pathfinder import PathFinder


class TextureLibrary:
    def __init__(self, data):
        self.__data = data

    def __getitem__(self, item):
        return self.image(item)

    def image(self, name):
        return self.__data[name]

    @staticmethod
    def with_images(names):
        data = {}
        for name in names:
            path = PathFinder.sprite(name)
            data[name] = pygame.image.load(path)
        return TextureLibrary(data)
