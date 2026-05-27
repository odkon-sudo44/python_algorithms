from AlgorithmsCourse.Practice1.abstract_object import AbstractObject


class Node:

    def __init__(self, data: AbstractObject):
        self.data = data
        self.next: None | Node = None   # from Python 3.11
                                        # type: [Node, None]

    def __repr__(self):
        return self.data