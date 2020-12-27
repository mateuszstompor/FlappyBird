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
        self.textures = TextureLibrary.with_images(['pipe-green.png', 'redbird-downflap.png'])

    def draw(self, board: Board):
        self.screen.fill((255, 255, 255))
        self.present_bird(board.bird)
        for o in board.obstacles:
            if Drawer.is_in_sight(o, Rect(Point(0, 0), Size(1, 1))):
                self.present_wall(o)

    def present_bird(self, bird: Bird):
        rect = RectConverter.as_pygame(bird.frame, self.screen)
        image = self.textures.image('redbird-downflap.png')
        self.screen.blit(image, rect)

    def present_wall(self, obstacle: Obstacle):
        upper, lower = obstacle.walls
        rect = RectConverter.as_pygame(lower, self.screen)
        image = self.textures.image('pipe-green.png')
        self.screen.blit(image, rect)

        image_rect = image.get_rect()
        rect = RectConverter.as_pygame(upper, self.screen)
        cropped = pygame.Surface((image_rect[2], rect.height))
        cropped.blit(image, (0, 0), (0, 0, image_rect[2], rect[3]))
        rotated_image = pygame.transform.rotate(cropped, 180)
        self.screen.blit(rotated_image, rect)

    @staticmethod
    def is_in_sight(obstacle: Obstacle, sight: Rect):
        return sight.is_overlapping(obstacle.walls[0]) or sight.is_overlapping(obstacle.walls[1])
