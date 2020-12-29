from abc import ABC, abstractmethod


class InteractionProcessor(ABC):
    @abstractmethod
    def process(self, events):
        pass
