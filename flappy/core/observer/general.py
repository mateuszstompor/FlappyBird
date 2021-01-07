from typing import Any, Set
from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interface of a class that is capable of receiving events
    from the subjects that the class is subscribed to
    """
    @abstractmethod
    def update(self, subject, event: Any):
        pass

    def terminate(self):
        pass


class Subject(ABC):
    """
    Interface of a class that produces events based on
    its defined criterion and notifies all observers once
    a new event occurs
    """
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, event: Any):
        pass

    @abstractmethod
    def observers(self) -> Set[Observer]:
        pass
