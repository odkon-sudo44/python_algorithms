from __future__ import annotations
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from dataclasses import dataclass


@dataclass
class Node:
    data: AbstractObject
    next: None | Node
