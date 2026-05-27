from typing import Iterable
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructureExtended
from AlgorithmsCourse.Practice4.node import Node


class LinkedList(AbstractStructureExtended):

    def __init__(self, *args: Iterable[AbstractObject]):
        self.__head = None  # посилання на перший елемент зв'язаного списку
        self.__tail = None  # посилання на останній елемент зв'язаного списку, актуальний для виключення перебору всіх елементів при додаванні нового елемента в кінець списка
        self.__size = 0
        self.__iter_link = self.__head
        if args and isinstance(args, Iterable):
            for element in args[0]:
                self.append(element)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        pass

    def __getitem__(self, item):
        if isinstance(item, slice):
            raise NotImplemented

        # some text
        link = self.__head
        counter = 0
        while link is not None and counter < item:
            link = link.next
            counter += 1

        if link is not None:
            return link.data
        raise IndexError("Out of linkedlist")

    def __setitem__(self, key, value):
        pass

    def append(self, value: AbstractObject) -> None:
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(value)
            self.__tail = self.__tail.next
        self.__size += 1

    def insert(self, index: int, value: AbstractObject) -> None:
        pass

    def index(self, value: AbstractObject, start: int, stop: int) -> int:
        pass

    def remove(self, value: AbstractObject) -> None:
        pass

    # Extended part

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> AbstractObject:
        if isinstance(self.__iter_link, Node):
            self.__iter_link = self.__iter_link.next
            return self.__iter_link.data
        raise StopIteration("Ending linkedlist")


    def clear(self) -> None:
        pass

    def copy(self) -> list[AbstractObject]:
        pass

    def __delitem__(self, key) -> None:
        pass

    def extend(self, values: Iterable[AbstractObject]) -> None:
        pass

    def pop(self, index: int) -> AbstractObject:
        pass

    def reverse(self) -> None:
        pass

    def count(self, value: AbstractObject) -> int:
        pass
