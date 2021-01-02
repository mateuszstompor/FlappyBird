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
    def __init__(self):
        self.textures = TextureLibrary.with_images(['pipe-green.png',
                                                    'pipe-red.png',
                                                    'redbird-downflap.png',
                                                    'background-day.png',
                                                    'background-night.png',
                                                    'base.png'])

    def draw(self, surface: Surface, board: Board):
        self.present_bird(surface, board.bird)
        for index, obstacle in enumerate(board.obstacles):
            if Drawer.is_in_sight(obstacle, Rect(Point(-1, 0), Size(3, 1))):
                image_name = 'pipe-red.png' if index % 5 == 0 and index > 0 else 'pipe-green.png'
                self.present_wall(surface, obstacle, image_name)

    @staticmethod
    def present_bird(surface: Surface, bird: Bird):
        rect = RectConverter.as_pygame(bird.frame, surface)
        image = pygame.transform.rotate(bird.animation.data(), bird.state.angle)
        surface.blit(image, rect)

    def present_wall(self, surface: Surface, obstacle: Obstacle, image_name: str):
        upper, lower = obstacle.wall
        rect = RectConverter.as_pygame(lower, surface)
        image = self.textures[image_name]
        scale = (rect[2], image.get_rect()[3])
        scaled = pygame.transform.scale(image, scale)
        surface.blit(scaled, (rect[0], rect[1], scale[0], image.get_rect()[3]))

        image_rect = image.get_rect()
        rect = RectConverter.as_pygame(upper, surface)
        cropped = pygame.Surface((image_rect[2], rect.height))
        cropped.blit(image, (0, 0), (0, 0, image_rect[2], rect[3]))
        rotated_image = pygame.transform.rotate(cropped, 180)
        scale = (rect[2], rotated_image.get_rect()[3])
        scaled = pygame.transform.scale(rotated_image, scale)
        surface.blit(scaled, rect)

    @staticmethod
    def is_in_sight(obstacle: Obstacle, sight: Rect):
        return sight.is_overlapping(obstacle.wall.upper) or \
               sight.is_overlapping(obstacle.wall.lower) or \
               obstacle.wall.upper.is_overlapping(sight) or \
               obstacle.wall.lower.is_overlapping(sight)
