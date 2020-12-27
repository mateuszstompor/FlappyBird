import os
from time import sleep
from typing import Any

import pygame
from flappy.collision.detector import CollisionDetector
from flappy.core.observer.general import Observer, Subject
from flappy.gmath.frange import Frange
from flappy.gmath.point import Point
from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.scene.bird import Bird
from flappy.scene.board import Board
from flappy.scene.obstacle import Obstacle
from flappy.scene.terrain import TerrainGenerator
from flappy.score.counter import ScoreCounter
from flappy.sfx.player import Player
from flappy.textures.library import TextureLibrary
from flappy.visualizer.drawer import Drawer
from flappy.physics.motion import MotionEngine

from flappy.view.general import View
from flappy.visualizer.score import ScoreDrawer

player = None


class PlayView(View, Observer):
    def __init__(self):
        self.__score = 0

    def update(self, subject: Subject, event: Any):
        player.play('point.wav')
        self.__score = event

    def show(self):
        screen = pygame.display.set_mode([500, 500])
        running = True

        v = Drawer(screen)
        vs = ScoreDrawer(screen)
        terrain = TerrainGenerator(Frange(0.1, 0.3), 0.5, Frange(0.4, 0.9))
        engine = MotionEngine()
        detector = CollisionDetector()
        walls = [Obstacle(Rect(Point(0.6, 0.6), Size(0.1, 0.3)))]
        score = ScoreCounter()
        score.point_gained.attach(self)
        bird = Bird(Rect(Point(0.2, 0.5), Size(0.068, 0.05)), flap_velocity=0.6, horizontal_velocity=0.3,
                    vertical_velocity=0.0)
        board = Board(bird, walls)
        global player
        player = Player.with_sounds(['wing.wav', 'hit.wav', 'point.wav'])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        board.bird.flap()
                        player.play('wing.wav')
            score.update_score(board.obstacles, board.bird)
            engine.update(board)
            v.draw(board)
            vs.draw(self.__score)
            for o in board.obstacles:
                if detector.is_colliding(board.bird, o):
                    player.play('hit.wav')
            if 100 > len(board.obstacles) > 0:
                board.obstacles.append(terrain.next_obstacle(board.obstacles[-1]))
            pygame.display.flip()
        pygame.quit()
