import pygame

from pygame.surface import Surface
from flappy.ui.view.general import View
from flappy.textures.library import TextureLibrary


class LostView(View):
    def draw(self, surface: Surface):
        self.render_game_over(surface)
        pygame.display.flip()

    def __init__(self):
        self.textures = TextureLibrary.with_images(['gameover.png'])

    def render_game_over(self, screen):
        image = self.textures.image('gameover.png')
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        screen.blit(image, pygame.rect.Rect(screen.get_rect()[2] / 2 - x,
                                            screen.get_rect()[2] / 2 - y,
                                            30, 30))
