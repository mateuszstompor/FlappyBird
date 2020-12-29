import pygame

from pygame.surface import Surface
from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.scene.bird import Bird
from flappy.gmath.point import Point
from flappy.ui.view.general import View
from flappy.visualizer.drawer import Drawer
from flappy.animation.store import AnimationStore
from flappy.textures.library import TextureLibrary


class LandingView(View):
    def draw(self, surface: Surface):
        self.board_drawer = Drawer(surface)
        self.board_drawer.present_background(self.backgrounds[self.chosen_background])
        self.render_logo(surface)
        self.render_sidewalk(surface)
        self.render_button(surface)
        self.board_drawer.present_bird(self.bird)
        pygame.display.flip()

    def __init__(self):
        self.textures = TextureLibrary.with_images(['flappy-bird.png', 'play.png', 'base.png'])
        self.backgrounds = ['background-day.png', 'background-night.png']
        self.chosen_background = 0
        bird_size = Size(0.068, 0.05)

        self.animation_store = AnimationStore()
        self.available_animations = [self.animation_store.blue_bird(),
                                     self.animation_store.red_bird(),
                                     self.animation_store.yellow_bird()]
        self.current = 0
        self.bird = Bird(Rect(Point(0.5 - bird_size.width / 2, 0.5), bird_size),
                         flap_velocity=0.6,
                         horizontal_velocity=0.3,
                         vertical_velocity=0.0,
                         animation=self.available_animations[0])
        self.bird.animation.repeat = True
        self.bird.animation.play()

    def render_logo(self, screen):
        image = self.textures['flappy-bird.png']
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        screen.blit(image, pygame.rect.Rect(screen.get_rect()[2] / 2 - x,
                                            screen.get_rect()[2] / 2 - y,
                                            30, 30))

    def render_button(self, screen):
        image = self.textures['play.png']
        x = image.get_rect()[2] / 2
        screen.blit(image, pygame.rect.Rect(screen.get_rect()[2] / 2 - x,
                                            screen.get_rect()[2] / 2 + 210,
                                            15, 15))

    def render_sidewalk(self, screen):
        image = self.textures['base.png']
        x = image.get_rect()[2] / 2
        screen.blit(image, pygame.rect.Rect(screen.get_rect()[2] / 2 - x,
                                            screen.get_rect()[2] / 2 + 300,
                                            15, 15))

    def change_bird_animation(self, animation):
        self.bird.animation = animation
        self.bird.animation.repeat = True
        if not self.bird.animation.is_playing():
            self.bird.animation.play()
