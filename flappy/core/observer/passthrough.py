from typing import Any, Set

from flappy.core.observer.general import Subject, Observer


class PassthroughSubject(Subject):
    """
    Subject that does not contain any history
    of events and provides the subscribers only with
    the latest one
    """
    def __init__(self):
        self.__observers = set()  # type: Set[Observer]

    def detach(self, observer: Observer):
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self, event: Any):
        for observer in self.__observers:
            observer.update(self, event)

    def attach(self, observer: Observer):
        self.__observers.add(observer)

    def observers(self) -> Set[Observer]:
        return self.__observers
