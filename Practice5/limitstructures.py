from typing import Iterable

from Practice1.abstract_object import AbstractObject
from Practice1.notebook_dataclass import Notebook
from Practice3.structureexamples import ArrayParts
from Practice4.linkedlist import LinkedList
from Practice5.abstractlimitstructure import AbstractStack, AbstractQueue, AbstractDeque


class ArrayStack(AbstractStack):

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        self.__data = ArrayParts()
        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.push(element)
        else:
            for element in args:
                self.push(element)

    def push(self, value: Notebook) -> None:
        self.__data.append(value)

    def pop(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    def top(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("top from empty stack")
        return self.__data[len(self.__data) - 1]

    def __len__(self) -> int:
        return len(self.__data)

    def __repr__(self) -> str:
        return "Stack(bottom -> top): " + repr(self.__data)


class LinkedPriorityQueue(AbstractQueue):

    def __init__(self, *args: Notebook | Iterable[Notebook]):
        self.__data = LinkedList()
        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.enqueue(element)
        else:
            for element in args:
                self.enqueue(element)

    @staticmethod
    def __priority(item: Notebook) -> int:
        return item.memory

    def enqueue(self, value: Notebook) -> None:
        target = self.__priority(value)
        position = len(self.__data)          # за замовчуванням - у кінець
        for i, existing in enumerate(self.__data):
            if self.__priority(existing) < target:
                position = i
                break
        self.__data.insert(position, value)

    def dequeue(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("dequeue from empty queue")
        return self.__data.pop(0)

    def top(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("top from empty queue")
        return self.__data[0]

    def __len__(self) -> int:
        return len(self.__data)

    def __repr__(self) -> str:
        return "PriorityQueue(high -> low RAM): " + repr(self.__data)


class DequeDeque(AbstractDeque):

    def __init__(self, *args: Notebook | Iterable[Notebook]):
        from collections import deque
        self.__data = deque()
        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.push_last(element)
        else:
            for element in args:
                self.push_last(element)

    def push_first(self, value: Notebook) -> None:
        self.__data.appendleft(value)

    def push_last(self, value: Notebook) -> None:
        self.__data.append(value)

    def pop_first(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("pop_first from empty deque")
        return self.__data.popleft()

    def pop_last(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("pop_last from empty deque")
        return self.__data.pop()

    def top_first(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("top_first from empty deque")
        return self.__data[0]

    def top_last(self) -> Notebook:
        if len(self.__data) == 0:
            raise IndexError("top_last from empty deque")
        return self.__data[-1]

    def __len__(self) -> int:
        return len(self.__data)

    def __repr__(self) -> str:
        return "Deque(first -> last): [" + ", ".join(repr(x) for x in self.__data) + "]"
