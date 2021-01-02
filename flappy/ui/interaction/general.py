from abc import ABC, abstractmethod


class InteractionProcessor(ABC):
    @abstractmethod
    def responds(self, events) -> bool:
        pass

    @abstractmethod
    def allows_other(self) -> bool:
        pass
