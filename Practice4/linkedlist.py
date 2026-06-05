from typing import Iterable
from Practice1.abstract_object import AbstractObject
from Practice3.abstractstructure import AbstractStructureExtended
from Practice4.node import Node


class LinkedList(AbstractStructureExtended):

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        self.__head: None | Node = None
        self.__tail: None | Node = None
        self.__size = 0
        self.__iter_link: None | Node = None
        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.append(element)
        else:
            for element in args:
                self.append(element)


    def __node_at(self, index: int) -> Node:
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise IndexError("Out of linkedlist")
        link = self.__head
        for _ in range(index):
            link = link.next
        return link


    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        parts = []
        link = self.__head
        while link is not None:
            parts.append(repr(link.data))
            link = link.next
        return "[" + ", ".join(parts) + "]"

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.indices(self.__size)
            result = []
            for i in range(start, stop, step):
                result.append(self.__node_at(i).data)
            return result
        if isinstance(item, int):
            return self.__node_at(item).data
        raise TypeError("Index must be int or slice")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.__node_at(key).data = value
            return
        raise TypeError("Index must be int")

    def append(self, value: AbstractObject) -> None:
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def insert(self, index: int, value: AbstractObject) -> None:
        if index < 0:
            index += self.__size
        if index < 0:
            index = 0
        if index >= self.__size:
            self.append(value)
            return

        new_node = Node(value)
        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
        else:
            prev = self.__node_at(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.__size += 1

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1 or stop > self.__size:
            stop = self.__size
        if start < 0:
            start += self.__size
        if start < 0:
            start = 0
        link = self.__head
        i = 0
        while link is not None and i < stop:
            if i >= start and link.data == value:
                return i
            link = link.next
            i += 1
        raise ValueError("index: value is not exists")

    def remove(self, value: AbstractObject) -> None:
        prev = None
        link = self.__head
        while link is not None:
            if link.data == value:
                if prev is None:
                    self.__head = link.next
                    if self.__head is None:
                        self.__tail = None
                else:
                    prev.next = link.next
                    if link is self.__tail:
                        self.__tail = prev
                self.__size -= 1
                return
            prev = link
            link = link.next
        raise ValueError("remove: value is not exists")


    def __iter__(self) -> Iterable:
        self.__iter_link = self.__head
        return self

    def __next__(self) -> AbstractObject:
        if self.__iter_link is None:
            raise StopIteration("Ending linkedlist")
        data = self.__iter_link.data
        self.__iter_link = self.__iter_link.next
        return data

    def __delitem__(self, key) -> None:
        if not isinstance(key, int):
            raise TypeError("Index must be int")
        if key < 0:
            key += self.__size
        if key < 0 or key >= self.__size:
            raise IndexError("Out of linkedlist")

        if key == 0:
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None
        else:
            prev = self.__node_at(key - 1)
            target = prev.next
            prev.next = target.next
            if target is self.__tail:
                self.__tail = prev
        self.__size -= 1

    def clear(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__iter_link = None

    def copy(self) -> list[AbstractObject]:
        result = []
        link = self.__head
        while link is not None:
            result.append(link.data)
            link = link.next
        return result

    def extend(self, values: Iterable[AbstractObject]) -> None:
        for value in values:
            self.append(value)

    def pop(self, index: int = -1) -> AbstractObject:
        if self.__size == 0:
            raise IndexError("pop from empty linkedlist")
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise IndexError("Out of linkedlist")

        if index == 0:
            value = self.__head.data
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None
        else:
            prev = self.__node_at(index - 1)
            target = prev.next
            value = target.data
            prev.next = target.next
            if target is self.__tail:
                self.__tail = prev
        self.__size -= 1
        return value

    def reverse(self) -> None:
        prev = None
        link = self.__head
        self.__tail = self.__head
        while link is not None:
            nxt = link.next
            link.next = prev
            prev = link
            link = nxt
        self.__head = prev

    def count(self, value: AbstractObject) -> int:
        total = 0
        link = self.__head
        while link is not None:
            if link.data == value:
                total += 1
            link = link.next
        return total
