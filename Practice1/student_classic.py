from Practice1.abstract_object import AbstractObject


class StudentBasic(AbstractObject):
    name: str           # ім’я студента
    surname: str        # прізвище студента
    discipline: str     # назва дисципліни
    mark: int           # оцінка з дисципліни
    exam: str = "іспит"  # передвстановлене значення

    def __init__(self, name: str, surname: str, discipline: str, mark: int, exam: str = "іспит") -> None:
        """Конструктор класу - метод, що запускається при створенні об'єкта і використовується для початкового внесення
        необхідних даних
        """
        self.name = name
        self.surname = surname
        self.discipline = discipline
        self.mark = mark
        self.exam = exam

    def get_info(self) -> str:
        """Метод для виведення стислої інформації
        """
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"

    def get_message(self) -> str:
        """Метод для виведення інформації по алгоритму
        """
        if self.mark < 60:
            letter, markname = "FX", "незадовільно"
        elif self.mark < 68:
            letter, markname = "E", "задовільно"
        elif self.mark < 75:
            letter, markname = "D", "задовільно"
        elif self.mark < 83:
            letter, markname = "C", "добре"
        elif self.mark < 90:
            letter, markname = "B", "добре"
        else:
            letter, markname = "A", "відмінно"

        if self.exam == "залік" and self.mark < 60:
            markname = "незараховано"
        elif self.exam == "залік":
            markname = "зараховано"

        return f'"Студент {self.name} {self.surname} ' \
               f'по предмету {self.discipline} отримав ' \
               f'оцінку "{markname}" ({letter}, {self.mark})"'


class Student(StudentBasic):
    """Розширений клас через наслідування StudentBasic
    """
    __mark: int

    @property
    def mark(self):
        """Getter для атрибуту mark
        """
        return self.__mark

    @mark.setter
    def mark(self, value):
        """Setter для атрибуту mark з забороною помилкових значень
        """
        if type(value) != int:
            raise TypeError
        elif value < 0 or value > 100:
            raise ValueError
        else:
            self.__mark = value

    def __repr__(self):
        """Метод представлення в ПР2 об'єкта при виведенні у вигляді рядка зі значеннями атрибутів
        """
        return self.get_info()

    def __eq__(self, other):
        """Метод порівняння в ПР3-6 двох об'єктів для пошуку співпадіння
        """
        # if other.__class__ is not self.__class__:
        #     return NotImplemented
        return self.surname == other.surname and \
            self.name == other.name and \
            self.discipline == other.discipline and \
            self.mark == other.mark

    def __le__(self, other):
        """Метод визначення меншого в ПР3-6 з двох об'єктів для впорядкування
        """
        return (self.surname, self.name, self.discipline, self.mark) \
            <= (other.surname, other.name, other.discipline, other.mark)

    def __ge__(self, other):
        """Метод визначення більшого в ПР3-6 з двох об'єктів для впорядкування
        """
        return (self.surname, self.name, self.discipline, self.mark) \
            >= (other.surname, other.name, other.discipline, other.mark)
