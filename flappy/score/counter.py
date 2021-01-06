from typing import List
from flappy.scene.bird import Bird
from flappy.scene.obstacle import Obstacle
from flappy.core.observer.general import Subject
from flappy.core.observer.passthrough import PassthroughSubject


class ScoreCounter:
    def __init__(self):
        self.point_gained = PassthroughSubject()  # type: Subject
        self.__score = 0

    def update_score(self, obstacles: List[Obstacle], bird: Bird):
        new_score = self.count_passed(obstacles, bird)
        if new_score > self.__score:
            self.point_gained.notify(new_score)
            self.__score = new_score

    def score(self) -> int:
        return self.__score

    def reset(self):
        self.__score = 0

    @staticmethod
    def count_passed(obstacles: List[Obstacle], bird: Bird) -> int:
        return sum([1 for obstacle in obstacles
                    if obstacle.wall.upper.origin.x < bird.frame.origin.x])
