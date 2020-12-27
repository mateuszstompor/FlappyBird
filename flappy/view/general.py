from abc import ABC
from abc import abstractmethod


class View(ABC):
    @abstractmethod
    def show(self):
        pass
