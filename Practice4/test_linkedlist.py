import datetime

import pytest

from Practice4.linkedlist import LinkedList
from Practice4.node import Node
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


#   node
def test_node_repr():
    nb = make_notebook()
    node = Node(nb)
    assert node.next is None
    assert repr(node) == repr(nb)


#   init / len
def test_init_empty():
    assert len(LinkedList()) == 0


def test_init_from_list(five_notebooks):
    assert len(LinkedList(five_notebooks)) == 5


def test_init_from_tuple(five_notebooks):
    assert len(LinkedList(tuple(five_notebooks))) == 5


def test_init_separate_objects(five_notebooks):
    ll = LinkedList(five_notebooks[0], five_notebooks[1], five_notebooks[2])
    assert len(ll) == 3


def test_elements_are_abstract_objects(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert isinstance(ll[0], AbstractObject)
    assert isinstance(ll[0], Notebook)


#   repr
def test_repr_empty():
    assert repr(LinkedList()) == "[]"


def test_repr_contains_elements(five_notebooks):
    text = repr(LinkedList(five_notebooks))
    assert text.startswith("[") and text.endswith("]")
    assert "Dell" in text


#   getitem
def test_getitem_positive(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll[0] == five_notebooks[0]
    assert ll[4] == five_notebooks[4]


def test_getitem_negative(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll[-1] == five_notebooks[-1]
    assert ll[-5] == five_notebooks[0]


def test_getitem_out_of_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(IndexError):
        _ = ll[5]
    with pytest.raises(IndexError):
        _ = ll[-6]


def test_getitem_slice(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll[1:3] == five_notebooks[1:3]
    assert ll[:] == five_notebooks
    assert ll[::2] == five_notebooks[::2]


def test_getitem_wrong_type(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(TypeError):
        _ = ll["a"]


#   setitem
def test_setitem(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air", 13.3, 16, "Apple M2", 512)
    ll[2] = new
    assert ll[2] == new


def test_setitem_negative(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll[-1] = new
    assert ll[4] == new


def test_setitem_out_of_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(IndexError):
        ll[10] = make_notebook()


def test_setitem_wrong_type(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(TypeError):
        ll["x"] = make_notebook()


#   append
def test_append_to_empty():
    ll = LinkedList()
    nb = make_notebook()
    ll.append(nb)
    assert len(ll) == 1
    assert ll[0] == nb


def test_append_many():
    ll = LinkedList()
    items = [make_notebook(model=str(i)) for i in range(50)]
    for it in items:
        ll.append(it)
    assert len(ll) == 50
    assert ll[0] == items[0]
    assert ll[49] == items[49]


#   insert
def test_insert_head(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll.insert(0, new)
    assert ll[0] == new
    assert ll[1] == five_notebooks[0]
    assert len(ll) == 6


def test_insert_middle(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll.insert(2, new)
    assert ll[2] == new
    assert ll[3] == five_notebooks[2]


def test_insert_at_end(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll.insert(len(ll), new)
    assert ll[-1] == new


def test_insert_negative(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll.insert(-1, new)
    assert ll[4] == new


def test_insert_clamps_underflow(five_notebooks):
    ll = LinkedList(five_notebooks)
    new = make_notebook("Apple", "MacBook Air")
    ll.insert(-999, new)
    assert ll[0] == new


def test_insert_into_empty():
    ll = LinkedList()
    nb = make_notebook()
    ll.insert(0, nb)
    assert ll[0] == nb
    assert len(ll) == 1


#   index
def test_index_found(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll.index(five_notebooks[3]) == 3


def test_index_with_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll.index(five_notebooks[4], 2, 5) == 4


def test_index_negative_start(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll.index(five_notebooks[4], -2) == 4


def test_index_not_found(five_notebooks):
    ll = LinkedList(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    with pytest.raises(ValueError):
        ll.index(other)


def test_index_outside_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(ValueError):
        ll.index(five_notebooks[4], 0, 2)


def test_index_large_negative_start(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert ll.index(five_notebooks[0], -999) == 0


#   remove
def test_remove_head(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.remove(five_notebooks[0])
    assert len(ll) == 4
    assert ll[0] == five_notebooks[1]


def test_remove_middle(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.remove(five_notebooks[2])
    assert len(ll) == 4
    assert ll[2] == five_notebooks[3]


def test_remove_tail(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.remove(five_notebooks[4])
    assert len(ll) == 4
    nb = make_notebook("Apple", "MacBook Air")
    ll.append(nb)
    assert ll[-1] == nb


def test_remove_only_element():
    nb = make_notebook()
    ll = LinkedList([nb])
    ll.remove(nb)
    assert len(ll) == 0
    assert repr(ll) == "[]"


def test_remove_not_found(five_notebooks):
    ll = LinkedList(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    with pytest.raises(ValueError):
        ll.remove(other)


#   iter / next
def test_iteration(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert [item for item in ll] == five_notebooks


def test_iteration_restarts(five_notebooks):
    ll = LinkedList(five_notebooks)
    assert list(ll) == list(ll)


def test_next_stops_empty():
    ll = LinkedList()
    it = iter(ll)
    with pytest.raises(StopIteration):
        next(it)


#   delitem
def test_delitem_head(five_notebooks):
    ll = LinkedList(five_notebooks)
    del ll[0]
    assert len(ll) == 4
    assert ll[0] == five_notebooks[1]


def test_delitem_middle(five_notebooks):
    ll = LinkedList(five_notebooks)
    del ll[2]
    assert ll[2] == five_notebooks[3]


def test_delitem_tail(five_notebooks):
    ll = LinkedList(five_notebooks)
    del ll[-1]
    assert len(ll) == 4
    assert ll[-1] == five_notebooks[3]


def test_delitem_only_element():
    ll = LinkedList([make_notebook()])
    del ll[0]
    assert len(ll) == 0
    nb = make_notebook("Apple", "MacBook Air")
    ll.append(nb)
    assert ll[0] == nb


def test_delitem_out_of_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(IndexError):
        del ll[10]


def test_delitem_wrong_type(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(TypeError):
        del ll["x"]


#   clear
def test_clear(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.clear()
    assert len(ll) == 0
    assert repr(ll) == "[]"


def test_clear_then_append(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.clear()
    nb = make_notebook()
    ll.append(nb)
    assert len(ll) == 1
    assert ll[0] == nb


#   copy
def test_copy(five_notebooks):
    ll = LinkedList(five_notebooks)
    snapshot = ll.copy()
    assert snapshot == five_notebooks
    ll.remove(five_notebooks[0])
    assert len(snapshot) == 5


#   extend
def test_extend(five_notebooks):
    ll = LinkedList(five_notebooks[:2])
    ll.extend(five_notebooks[2:])
    assert len(ll) == 5
    assert ll.copy() == five_notebooks


def test_extend_empty(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.extend([])
    assert len(ll) == 5


#   pop
def test_pop_default(five_notebooks):
    ll = LinkedList(five_notebooks)
    value = ll.pop()
    assert value == five_notebooks[4]
    assert len(ll) == 4


def test_pop_head(five_notebooks):
    ll = LinkedList(five_notebooks)
    value = ll.pop(0)
    assert value == five_notebooks[0]
    assert ll[0] == five_notebooks[1]


def test_pop_middle(five_notebooks):
    ll = LinkedList(five_notebooks)
    value = ll.pop(2)
    assert value == five_notebooks[2]
    assert ll[2] == five_notebooks[3]


def test_pop_only_element():
    ll = LinkedList([make_notebook()])
    ll.pop(0)
    assert len(ll) == 0
    nb = make_notebook("Apple", "MacBook Air")
    ll.append(nb)
    assert ll[0] == nb


def test_pop_empty():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop()


def test_pop_out_of_range(five_notebooks):
    ll = LinkedList(five_notebooks)
    with pytest.raises(IndexError):
        ll.pop(10)


#   reverse
def test_reverse(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.reverse()
    assert ll.copy() == list(reversed(five_notebooks))


def test_reverse_then_append(five_notebooks):
    ll = LinkedList(five_notebooks)
    ll.reverse()
    nb = make_notebook("Apple", "MacBook Air")
    ll.append(nb)              # перевірка, що хвіст коректний після reverse
    assert ll[-1] == nb


def test_reverse_empty():
    ll = LinkedList()
    ll.reverse()
    assert len(ll) == 0


#   count
def test_count():
    nb = make_notebook("Dell", "XPS 13")
    dup = make_notebook("Dell", "XPS 13")
    other = make_notebook("HP", "Pavilion")
    ll = LinkedList([nb, dup, other])
    assert ll.count(nb) == 2
    assert ll.count(other) == 1


def test_count_absent(five_notebooks):
    ll = LinkedList(five_notebooks)
    other = make_notebook("Samsung", "Galaxy Book")
    assert ll.count(other) == 0


#   integration
def test_with_generator():
    g = Generator()
    data = [g.generate_single() for _ in range(5)]
    ll = LinkedList(data)
    assert len(ll) == 5
    assert all(isinstance(ll[i], Notebook) for i in range(5))
