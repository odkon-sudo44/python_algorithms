from abc import ABC, abstractmethod
from collections.abc import Iterable
from AlgorithmsCourse.Practice1.abstract_object import AbstractObject


class AbstractStructureBasic(ABC):
    """Абстрактний клас - шаблон класу з переліком необхідних до реалізації базових методів структур даних без самої їх
    реалізації"""

    @abstractmethod
    def __init__(self, *args: Iterable[AbstractObject]):
        """
        Метод ініціалізації класу, його властивостей і наповнення його елементами структури, переданої в параметрі args
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Повертає кількість елементів структури
        :return: Кількість елементів
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Повертає перелік і зміст елементів структури у вигляді рядка
        :return: Рядок зі значеннями елементів структури
        """
        pass

    @abstractmethod
    def __getitem__(self, key) -> AbstractObject:
        """
        Метод отримання значення елемента структури за індексом
            value = struct[key]
        :param key: Ціле число(індекс) або зріз(діапазон чисел)
        :return: Значення елемента по вказаному ключу або IndexError
        """
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        """
        Метод зміни значення елемента структури по ключу
            struct[key] = value
        :param key: Ключ вибору елемента структури
        :param value: Нове значення елемента структури
        :return: None або IndexError у разі відсутності ключа
        """
        pass

    @abstractmethod
    def append(self, value: AbstractObject) -> None:
        """
        Метод вставки нового елемента структури в кінець, якщо це передбачено логікою структури
        :param value: Значення нового елемента структури
        :return: None
        """
        pass

    @abstractmethod
    def insert(self, index: int, value: AbstractObject) -> None:
        """
        Метод вставки нового елемента у вказану позицію структури зі зміщенням поточної і наступних (якщо це передбачено логікою структури)
        :param index: Позиція для вставки нового елемента
        :param value: Значення нового елемента структури
        :return: None
        """
        pass

    @abstractmethod
    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        """
        Метод пошуку значення в структурі з поверненням її індексу
        :param value: Значення елемента, що шукається
        :param start: Початкова позиція пошуку
        :param stop: Кінцева позиція пошуку
        :return: Позиція знайденого значення або IndexError
        """
        pass

    @abstractmethod
    def remove(self, value: AbstractObject) -> None:
        """
        Метод видалення вказаного значення зі структури з сувом наступних елементів
        :param value: Значення, що видаляється з структури
        :return: None або ValueError
        """
        pass


class AbstractStructureExtended(AbstractStructureBasic):
    # Розширений набір методів

    @abstractmethod
    def clear(self) -> None:
        """
        Метод видалення всіх елементів структури
        :return: None
        """
        pass

    @abstractmethod
    def copy(self) -> list[AbstractObject]:
        """
        Метод копіювання всіх елементів структури у новий list
        :return: list з поточних елементів структури
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterable:
        """
        ПОвертає об'єкт-ітератор
        :return: Об'єкт-ітератор
        """
        pass

    @abstractmethod
    def __next__(self) -> AbstractObject:
        """
        Метод визначає правила перебору елементів структури і наступний елемент
        :return: Наступний елемент  структури або виключення StopIteration, якщо всі перераховано
        """
        pass

    @abstractmethod
    def __delitem__(self, key) -> None:
        """
        Метод видалення елемента структури по ключу:
            del struct[key]
        :param key: Значення або позиція елемента структури зі зміщенням наступних елементів на позицію
        :return:
        """
        pass

    @abstractmethod
    def extend(self, values: Iterable[AbstractObject]) -> None:
        """
        Метод вставки сукупності елементів з вказаної структури
        :param values: Структура, елементи якої додаються в поточну
        :return: None
        """
        pass

    @abstractmethod
    def pop(self, index: int) -> AbstractObject:
        """
        Метод вилучення останього або вказаного елемента структури
        :param index: Необов'язковий індекс елемента
        :return: Значення еелемента, що вилучено з структури
        """
        pass

    @abstractmethod
    def reverse(self) -> None:
        """
        Метод, що змінює порядок слідування структури на протилежний
        :return: None
        """
        pass

    @abstractmethod
    def count(self, value: AbstractObject) -> int:
        """
        Метод підрахунку кількості включень заданого значення в структурі
        :param value: Значення, що шукається
        :return: Кількість включень заданого елемента
        """
        pass


class AbstractStructureBonus(AbstractStructureExtended):
    # Бонусний набір методів

    @abstractmethod
    def deepcopy(self) -> list[AbstractObject] | AbstractStructureBasic:
        """
        Метод, що повертає копію структури з однаковими значеннями в нових об'єктах елементів структури (не посиланнями на об'єкти поточної структури)
        :return: Копія структури
        """
        pass

    @abstractmethod
    def min(self) -> AbstractObject:
        """
        Повертає найменший елемент структури
        :return: Значення найменшого елемента структури
        """
        pass

    @abstractmethod
    def max(self) -> AbstractObject:
        """
        Повертає найбільший елемент структури
        :return: Значення найбільшого елемента структури
        """
        pass

    @abstractmethod
    def __add__(self, other) -> AbstractStructureBasic|list:
        """
        Поєднання елементів поточної і наступної структури у єдину
        :param other: Структура, що поєднується з поточною
        :return: Структура зі значеннями обох структур, що поєднуються
        """
        pass

    @abstractmethod
    def __mul__(self, other) -> AbstractStructureBasic|list:
        """
        Дублювання елементів структури вказану кількість разів (тільки при множенні на ціле число), якщо це передбачено логікою структури
        :param other: Структура або число повторень
        :return: Структура з повтореннями вказаної кількості разів
        """
        pass
