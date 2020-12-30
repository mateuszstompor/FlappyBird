import pygame

from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.textures.library import TextureLibrary
from flappy.visualizer.common import render_centered


class LostView(View):
    def __init__(self):
        self.textures = TextureLibrary.with_images(['gameover.png'])

    def draw(self, surface: Surface):
        render_centered(self.textures['gameover.png'], surface)
        pygame.display.flip()
