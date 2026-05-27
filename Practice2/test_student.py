import pytest
from AlgorithmsCourse.Practice1.student_dataclass import Student


class TestStudentClass:
    """Перевірка базових дій класу Student
    """

    @pytest.fixture
    def init_student(self):
        """Підготовка до тестів
        """
        return Student("Name", "Surname", "Discipline", 87)

    def test_data_type(self, init_student):
        """Перевірка відповідності класу"""
        assert isinstance(init_student, Student)

    def test_check_init(self, init_student):
        """Перевірка ініціації і внесення даних
        """
        # s = Student("Name", "Surname", "Discipline", 87)
        s = init_student
        assert s.name == "Name"
        assert s.surname == "Surname"
        assert s.discipline == "Discipline"
        assert s.mark == 87

    def test_check_default(self, init_student):
        """Перевірка значень за замовчуванням
        """
        assert init_student.exam == "іспит"

    @pytest.mark.skip("Для демонстративних цілей")
    def test_get_info(self, init_student):
        """Перевірка методу get_info()
        """
        assert init_student.get_info() == "Student(Name, Surname, Discipline, іспит, 87)"

    values_to_try = [(Student("Stu", "dent1", "Algo", 0, "залік"), "FX", "незараховано"),
                     (Student("Stu", "dent2", "Algo", 80, "залік"), "C", "зараховано"),
                     (Student("Stu", "dent3", "Algo", 67, "іспит"), "E", "задовільно"),
                     (Student("Stu", "dent4", "Algo", 74, "іспит"), "D", "задовільно"),
                     (Student("Stu", "dent5", "Algo", 75, "іспит"), "C", "добре"),
                     (Student("Stu", "dent6", "Algo", 83, "іспит"), "B", "добре"),
                     (Student("Stu", "dent7", "Algo", 90, "іспит"), "A", "відмінно"),
                     (Student("Stu", "dent8", "Algo", 100, "іспит"), "A", "відмінно")]

    @pytest.mark.parametrize('student, letter, mname', values_to_try)
    def test_get_message(self, student, letter, mname):
        """Перевірка get_message() на коректних значеннях
        """
        assert student.get_message() == f'"Студент {student.name} {student.surname} ' \
                                        f'по предмету {student.discipline} отримав ' \
                                        f'оцінку "{mname}" ({letter}, {student.mark})"'


class TestStudentErrors:
    """Перевірка основних помилок класу Student
    """

    @pytest.fixture
    def student(self):
        return Student("Name", "Surname", "Discipline", 87)

    @pytest.mark.xfail
    def test_wrong_name_type(self, student):
        student.name = 5645
        assert type(student.name) == str

    @pytest.mark.xfail
    def test_wrong_disc_type(self, student):
        student.discipline = True
        assert isinstance(student.discipline, str)

    def test_mark_type_error(self):
        """Очікуємо помилку TypeError при виконанні тесту
        """
        with pytest.raises(TypeError):
            Student("Name", "Surname", "Discipline", "87")

    values_to_try = [("Stu", "dent1", "Algo", -10),
                     ("Stu", "dent2", "Algo", 160),
                     ("Stu", "dent3", "Algo", 0),
                     ("Stu", "dent4", "Algo", 101)]

    @pytest.mark.xfail
    @pytest.mark.parametrize('name, surname, disc, mark', values_to_try)
    def test_mark_value_error(self, name, surname, disc, mark):
        with pytest.raises(ValueError):
            Student(name, surname, disc, mark)


class TestStudentComparison:

    @pytest.fixture
    def student(self):
        """Підготовка до тестів
        """
        return [Student("Name", "Surname", "Discipline", 87),
                Student("Name", "Surname2", "Discipline", 87),
                Student("Name", "Surname", "Discipline", 46)]

    def test_repr(self, student):
        """Перевірка __repr__
        """
        assert str(student[0]) == "Student(Name, Surname, Discipline, іспит, 87)"

    def test_equals(self, student):
        """Перевірка рівності об'єктів
        """
        assert student[0] == Student("Name", "Surname", "Discipline", 87)

    def test_less(self, student):
        """Перевірка чи перший об'єкт менше
        """
        assert student[0] <= student[1]

    def test_greater(self, student):
        """Перевірка чи перший об'єкт більше
        """
        assert student[0] >= student[2]

    # @pytest.mark.xfail()
    # def test_compare_diff_classes(self, student):
    #     """Порівняння різних типів даних
    #     """
    #     assert student[0] <= ("Name", "Surname", "Discipline", 87)
