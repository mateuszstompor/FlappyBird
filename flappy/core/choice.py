from random import randrange
from typing import Any, List


class WheelChoice:
    """
    An iterator, similar to itertools.cycle providing methods to get
    the next element as well as current
    """
    def __init__(self, collection: List[Any]):
        self.__collection = collection
        self.__current = randrange(0, len(collection))

    def __step(self):
        self.__current = (self.__current + 1) % len(self.__collection)

    def __iter__(self):
        return self

    def __next__(self):
        self.__step()
        return self.item()

    def item(self) -> Any:
        return self.__collection[self.__current]
