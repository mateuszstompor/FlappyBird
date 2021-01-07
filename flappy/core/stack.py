from typing import Any, List, Iterable


class EmptyStack(Exception):
    """
    An exception raised when the user attempts
    to read an element from an empty stack
    """


class Stack:
    """
    List wrapper limiting its interface and providing methods
    for stack manipulation
    """
    def __init__(self):
        self.__items = []  # type: List[Any]

    def pop(self) -> Any:
        if self.__items:
            return self.__items.pop(len(self.__items)-1)
        raise EmptyStack

    def push(self, item: Any):
        self.__items.append(item)

    def clear(self):
        self.__items = []

    def top(self) -> Any:
        if self.__items:
            return self.__items[len(self.__items) - 1]
        raise EmptyStack

    def from_bottom(self) -> Iterable[Any]:
        return iter(self.__items)
