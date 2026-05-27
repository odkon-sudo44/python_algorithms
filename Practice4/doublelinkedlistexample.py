from __future__ import annotations
from typing import Iterable
from dataclasses import dataclass
from AlgorithmsCourse.Practice1.student_dataclass import Student
from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructureBasic
from AlgorithmsCourse.Practice2.generator import Generator


@dataclass
class DoubleNode:
    data: Student
    next: None | DoubleNode = None
    prev: None | DoubleNode = None


class DoubleLinkedList(AbstractStructureBasic):

    def __init__(self, *args: Iterable[Student]):
        self.__head: None | DoubleNode = None
        self.__tail: None | DoubleNode = None
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        content = ''
        current_node = self.__head
        while current_node is not None:
            content += str(current_node.data) + ', '
            current_node = current_node.next

        if len(content) > 1:
            content = content[:-2]

        return '[' + content + ']'

    def __getitem__(self, key) -> Student:
        pass

    def __setitem__(self, key, value):
        pass

    def append(self, value: Student) -> None:
        if self.__head is None:
            tmp_node = DoubleNode(value)
            self.__head = tmp_node
        else:
            # current_node = self.__head
            # while current_node.next is not None:
            #     current_node = current_node.next
            #
            # tmp_node = DoubleNode(value)
            # current_node.next = tmp_node
            # tmp_node.prev = current_node

            tmp_node = DoubleNode(value, None, self.__tail)
            # tmp_node.prev = self.__tail

            self.__tail.next = tmp_node

        self.__tail = tmp_node
        self.__size += 1

    def insert(self, index: int, value: Student) -> None:
        pass

    def index(self, value: Student, start: int = 0, stop: int = -1) -> int:
        pass

    def remove(self, value: Student) -> None:
        pass


if __name__ == "__main__":

    gen = Generator()
    st = [gen.generate_single() for _ in range(5)]
    print(st)

    dll = DoubleLinkedList()
    print(dll)

    dll.append(st[0])
    print(dll)

    dll.append(st[1])
    dll.append(st[2])
    print(dll)

