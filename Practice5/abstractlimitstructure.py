from abc import ABC, abstractmethod
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject


class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: AbstractObject) -> None:
        ...

    @abstractmethod
    def pop(self) -> AbstractObject:
        ...

    @abstractmethod
    def top(self) -> AbstractObject:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...


class AbstractQueue(ABC):

    @abstractmethod
    def enqueue(self, value: AbstractObject) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> AbstractObject:
        ...

    @abstractmethod
    def top(self) -> AbstractObject:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...


class AbstractDeque(ABC):

    @abstractmethod
    def push_first(self, value: AbstractObject) -> None:
        ...

    @abstractmethod
    def push_last(self, value: AbstractObject) -> None:
        ...

    @abstractmethod
    def pop_first(self) -> AbstractObject:
        ...

    @abstractmethod
    def pop_last(self) -> AbstractObject:
        ...

    @abstractmethod
    def top_first(self) -> AbstractObject:
        ...

    @abstractmethod
    def top_last(self) -> AbstractObject:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
