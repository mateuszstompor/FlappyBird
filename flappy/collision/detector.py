from functools import reduce

from typing import List

from flappy.gmath.rect import Rect
from flappy.scene.board import Board
from flappy.core.observer.passthrough import PassthroughSubject


class CollisionDetector:
    """
    Analyzes positions of obstacles and the bird. Notifies its
    subscribers once a collision is detected
    """
    def __init__(self):
        self.collision_notifier = PassthroughSubject()

    def detect_collision(self, board: Board):
        obstacles = [[obstacle.wall.lower, obstacle.wall.upper]
                     for obstacle in board.obstacles]
        if self.is_colliding(board.bird.frame, reduce(lambda a, b: a + b, obstacles)):
            self.collision_notifier.notify(None)

    @staticmethod
    def is_colliding(rect: Rect, against: List[Rect]) -> bool:
        return any([rect.is_overlapping(obstacle) for obstacle in against])
