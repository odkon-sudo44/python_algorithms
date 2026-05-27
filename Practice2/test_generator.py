import pytest
from datetime import date
from Practice2.generator import Generator
from Practice1.notebook_dataclass import Notebook

class TestGenerator:

    @pytest.fixture
    def init_notebook(self):
        """Підготовка до тестів
        """
        return Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)

    def test_gen_single_types(self):
        """Перевірка типів атрибутів згенерованого Notebook
        """
        g = Generator()
        nb = g.generate_single()
        assert isinstance(nb, Notebook)
        assert isinstance(nb.manufacturer, str)
        assert isinstance(nb.model, str)
        assert isinstance(nb.screen_size, float)
        assert isinstance(nb.memory, int)
        assert isinstance(nb.cpu, str)
        assert isinstance(nb.storage, int)
        assert isinstance(nb.birthday, date)

    def test_gen_1000_type(self):
        """Перевірка генерування 1000 ноутбуків
        """
        g = Generator()
        nlist = g.generate_1000()
        assert isinstance(nlist, list)
        assert isinstance(nlist[0], Notebook)
        assert len(nlist) == 1000

    def test_gen_10_000_type(self):
        """Перевірка генерування 10 000 ноутбуків
        """
        g = Generator()
        nlist = g.generate_10_000()
        assert isinstance(nlist, list)
        assert isinstance(nlist[0], Notebook)
        assert len(nlist) == 10000
