from typing import Any


class EmptyStack(Exception):
    pass


class Stack:
    def __init__(self):
        self.__items = []

    def pop(self) -> Any:
        if self.__items:
            return self.__items.pop(len(self.__items)-1)
        raise EmptyStack

    def push(self, item: Any):
        self.__items.append(item)

    def clear(self):
        self.__items = []

    def top(self):
        if self.__items:
            return self.__items[len(self.__items) - 1]
        raise EmptyStack

    def from_bottom(self):
        return iter(self.__items)
