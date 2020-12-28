import pygame

from pygame.surface import Surface
from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.scene.bird import Bird
from flappy.gmath.point import Point
from flappy.scene.board import Board
from flappy.scene.obstacle import Obstacle
from flappy.textures.library import TextureLibrary
from flappy.visualizer.conversion.rect import RectConverter


class Drawer:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.textures = TextureLibrary.with_images(['pipe-green.png',
                                                    'redbird-downflap.png',
                                                    'background-day.png',
                                                    'background-night.png',
                                                    'base.png'])

    def draw(self, board: Board, background):
        self.present_background(background)
        self.present_bird(board.bird)
        for o in board.obstacles:
            if Drawer.is_in_sight(o, Rect(Point(-1, 0), Size(3, 1))):
                self.present_wall(o)
        self.present_base()

    def present_bird(self, bird: Bird):
        rect = RectConverter.as_pygame(bird.frame, self.screen)
        image = bird.animation.image()
        image = pygame.transform.rotate(image, bird.current_angle)
        self.screen.blit(image, rect)

    def present_base(self):
        image = self.textures['base.png']
        x = image.get_rect()[2] / 2
        self.screen.blit(image, pygame.rect.Rect(self.screen.get_rect()[2] / 2 - x,
                                                 self.screen.get_rect()[2] / 2 + 320,
                                                 15, 15))

    def present_background(self, name='background-day.png'):
        image = self.textures.image(name)
        self.screen.blit(image, self.screen.get_rect())

    def present_wall(self, obstacle: Obstacle):
        upper, lower = obstacle.walls
        rect = RectConverter.as_pygame(lower, self.screen)
        image = self.textures.image('pipe-green.png')
        scale = (rect[2], image.get_rect()[3])
        scaled = pygame.transform.scale(image, scale)
        self.screen.blit(scaled, (rect[0], rect[1], scale[0], image.get_rect()[3]))

        image_rect = image.get_rect()
        rect = RectConverter.as_pygame(upper, self.screen)
        cropped = pygame.Surface((image_rect[2], rect.height))
        cropped.blit(image, (0, 0), (0, 0, image_rect[2], rect[3]))
        rotated_image = pygame.transform.rotate(cropped, 180)
        scale = (rect[2], rotated_image.get_rect()[3])
        scaled = pygame.transform.scale(rotated_image, scale)
        self.screen.blit(scaled, rect)

    @staticmethod
    def is_in_sight(obstacle: Obstacle, sight: Rect):
        return sight.is_overlapping(obstacle.walls[0]) or sight.is_overlapping(obstacle.walls[1]) or \
               obstacle.walls[0].is_overlapping(sight) or obstacle.walls[1].is_overlapping(sight)
