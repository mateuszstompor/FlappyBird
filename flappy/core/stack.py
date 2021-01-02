from typing import Any


class Stack:
    def __init__(self):
        self.__items = []

    def pop(self) -> Any:
        return self.__items.pop(len(self.__items)-1)

    def push(self, item: Any):
        self.__items.append(item)

    def clear(self):
        self.__items = []

    def top(self):
        return self.__items[len(self.__items) - 1]

    def from_top(self):
        return iter(self.__items[::-1])

    def from_bottom(self):
        return iter(self.__items)

    def __bool__(self):
        return bool(self.__items)

    def __len__(self):
        return len(self.__items)
