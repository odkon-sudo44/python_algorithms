from AlgorithmsCourse.Practice3.abstractstructure import AbstractStructureBasic, AbstractStructureExtended
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject
from collections.abc import Iterable


class StructureExample(AbstractStructureExtended):
    """Класс реалізації структури на основі list і основних його методів
    """

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        """Ініціалізація окремими значеннями або ітерируємою структурою (list, tuple, ...) з даними
        :param args: Кортеж аргументів змінної довжини з об'єктами або структурою (Iterable) з даними
        """
        self._list: list[AbstractObject] = []        # внутрішній масив для зберігання даних
        self.__iter_index = 0   # індекс ітератора

        if args and isinstance(args[0], AbstractObject):
            for element in args:
                self._list.append(element)         # додавання окремих перелічених об'єктів до внутрішнього масиву
        if args and isinstance(args[0], Iterable):
            self._list.extend(args[0])             # додавання елементів структури до внутрішнього масиву

    def __len__(self) -> int:
        return len(self._list)

    def __repr__(self) -> str:
        return str(self._list)

    def __getitem__(self, item):
        try:
            return self._list[item]
        except IndexError:
            raise IndexError("getitem: index out of range")  # Виключення про вихід за межі існуючих індексів

    def __setitem__(self, key, value):
        try:
            self._list[key] = value
        except IndexError:
            raise IndexError("setitem: index out of range")

    def append(self, value: AbstractObject) -> None:
        self._list.append(value)

    def insert(self, index: int, value: AbstractObject) -> None:
        self._list.insert(index, value)

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = len(self._list)
        try:
            return self._list.index(value, start, stop)
        except IndexError:
            raise IndexError("index: Для наочності ")

    def remove(self, value: AbstractObject) -> None:
        try:
            self._list.remove(value)
        except ValueError:
            raise ValueError("remove: value is not exists")     # Помилка за відсутності вказаного об'єкта в структурі

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> AbstractObject:
        if self.__iter_index >= len(self._list):
            raise StopIteration("Ending elements")
        result = self._list[self.__iter_index]
        self.__iter_index += 1
        return result

    def __delitem__(self, key):
        pass

    def extend(self, values: Iterable[AbstractObject]) -> None:
        pass

    def clear(self) -> None:
        pass

    def pop(self, index: int = -1) -> AbstractObject:
        pass

    def copy(self) -> list[AbstractObject]:
        pass

    def reverse(self) -> None:
        pass

    def count(self, value: AbstractObject) -> int:
        pass


class ArrayParts(AbstractStructureBasic):
    __array: list[AbstractObject|None]
    __size: int
    __reserved: int

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        self.__array = [None] * 10  # [None, None, None, None, None, None, None, None, None, None]
        self.__size = 0
        self.__reserved = 10        # Загальний розмір масиву - кількість зберігаємих об'єктів + зарезервовані місця

        if len(args) == 1 and isinstance(args, Iterable):
            if len(args[0]) >= self.__reserved:
                self.__size_extending(self.__reserved + len(args[0]))
            for element in args[0]:
                self.append(element)

    def __size_extending(self, max_size=-1) -> None:
        """
        Метод розширення масиву вдвічі або більше, якщо немає пустих елементів
        :param max_size: скільки елементів буде містити
        :return:
        """
        # Бажано збільшувати кратно до початкового розміру і на кількість з запасом
        # Наприклад: зараз 10, буде 51 значень -> розширити на 10*2*2*2, тобто 80 елементів
        pass

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        pass

    def __getitem__(self, item):
        if isinstance(item, int) and item >= self.__size:
            raise IndexError("Out of index")

        if isinstance(item, slice):
            if item.step is None or item.step >= 0:
                if item.stop is None:
                    item = slice(item.start, self.__size, item.step)
                elif item.stop > self.__size:
                    raise IndexError("Out of index")
            else:
                if item.start is None:
                    item = slice(
                        self.__size-1 if item.start is None else item.start, item.stop, item.step)
                elif item.start > self.__size-1:
                    raise IndexError("Out of index")
        return self.__array[item]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if 0 <= key < self.__size:
                self.__array[key] = value
                return
        raise IndexError("Out of index")

    def append(self, value: AbstractObject) -> None:
        if self.__size >= self.__reserved - 1:
            self.__size_extending()     # розширення масива вдвічі, якщо вичерпано всі зарезервовані місця
        self.__array[self.__size] = value
        self.__size += 1

    def insert(self, index: int, value: AbstractObject) -> None:
        pass

    def index(self, value: AbstractObject, start: int, stop: int) -> int:
        pass

    def remove(self, value: AbstractObject) -> None:
        pass

