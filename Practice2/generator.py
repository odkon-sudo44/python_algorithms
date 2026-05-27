import names
import random
from datetime import date
from AlgorithmsCourse.Practice1.student_dataclass import Student


class Generator:
    disciplines = ("Алгоритми і структури даних",
                   "Основи програмування",
                   "Бази даних",
                   "Захист інформації",
                   "Основи машинного навчання",
                   "Адміністрування Linux")
    exam = ["іспит", "залік", "діф. залік"]

    def __create_date(self) -> str:
        cur_year = date.today().year
        year = random.randint(1930, cur_year)
        month = random.randint(1, 12)

        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)

    def generate_single(self) -> Student:
        """Метод автоматичного створення екземпляру класу Student з випадковими чи обраними з певного переліку значеннями кожної властивості класу
        """
        name = names.get_first_name()
        surname = names.get_last_name()

        exam = self.exam[
            random.randint(0, 2)]
        disc = random.choice(self.disciplines)
        mark = random.randint(0,100)
        return Student(surname, name, disc, mark, exam)

    def generate_1000(self) -> list:
        """Метод генерування 1000 об'єктів класу Student"""
        plist = list()
        for i in range(1000):
            plist.append(self.generate_single())
        return plist

    def generate_10_000(self) -> list:
        """Метод генерування 10 000 об'єктів класу Student"""
        plist = [self.generate_single() for i in range(10000)]
        return plist

