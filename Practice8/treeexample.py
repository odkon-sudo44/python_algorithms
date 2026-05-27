from __future__ import annotations
from typing import Iterable
from AlgorithmsCourse.Practice1.student_dataclass import Student
from AlgorithmsCourse.Practice2.generator import Generator
from AlgorithmsCourse.Practice8.abstracttree import AbstractTreeBasic


class TreeNode:
    value: Student
    left_child: None | TreeNode
    right_child: None | TreeNode

    def __init__(self, value, left_child: TreeNode | None = None, right_child: TreeNode | None = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self) -> str:
        return f"TreeNode(value:{self.value}, " \
               f"left:{self.left_child is not None}," \
               f" right:{self.left_child is not None})"


class BinaryTree(AbstractTreeBasic):
    __root: None | TreeNode
    __size: int

    def __init__(self, *args: Iterable[Student]):
        self.__root = None
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        if self.__root is None:
            return "[]"
        return self.__tree(self.__root, 0, '')

    def __tree(self, node: TreeNode, tab: int, prefix) -> str:
        if node is None:
            # return ' '*tab + "None\n"
            return ''
        prev = self.__tree(node.left_child, tab+2, 'l: ')
        nxt = self.__tree(node.right_child, tab+2, 'r: ')
        return prev + ' '*tab + prefix + str(node.value) + "\n" + nxt

    def insert(self, value: Student) -> None:
        if self.__root is None:
            self.__root = TreeNode(value)
            self.__size += 1
        else:
            self.__insert(self.__root, value)

    def __insert(self, node:TreeNode, value: Student):
        if value < node.value:
            if node.left_child is None:
                node.left_child = TreeNode(value)
                self.__size += 1
            else:
                self.__insert(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = TreeNode(value)
                self.__size += 1
            else:
                self.__insert(node.right_child, value)

    def find(self, value: Student) -> bool:
        pass

    def remove(self, value: Student) -> None:
        pass

    def min(self) -> Student:
        pass


if __name__ == "__main__":

    gen = Generator()
    students = [gen.generate_single() for _ in range(10)]
    for stud in students:
        print(stud)

    print('---')
    tree = BinaryTree()

    for stud in students:
        tree.insert(stud)
    print(tree)



