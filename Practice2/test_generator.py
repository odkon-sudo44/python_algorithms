import pytest
from AlgorithmsCourse.Practice2.generator import Generator
from AlgorithmsCourse.Practice1.student_dataclass import Student

class TestGenerator:

    @pytest.fixture
    def init_student(self):
        """Підготовка до тестів
        """
        return Student("Name", "Surname", "Discipline", 87)

    def test_gen_single_types(self):
        g = Generator()
        st = g.generate_single()
        assert isinstance(st, Student)
        assert isinstance(st.name, str)
        assert isinstance(st.surname, str)
        assert isinstance(st.discipline, str)
        assert isinstance(st.mark, int)

    def test_gen_1000_type(self):
        g = Generator()
        slist = g.generate_1000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], Student)
        assert len(slist) == 1000

    def test_gen_10_000_type(self):
        g = Generator()
        slist = g.generate_10_000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], Student)
        assert len(slist) == 10000
