from typing import Any, List

from flappy.core.observer.general import Subject, Observer


class PassthroughSubject(Subject):
    def __init__(self):
        self.observers = []  # type: List[Observer]

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, event: Any):
        for o in self.observers:
            o.update(self, event)

    def attach(self, observer: Observer):
        self.observers.append(observer)
