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
        distance = bird.state.velocity * delta - (self.__gravity * delta ** 2)/2
        bird.frame.origin.y -= distance
        bird.state.velocity = bird.state.velocity - self.__gravity * delta
        bird.state.distance += bird.flight_velocity.horizonatal * delta
        angle = (bird.state.velocity / bird.flight_velocity.vertical) * bird.maximal_angle
        biased_angle = angle + self.__angle_bias
        bird.state.angle = min(biased_angle, bird.maximal_angle)

    @staticmethod
    def move_terrain(board: Board, delta: float):
        distance = board.bird.flight_velocity.horizonatal * delta
        for obstacle in board.obstacles:
            obstacle.wall.lower.origin.x -= distance
            obstacle.wall.upper.origin.x -= distance
