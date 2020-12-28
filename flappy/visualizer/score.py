import pygame

from math import floor
from pygame.surface import Surface
from flappy.textures.library import TextureLibrary


class ScoreDrawer:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.__textures = TextureLibrary.with_images(ScoreDrawer.image_names())

    def draw(self, score):
        i, j = score % 10, floor(score / 10)
        i_image = self.__textures.image(f'{i}.png')
        screen_rect = self.screen.get_rect()
        if j == 0:
            self.screen.blit(i_image, pygame.rect.Rect(screen_rect[2]/2 - 10, 40, 40, 40))
        else:
            j_image = self.__textures.image(f'{j}.png')
            self.screen.blit(i_image, pygame.rect.Rect(screen_rect[2] / 2, 40, 40, 40))
            self.screen.blit(j_image, pygame.rect.Rect(screen_rect[2] / 2 - 25, 40, 40, 40))

    @staticmethod
    def image_names():
        return [f'{i}.png' for i in range(10)]
