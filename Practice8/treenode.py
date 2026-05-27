from __future__ import annotations
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject


class TreeNode:
    value: AbstractObject
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
