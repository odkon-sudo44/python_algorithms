from Practice3.abstractstructure import AbstractStructureBasic, AbstractStructureExtended
from Practice1.abstract_object import AbstractObject
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
        elif args and isinstance(args[0], Iterable):
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


class ArrayParts(AbstractStructureExtended):
    """Динамічний масив для зберігання об'єктів Notebook без використання
    готових методів list. Дані зберігаються у внутрішньому буфері, доступ і
    зміна виконуються через __getitem__/__setitem__, а зайва ємність
    резервується наперед і нарощується по мірі заповнення.

    Внутрішній буфер __array завжди має довжину __reserved (частина комірок
    після __size порожні і містять None). __size - реальна кількість елементів.
    """

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        """Створення порожнього масиву або наповнення його з переданих даних.

        Підтримує два варіанти виклику:
            ArrayParts(obj1, obj2, ...)      - окремі об'єкти через кому
            ArrayParts([obj1, obj2, ...])    - одна ітерируєма структура
        :param args: окремі об'єкти AbstractObject або одна Iterable з ними
        """
        self.__start_size = 10
        self.__array: list[AbstractObject | None] = [None] * self.__start_size
        self.__size = 0                 # реальна кількість збережених елементів
        self.__reserved = self.__start_size   # повна довжина буфера (зайняті + резерв)
        self.__iter_index = 0           # позиція для __next__

        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.append(element)
        else:
            for element in args:
                self.append(element)

    # ------------------------------------------------------------------ #
    #  Внутрішні допоміжні методи                                        #
    # ------------------------------------------------------------------ #
    def __size_extending(self) -> None:
        """Подвоєння ємності внутрішнього буфера зі збереженням наявних
        елементів. Викликається, коли всі зарезервовані комірки заповнені.
        """
        new_reserved = (self.__reserved if self.__reserved > 0 else self.__start_size) * 2
        new_array: list[AbstractObject | None] = [None] * new_reserved
        for i in range(self.__size):
            new_array[i] = self.__array[i]      # перенесення наявних елементів у новий буфер
        self.__array = new_array
        self.__reserved = new_reserved

    def __normalize_index(self, index: int) -> int:
        """Приводить від'ємний індекс до додатнього і перевіряє межі.
        :param index: цілий індекс (можливо від'ємний)
        :return: коректний невід'ємний індекс у межах [0, __size)
        """
        if index < 0:
            index += self.__size
        if index < 0 or index >= self.__size:
            raise IndexError("Out of index")
        return index

    # ------------------------------------------------------------------ #
    #  Базовий рівень                                                    #
    # ------------------------------------------------------------------ #
    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return "[" + ", ".join(repr(self.__array[i]) for i in range(self.__size)) + "]"

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.indices(self.__size)
            result = []
            for i in range(start, stop, step):
                result.append(self.__array[i])
            return result
        if isinstance(item, int):
            return self.__array[self.__normalize_index(item)]
        raise TypeError("Index must be int or slice")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.__array[self.__normalize_index(key)] = value
            return
        raise TypeError("Index must be int")

    def append(self, value: AbstractObject) -> None:
        if self.__size >= self.__reserved:
            self.__size_extending()     # буфер заповнено - подвоюємо
        self.__array[self.__size] = value
        self.__size += 1

    def insert(self, index: int, value: AbstractObject) -> None:
        # дозволяємо вставку в кінець (index == __size) і нормалізацію від'ємних
        if index < 0:
            index += self.__size
        if index < 0:
            index = 0
        if index > self.__size:
            index = self.__size

        if self.__size >= self.__reserved:
            self.__size_extending()
        # зсув елементів вправо, починаючи з кінця, щоб звільнити позицію index
        for i in range(self.__size, index, -1):
            self.__array[i] = self.__array[i - 1]
        self.__array[index] = value
        self.__size += 1

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1 or stop > self.__size:
            stop = self.__size
        if start < 0:
            start += self.__size
        for i in range(max(0, start), stop):
            if self.__array[i] == value:
                return i
        raise ValueError("index: value is not exists")

    def remove(self, value: AbstractObject) -> None:
        pos = None
        for i in range(self.__size):
            if self.__array[i] == value:
                pos = i
                break
        if pos is None:
            raise ValueError("remove: value is not exists")
        # зсув наступних елементів на одну позицію вліво
        for i in range(pos, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1

    # ------------------------------------------------------------------ #
    #  Розширений рівень                                                 #
    # ------------------------------------------------------------------ #
    def __iter__(self) -> Iterable:
        self.__iter_index = 0
        return self

    def __next__(self) -> AbstractObject:
        if self.__iter_index >= self.__size:
            raise StopIteration("Ending elements")
        result = self.__array[self.__iter_index]
        self.__iter_index += 1
        return result

    def __delitem__(self, key) -> None:
        index = self.__normalize_index(key)
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1

    def clear(self) -> None:
        self.__array = [None] * self.__start_size
        self.__reserved = self.__start_size
        self.__size = 0
        self.__iter_index = 0

    def copy(self) -> list[AbstractObject]:
        return [self.__array[i] for i in range(self.__size)]

    def extend(self, values: Iterable[AbstractObject]) -> None:
        for value in values:
            self.append(value)

    def pop(self, index: int = -1) -> AbstractObject:
        if self.__size == 0:
            raise IndexError("pop from empty structure")
        index = self.__normalize_index(index)
        value = self.__array[index]
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1
        return value

    def reverse(self) -> None:
        left, right = 0, self.__size - 1
        while left < right:
            self.__array[left], self.__array[right] = self.__array[right], self.__array[left]
            left += 1
            right -= 1

    def count(self, value: AbstractObject) -> int:
        total = 0
        for i in range(self.__size):
            if self.__array[i] == value:
                total += 1
        return total