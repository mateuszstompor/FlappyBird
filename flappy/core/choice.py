from random import randrange
from typing import Any, List


class WheelChoice:
    def __init__(self, collection: List[Any]):
        self.__collection = collection
        self.__current = randrange(0, len(collection))

    def __step(self):
        self.__current = (self.__current + 1) % len(self.__collection)

    def next_item(self) -> Any:
        self.__step()
        return self.item()

    def item(self) -> Any:
        return self.__collection[self.__current]
