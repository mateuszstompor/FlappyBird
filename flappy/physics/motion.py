from time import time
from flappy.scene.bird import Bird
from flappy.scene.board import Board


class MotionEngine:
    def __init__(self, gravity=1.1, bird_angle_bias=20):
        self.__last_update = time()
        self.__gravity = gravity
        self.__angle_bias = bird_angle_bias

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
        counted_angle = (bird.vertical_velocity / bird.flap_velocity) * bird.maximal_angle
        biased = counted_angle + self.__angle_bias
        bird.current_angle = min(biased, bird.maximal_angle)

    @staticmethod
    def move_terrain(board: Board, delta: float):
        distance = board.bird.horizontal_velocity * delta
        for obstacle in board.obstacles:
            obstacle.wall.lower.origin.x -= distance
            obstacle.wall.upper.origin.x -= distance
