from typing import Any, Set
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject, event: Any):
        pass

    def terminate(self):
        pass


class Subject(ABC):
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
