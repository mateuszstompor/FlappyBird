from typing import List
from flappy.scene.bird import Bird
from flappy.scene.obstacle import Obstacle
from flappy.core.observer.passthrough import PassthroughSubject


class ScoreCounter:
    def __init__(self):
        self.point_gained = PassthroughSubject()
        self.score = 0

    def update_score(self, obstacles: List[Obstacle], bird: Bird):
        passed = [1 for o in obstacles if o.walls[0].origin.x + o.walls[0].size.width / 2 < bird.frame.origin.x]
        new_score = sum(passed)
        if new_score > self.score:
            self.point_gained.notify(new_score)
            self.score = new_score
