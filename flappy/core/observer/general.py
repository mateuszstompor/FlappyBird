from typing import Any
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject, event: Any):
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
