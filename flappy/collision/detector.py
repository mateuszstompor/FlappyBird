from flappy.scene.bird import Bird
from flappy.scene.board import Board
from flappy.scene.obstacle import Obstacle
from flappy.core.observer.passthrough import PassthroughSubject


class CollisionDetector:
    def __init__(self):
        self.collision_notifier = PassthroughSubject()

    def check_collisions(self, board: Board):
        for o in board.obstacles:
            if self.is_colliding(board.bird, o):
                self.collision_notifier.notify(None)

    @staticmethod
    def is_colliding(bird: Bird, obstacle: Obstacle):
        return bird.frame.is_overlapping(obstacle.walls[0]) or \
               bird.frame.is_overlapping(obstacle.walls[1])
