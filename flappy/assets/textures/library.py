from __future__ import annotations

from typing import Dict, List, Optional

import pygame

from flappy.assets.pathfinder import PathFinder


class TextureLibrary:
    def __init__(self, data: Dict[str, pygame.Surface]):
        self.__data = data

    def __getitem__(self, item) -> Optional[pygame.Surface]:
        return self.image(item)

    def image(self, name: str) -> Optional[pygame.Surface]:
        return self.__data.get(name)

    @staticmethod
    def with_images(names: List[str]) -> TextureLibrary:
        data = {}
        for name in names:
            path = PathFinder.sprite(name)
            data[name] = pygame.image.load(path)
        return TextureLibrary(data)

    @staticmethod
    def load_images(names: List[str]) -> List[pygame.Surface]:
        loader = TextureLibrary.with_images(names)
        return [loader[name] for name in names]
