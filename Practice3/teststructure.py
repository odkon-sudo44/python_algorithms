import datetime

import pytest

from Practice3.structureexamples import ArrayParts
from Practice2.generator import Generator
from Practice1.notebook_dataclass import Notebook
from Practice1.abstract_object import AbstractObject


def make_notebook(manufacturer="Dell", model="XPS 13", screen=14.0,
                  memory=8, cpu="Intel i5", storage=256):
    return Notebook(manufacturer, model, screen, memory, cpu, storage,
                    datetime.date(2024, 1, 1))


@pytest.fixture
def five_notebooks():
    return [
        make_notebook("Dell", "XPS 13"),
        make_notebook("ASUS", "ROG Strix", 15.6, 16, "Intel i7", 512),
        make_notebook("Acer", "Aspire 5", 15.6, 4, "Intel i3", 128),
        make_notebook("Lenovo", "IdeaPad 3", 14.0, 8, "AMD Ryzen 5", 256),
        make_notebook("HP", "Pavilion", 17.3, 32, "AMD Ryzen 7", 1024),
    ]


# init / len

def test_init_empty():
    arr = ArrayParts()
    assert len(arr) == 0


def test_init_from_list(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert len(arr) == 5


def test_init_from_tuple(five_notebooks):
    arr = ArrayParts(tuple(five_notebooks))
    assert len(arr) == 5


def test_init_separate_objects(five_notebooks):
    arr = ArrayParts(five_notebooks[0], five_notebooks[1], five_notebooks[2])
    assert len(arr) == 3


def test_elements_are_abstract_objects(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert isinstance(arr[0], AbstractObject)
    assert isinstance(arr[0], Notebook)


#  repr

def test_repr_empty():
    assert repr(ArrayParts()) == "[]"


def test_repr_contains_elements(five_notebooks):
    arr = ArrayParts(five_notebooks)
    text = repr(arr)
    assert text.startswith("[") and text.endswith("]")
    assert "Dell" in text


#  getitem

def test_getitem_positive(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr[0] == five_notebooks[0]
    assert arr[4] == five_notebooks[4]


def test_getitem_negative(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr[-1] == five_notebooks[-1]
    assert arr[-5] == five_notebooks[0]


def test_getitem_out_of_range(five_notebooks):
    arr = ArrayParts(five_notebooks)
    with pytest.raises(IndexError):
        _ = arr[5]
    with pytest.raises(IndexError):
        _ = arr[-6]


def test_getitem_slice(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr[1:3] == five_notebooks[1:3]
    assert arr[:] == five_notebooks
    assert arr[::2] == five_notebooks[::2]


def test_getitem_wrong_type(five_notebooks):
    arr = ArrayParts(five_notebooks)
    with pytest.raises(TypeError):
        _ = arr["a"]


#  setitem

def test_setitem(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air", 13.3, 16, "Apple M2", 512)
    arr[2] = new
    assert arr[2] == new


def test_setitem_negative(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr[-1] = new
    assert arr[4] == new


def test_setitem_out_of_range(five_notebooks):
    arr = ArrayParts(five_notebooks)
    with pytest.raises(IndexError):
        arr[10] = make_notebook()


def test_setitem_wrong_type(five_notebooks):
    arr = ArrayParts(five_notebooks)
    with pytest.raises(TypeError):
        arr["x"] = make_notebook()


#  append / resize

def test_append_grows():
    arr = ArrayParts()
    items = [make_notebook(model=str(i)) for i in range(25)]
    for it in items:
        arr.append(it)
    assert len(arr) == 25
    assert arr[24] == items[24]
    assert arr[0] == items[0]


def test_resize_keeps_order():
    arr = ArrayParts()
    items = [make_notebook(model=str(i)) for i in range(100)]
    for it in items:
        arr.append(it)
    assert len(arr) == 100
    for i in range(100):
        assert arr[i] == items[i]


#  insert
def test_insert_middle(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(2, new)
    assert arr[2] == new
    assert arr[3] == five_notebooks[2]
    assert len(arr) == 6


def test_insert_at_end(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(len(arr), new)
    assert arr[-1] == new


def test_insert_negative(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(-1, new)
    assert arr[4] == new


def test_insert_clamps_overflow(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(999, new)
    assert arr[-1] == new


def test_insert_clamps_underflow(five_notebooks):
    arr = ArrayParts(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(-999, new)
    assert arr[0] == new


def test_insert_triggers_resize():
    arr = ArrayParts([make_notebook(model=str(i)) for i in range(10)])
    new = make_notebook("Apple", "MacBook Air")
    arr.insert(0, new)
    assert arr[0] == new
    assert len(arr) == 11


#  index
def test_index_found(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr.index(five_notebooks[3]) == 3


def test_index_with_range(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr.index(five_notebooks[4], 2, 5) == 4


def test_index_negative_start(five_notebooks):
    arr = ArrayParts(five_notebooks)
    assert arr.index(five_notebooks[4], -2) == 4


def test_index_not_found(five_notebooks):
    arr = ArrayParts(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    with pytest.raises(ValueError):
        arr.index(other)


#  remove
def test_remove(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.remove(five_notebooks[1])
    assert len(arr) == 4
    assert arr[1] == five_notebooks[2]


def test_remove_last(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.remove(five_notebooks[4])
    assert len(arr) == 4
    with pytest.raises(IndexError):
        _ = arr[4]


def test_remove_not_found(five_notebooks):
    arr = ArrayParts(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    with pytest.raises(ValueError):
        arr.remove(other)


#  iter / next

def test_iteration(five_notebooks):
    arr = ArrayParts(five_notebooks)
    collected = [item for item in arr]
    assert collected == five_notebooks


def test_iteration_restarts(five_notebooks):
    arr = ArrayParts(five_notebooks)
    first = list(arr)
    second = list(arr)
    assert first == second


def test_next_stops():
    arr = ArrayParts([make_notebook()])
    it = iter(arr)
    next(it)
    with pytest.raises(StopIteration):
        next(it)


#  delitem

def test_delitem(five_notebooks):
    arr = ArrayParts(five_notebooks)
    del arr[0]
    assert len(arr) == 4
    assert arr[0] == five_notebooks[1]


def test_delitem_negative(five_notebooks):
    arr = ArrayParts(five_notebooks)
    del arr[-1]
    assert len(arr) == 4
    assert arr[-1] == five_notebooks[3]


def test_delitem_out_of_range(five_notebooks):
    arr = ArrayParts(five_notebooks)
    with pytest.raises(IndexError):
        del arr[10]


#  clear

def test_clear(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.clear()
    assert len(arr) == 0
    assert repr(arr) == "[]"


def test_clear_then_append(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.clear()
    nb = make_notebook()
    arr.append(nb)
    assert len(arr) == 1
    assert arr[0] == nb


#  copy

def test_copy(five_notebooks):
    arr = ArrayParts(five_notebooks)
    snapshot = arr.copy()
    assert snapshot == five_notebooks
    arr.remove(five_notebooks[0])
    assert len(snapshot) == 5


#  extend

def test_extend(five_notebooks):
    arr = ArrayParts(five_notebooks[:2])
    arr.extend(five_notebooks[2:])
    assert len(arr) == 5
    assert arr.copy() == five_notebooks


def test_extend_empty(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.extend([])
    assert len(arr) == 5


#  pop
def test_pop_default(five_notebooks):
    arr = ArrayParts(five_notebooks)
    value = arr.pop()
    assert value == five_notebooks[4]
    assert len(arr) == 4


def test_pop_index(five_notebooks):
    arr = ArrayParts(five_notebooks)
    value = arr.pop(0)
    assert value == five_notebooks[0]
    assert arr[0] == five_notebooks[1]


def test_pop_empty():
    arr = ArrayParts()
    with pytest.raises(IndexError):
        arr.pop()


#  reverse

def test_reverse(five_notebooks):
    arr = ArrayParts(five_notebooks)
    arr.reverse()
    assert arr.copy() == list(reversed(five_notebooks))


def test_reverse_empty():
    arr = ArrayParts()
    arr.reverse()
    assert len(arr) == 0


#  count

def test_count():
    nb = make_notebook("Dell", "XPS 13")
    dup = make_notebook("Dell", "XPS 13")     # рівний за полями
    other = make_notebook("HP", "Pavilion")
    arr = ArrayParts([nb, dup, other])
    assert arr.count(nb) == 2
    assert arr.count(other) == 1


def test_count_absent(five_notebooks):
    arr = ArrayParts(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    assert arr.count(other) == 0


#  integration with generator

def test_with_generator():
    g = Generator()
    data = [g.generate_single() for _ in range(5)]
    arr = ArrayParts(data)
    assert len(arr) == 5
    assert all(isinstance(arr[i], Notebook) for i in range(5))