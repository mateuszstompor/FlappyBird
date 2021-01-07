from abc import ABC, abstractmethod


class InteractionProcessor(ABC):
    """
    Interface describing an input handler. Based on the list of
    provided events the handler can react, notify its listeners
    and prevent other handlers from receiving the event if it
    declares itself as greedy
    """
    @abstractmethod
    def responds(self, events) -> bool:
        pass

    @abstractmethod
    def allows_other(self) -> bool:
        pass
