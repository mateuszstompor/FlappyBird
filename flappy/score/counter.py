from typing import List
from flappy.scene.bird import Bird
from flappy.scene.obstacle import Obstacle
from flappy.core.observer.general import Subject
from flappy.core.observer.passthrough import PassthroughSubject


class ScoreCounter:
    def __init__(self):
        self.point_gained = PassthroughSubject()  # type: Subject
        self.score = 0

    def update_score(self, obstacles: List[Obstacle], bird: Bird):
        new_score = self.count_passed(obstacles, bird)
        if new_score > self.score:
            self.point_gained.notify(new_score)
            self.score = new_score

    @staticmethod
    def count_passed(obstacles: List[Obstacle], bird: Bird):
        return sum([1 for o in obstacles if o.walls[0].origin.x + o.walls[0].size.width / 2 < bird.frame.origin.x])

    def reset(self):
        self.score = 0
