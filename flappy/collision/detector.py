from flappy.scene.bird import Bird
from flappy.scene.obstacle import Obstacle


class CollisionDetector:
    @staticmethod
    def is_colliding(bird: Bird, obstacle: Obstacle):
        return bird.frame.is_overlapping(obstacle.walls[0]) or \
               bird.frame.is_overlapping(obstacle.walls[1])
