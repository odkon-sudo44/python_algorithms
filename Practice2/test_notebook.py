import pytest
import datetime
from Practice1.notebook_dataclass import Notebook


class TestNotebookClass:
    @pytest.fixture
    def init_notebook(self):
        return Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)

    def test_data_type(self, init_notebook):
        assert isinstance(init_notebook, Notebook)

    def test_check_init(self, init_notebook):
        nb = init_notebook
        assert nb.manufacturer == "Dell"
        assert nb.model == "XPS 13"
        assert nb.screen_size == 13.3
        assert nb.memory == 16
        assert nb.cpu == "Intel i7"
        assert nb.storage == 512

    def test_check_default(self, init_notebook):
        assert init_notebook.birthday == datetime.date(2024, 1, 1)

    def test_get_info(self, init_notebook):
        assert init_notebook.get_info() == 'Dell XPS 13 (13.3", Intel i7, 16GB RAM, 512GB SSD)'

    values_to_try = [
        (Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512), "бізнес-модель"),
        (Notebook("ASUS", "ROG Strix", 15.6, 16, "AMD Ryzen 7", 1024), "ігрова модель"),
        (Notebook("Acer", "Aspire 5", 15.6, 4, "Intel Celeron", 256), "мультимедійна модель"),
        (Notebook("Lenovo", "IdeaPad 3", 14.0, 8, "Intel Celeron", 256), "ноутбук"),
    ]

    @pytest.mark.parametrize('notebook, model_type', values_to_try)
    def test_get_message(self, notebook, model_type):
        msg = notebook.get_message()
        assert model_type in msg
        assert notebook.manufacturer in msg
        assert notebook.model in msg
        assert str(notebook.screen_size) in msg
        assert str(notebook.memory) in msg
        assert notebook.cpu in msg
        assert str(notebook.storage) in msg


class TestNotebookErrors:
    @pytest.fixture
    def notebook(self):
        return Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)

    def test_screen_size_type_error(self):
        with pytest.raises(TypeError):
            Notebook("Dell", "XPS 13", "13.3", 16, "Intel i7", 512)

    def test_screen_size_value_error_negative(self):
        with pytest.raises(ValueError):
            Notebook("Dell", "XPS 13", -13.3, 16, "Intel i7", 512)

    def test_screen_size_value_error_zero(self):
        with pytest.raises(ValueError):
            Notebook("Dell", "XPS 13", 0, 16, "Intel i7", 512)

    def test_memory_type_error(self):
        with pytest.raises(TypeError):
            Notebook("Dell", "XPS 13", 13.3, "16", "Intel i7", 512)

    def test_memory_value_error_negative(self):
        with pytest.raises(ValueError):
            Notebook("Dell", "XPS 13", 13.3, -16, "Intel i7", 512)

    def test_memory_value_error_zero(self):
        with pytest.raises(ValueError):
            Notebook("Dell", "XPS 13", 13.3, 0, "Intel i7", 512)


class TestNotebookComparison:

    @pytest.fixture
    def notebooks(self):
        return [
            Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512),
            Notebook("ASUS", "ROG Strix", 15.6, 16, "AMD Ryzen 7", 1024),
            Notebook("Acer", "Aspire 5", 15.6, 4, "Intel i3", 256),
        ]

    def test_repr(self, notebooks):
        assert str(notebooks[0]) == 'Dell XPS 13 (13.3", Intel i7, 16GB RAM, 512GB SSD)'

    def test_equals(self, notebooks):
        nb_copy = Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)
        assert notebooks[0] == nb_copy

    def test_less(self, notebooks):
        assert notebooks[1] < notebooks[0]  # ASUS < Dell

    def test_greater(self, notebooks):

        assert notebooks[0] > notebooks[1]  # Dell > ASUS

