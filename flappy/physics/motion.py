from time import time
from flappy.scene.bird import Bird
from flappy.scene.board import Board


class MotionEngine:
    def __init__(self, gravity=1.1):
        self.last_update = time()
        self.gravity = gravity

    def update(self, board: Board):
        now = time()
        delta = now - self.last_update
        self.move_terrain(board, delta)
        self.move_bird(board.bird, delta)
        self.last_update = now

    def move_bird(self, bird: Bird, delta: float):
        distance = bird.vertical_velocity * delta - (self.gravity * delta ** 2)/2
        bird.frame.origin.y -= distance
        bird.vertical_velocity = bird.vertical_velocity - self.gravity * delta
        bird.distance_travelled += bird.horizontal_velocity * delta

    @staticmethod
    def move_terrain(board: Board, delta: float):
        distance = board.bird.horizontal_velocity * delta
        for o in board.obstacles:
            o.walls[0].origin.x -= distance
            o.walls[1].origin.x -= distance
