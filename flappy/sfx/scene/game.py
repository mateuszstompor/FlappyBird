from typing import Any

from flappy.core.observer.general import Observer
from flappy.sfx.player import Player


class GameAudio(Observer):
    """
    Listens for different kinds of events happening during
    the game and playing appropriate sound effects
    """
    def __init__(self, flap_subject, collision_subject, score_subject):
        self.player = Player.with_sounds(['wing.wav', 'hit.wav', 'point.wav'])
        self.flap_subject = flap_subject
        self.collision_subject = collision_subject
        self.score_subject = score_subject
        self.attach([self.flap_subject, self.collision_subject, self.score_subject])

    def update(self, subject, event: Any):
        if subject is self.flap_subject:
            self.player.play('wing.wav')
        elif subject is self.collision_subject:
            self.player.play('hit.wav')
        else:
            self.player.play('point.wav')

    def attach(self, subjects):
        for subject in subjects:
            subject.attach(self)
