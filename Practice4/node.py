from Practice1.abstract_object import AbstractObject


class Node:
    """Ланка однозв'язного списку: зберігає об'єкт даних і посилання на
    наступну ланку.
    """

    def __init__(self, data: AbstractObject):
        self.data = data
        self.next: None | Node = None

    def __repr__(self):
        return repr(self.data)
