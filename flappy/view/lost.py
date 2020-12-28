import pygame

from flappy.view.general import View
from flappy.textures.library import TextureLibrary


class LostView(View):
    def __init__(self, screen):
        self.screen = screen
        self.textures = TextureLibrary.with_images(['gameover.png'])

    def render_game_over(self):
        image = self.textures.image('gameover.png')
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        self.screen.blit(image, pygame.rect.Rect(self.screen.get_rect()[2] / 2 - x,
                                                 self.screen.get_rect()[2] / 2 - y,
                                                 30, 30))
        pygame.display.flip()

    def show(self):
        self.render_game_over()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
