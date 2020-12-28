from time import time
from flappy.scene.bird import Bird
from flappy.scene.board import Board


class MotionEngine:
    def __init__(self, gravity=1.1):
        self.__last_update = time()
        self.__gravity = gravity

    def update(self, board: Board):
        now = time()
        delta = now - self.__last_update
        self.move_terrain(board, delta)
        self.move_bird(board.bird, delta)
        self.__last_update = now

    def reset(self):
        self.__last_update = time()

    def move_bird(self, bird: Bird, delta: float):
        distance = bird.vertical_velocity * delta - (self.__gravity * delta ** 2)/2
        bird.frame.origin.y -= distance
        bird.vertical_velocity = bird.vertical_velocity - self.__gravity * delta
        bird.distance_travelled += bird.horizontal_velocity * delta
        bias = 20
        bird.current_angle = min((bird.vertical_velocity / bird.flap_velocity) * bird.maximal_angle + bias, bird.maximal_angle)

    @staticmethod
    def move_terrain(board: Board, delta: float):
        distance = board.bird.horizontal_velocity * delta
        for o in board.obstacles:
            o.wall.lower.origin.x -= distance
            o.wall.upper.origin.x -= distance
