import pygame

from pygame.surface import Surface
from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.extensions.rect import center
from flappy.visualizer.drawer import Drawer
from flappy.textures.library import TextureLibrary
from flappy.visualizer.common import render_centered
from flappy.animation.sequence import SequenceAnimation


class LandingView(View):
    def __init__(self, bird_animation: SequenceAnimation, background: Surface):
        self.background = background
        self.bird_animation = bird_animation
        self.bird_animation.repeat = True
        self.bird_animation.play()
        self.__board_drawer = Drawer()
        self.__textures = TextureLibrary.with_images(['flappy-bird.png', 'play.png', 'base.png'])

    def draw(self, surface: Surface):
        surface.blit(self.background, surface.get_rect())
        render_centered(self.__textures['flappy-bird.png'], surface, Point(0, -110))
        render_centered(self.__textures['base.png'], surface, Point(0, 250))
        render_centered(self.__textures['play.png'], surface, Point(0, 130))
        rect = center(self.bird_animation.data().get_rect(), surface.get_rect(),
                      y_axis=True, x_axis=True)
        surface.blit(self.bird_animation.data(), rect)
        pygame.display.flip()

    def change_bird_animation(self, animation: SequenceAnimation):
        self.bird_animation = animation
        self.bird_animation.repeat = True
        if not self.bird_animation.is_playing():
            self.bird_animation.play()
