from abc import ABC, abstractmethod


class InteractionProcessor(ABC):  # pylint: disable=R0903
    @abstractmethod
    def process(self, events):
        pass
