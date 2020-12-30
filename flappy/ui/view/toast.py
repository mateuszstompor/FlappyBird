import pygame

from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.textures.library import TextureLibrary
from flappy.visualizer.common import render_centered


class ToastView(View):  # pylint: disable=R0903
    def __init__(self, image_name):
        self.__image = TextureLibrary.load_images([image_name])[0]

    def draw(self, surface: Surface):
        render_centered(self.__image, surface)
        pygame.display.flip()
