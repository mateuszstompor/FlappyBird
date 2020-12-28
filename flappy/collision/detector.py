from flappy.scene.bird import Bird
from flappy.scene.board import Board
from flappy.scene.obstacle import Obstacle
from flappy.core.observer.passthrough import PassthroughSubject


class CollisionDetector:
    def __init__(self):
        self.collision_notifier = PassthroughSubject()

    def check_collisions(self, board: Board):
        colliding_objects = [o for o in board.obstacles if self.is_colliding(board.bird, o)]
        for o in colliding_objects:
            self.collision_notifier.notify([o, board.bird])

    @staticmethod
    def is_colliding(bird: Bird, obstacle: Obstacle):
        return bird.frame.is_overlapping(obstacle.wall.upper) or \
               bird.frame.is_overlapping(obstacle.wall.lower)
