import pygame

from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.scene.bird import Bird
from flappy.view.general import View
from flappy.gmath.point import Point
from flappy.view.play import PlayView
from flappy.visualizer.drawer import Drawer
from flappy.animation.store import AnimationStore
from flappy.textures.library import TextureLibrary


class LandingView(View):
    def __init__(self):
        self.screen = pygame.display.set_mode([285, 500])
        self.board_drawer = Drawer(self.screen)
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

    def render_logo(self):
        image = self.textures['flappy-bird.png']
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        self.screen.blit(image, pygame.rect.Rect(self.screen.get_rect()[2] / 2 - x,
                                                 self.screen.get_rect()[2] / 2 - y,
                                                 30, 30))

    def render_button(self):
        image = self.textures['play.png']
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        self.screen.blit(image, pygame.rect.Rect(self.screen.get_rect()[2] / 2 - x,
                                                 self.screen.get_rect()[2] / 2 + 210,
                                                 15, 15))

    def render_sidewalk(self):
        image = self.textures['base.png']
        x = image.get_rect()[2] / 2
        y = image.get_rect()[3] / 2
        self.screen.blit(image, pygame.rect.Rect(self.screen.get_rect()[2] / 2 - x,
                                                 self.screen.get_rect()[2] / 2 + 300,
                                                 15, 15))

    def change_background(self):
        pass

    def change_bird_animation(self, animation):
        self.bird.animation = animation
        self.bird.animation.repeat = True
        if not self.bird.animation.is_playing():
            self.bird.animation.play()

    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        animation = self.available_animations[self.current]
                        animation.repeat = False
                        PlayView(animation, self.backgrounds[self.chosen_background]).show()
                    elif event.key == pygame.K_1:
                        self.current = (self.current + 1) % 3
                        self.change_bird_animation(self.available_animations[self.current])
                    elif event.key == pygame.K_2:
                        self.chosen_background = (self.chosen_background + 1) % 2
            self.board_drawer.present_background(self.backgrounds[self.chosen_background])
            self.render_logo()
            self.render_sidewalk()
            self.render_button()
            self.board_drawer.present_bird(self.bird)
            pygame.display.flip()
