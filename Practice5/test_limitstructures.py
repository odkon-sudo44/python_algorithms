import datetime

import pytest

from Practice5.limitstructures import ArrayStack, LinkedPriorityQueue, DequeDeque
from Practice2.generator import Generator
from Practice1.notebook_dataclass import Notebook
from Practice1.abstract_object import AbstractObject


def nb(manufacturer="Dell", model="XPS 13", screen=14.0, memory=8,
       cpu="Intel i5", storage=256):
    return Notebook(manufacturer, model, screen, memory, cpu, storage,
                    datetime.date(2024, 1, 1))


def test_stack_empty():
    s = ArrayStack()
    assert len(s) == 0


def test_stack_init_from_list():
    s = ArrayStack([nb(memory=4), nb(memory=8), nb(memory=16)])
    assert len(s) == 3
    # останній переданий - на вершині
    assert s.top().memory == 16


def test_stack_init_separate():
    s = ArrayStack(nb(memory=4), nb(memory=8))
    assert len(s) == 2
    assert s.top().memory == 8


def test_stack_push_increases_len():
    s = ArrayStack()
    s.push(nb())
    s.push(nb())
    assert len(s) == 2


def test_stack_lifo_order():
    s = ArrayStack()
    s.push(nb(memory=4))
    s.push(nb(memory=8))
    s.push(nb(memory=16))
    assert s.pop().memory == 16
    assert s.pop().memory == 8
    assert s.pop().memory == 4


def test_stack_top_does_not_remove():
    s = ArrayStack()
    s.push(nb(memory=8))
    assert s.top().memory == 8
    assert len(s) == 1
    assert s.top().memory == 8


def test_stack_pop_empty():
    s = ArrayStack()
    with pytest.raises(IndexError):
        s.pop()


def test_stack_top_empty():
    s = ArrayStack()
    with pytest.raises(IndexError):
        s.top()


def test_stack_returns_notebook():
    s = ArrayStack([nb()])
    value = s.pop()
    assert isinstance(value, Notebook)
    assert isinstance(value, AbstractObject)


def test_stack_repr():
    s = ArrayStack([nb()])
    assert "Stack" in repr(s)


def test_stack_with_generator():
    g = Generator()
    data = [g.generate_single() for _ in range(5)]
    s = ArrayStack(data)
    assert len(s) == 5
    # знімаємо все - має вийти у зворотному порядку
    popped = [s.pop() for _ in range(5)]
    assert popped == list(reversed(data))


def test_pq_empty():
    q = LinkedPriorityQueue()
    assert len(q) == 0


def test_pq_init_from_list():
    q = LinkedPriorityQueue([nb(memory=8), nb(memory=32), nb(memory=4)])
    assert len(q) == 3
    assert q.top().memory == 32


def test_pq_init_separate():
    q = LinkedPriorityQueue(nb(memory=4), nb(memory=16))
    assert len(q) == 2
    assert q.top().memory == 16


def test_pq_orders_by_ram_desc():
    q = LinkedPriorityQueue([nb(memory=8), nb(memory=32),
                             nb(memory=4), nb(memory=16)])
    order = [q.dequeue().memory for _ in range(4)]
    assert order == [32, 16, 8, 4]


def test_pq_enqueue_highest_goes_first():
    q = LinkedPriorityQueue()
    q.enqueue(nb(memory=8))
    q.enqueue(nb(memory=4))
    q.enqueue(nb(memory=32))      # найбільший RAM стане головою
    assert q.top().memory == 32


def test_pq_enqueue_lowest_goes_last():
    q = LinkedPriorityQueue()
    q.enqueue(nb(memory=16))
    q.enqueue(nb(memory=8))
    q.enqueue(nb(memory=4))       # найменший RAM у кінець
    assert q.dequeue().memory == 16
    assert q.dequeue().memory == 8
    assert q.dequeue().memory == 4


def test_pq_equal_priority_keeps_order():
    first = nb(manufacturer="Dell", memory=8)
    second = nb(manufacturer="HP", memory=8)
    q = LinkedPriorityQueue()
    q.enqueue(first)
    q.enqueue(second)
    assert q.dequeue().manufacturer == "Dell"
    assert q.dequeue().manufacturer == "HP"


def test_pq_top_does_not_remove():
    q = LinkedPriorityQueue([nb(memory=16)])
    assert q.top().memory == 16
    assert len(q) == 1


def test_pq_dequeue_empty():
    q = LinkedPriorityQueue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_pq_top_empty():
    q = LinkedPriorityQueue()
    with pytest.raises(IndexError):
        q.top()


def test_pq_returns_notebook():
    q = LinkedPriorityQueue([nb()])
    value = q.dequeue()
    assert isinstance(value, Notebook)
    assert isinstance(value, AbstractObject)


def test_pq_repr():
    q = LinkedPriorityQueue([nb()])
    assert "PriorityQueue" in repr(q)


def test_pq_with_generator():
    g = Generator()
    data = [g.generate_single() for _ in range(10)]
    q = LinkedPriorityQueue(data)
    assert len(q) == 10
    rams = [q.dequeue().memory for _ in range(10)]
    assert rams == sorted(rams, reverse=True)


def test_pq_len_decreases_on_dequeue():
    q = LinkedPriorityQueue([nb(memory=4), nb(memory=8)])
    q.dequeue()
    assert len(q) == 1


def test_deque_empty():
    d = DequeDeque()
    assert len(d) == 0


def test_deque_init_from_list():
    d = DequeDeque([nb(memory=4), nb(memory=8)])
    assert len(d) == 2
    assert d.top_first().memory == 4
    assert d.top_last().memory == 8


def test_deque_init_separate():
    d = DequeDeque(nb(memory=4), nb(memory=8))
    assert len(d) == 2


def test_deque_push_first():
    d = DequeDeque()
    d.push_last(nb(memory=8))
    d.push_first(nb(memory=4))
    assert d.top_first().memory == 4
    assert d.top_last().memory == 8


def test_deque_push_last():
    d = DequeDeque()
    d.push_last(nb(memory=4))
    d.push_last(nb(memory=8))
    assert d.top_last().memory == 8


def test_deque_pop_first():
    d = DequeDeque([nb(memory=4), nb(memory=8)])
    assert d.pop_first().memory == 4
    assert len(d) == 1


def test_deque_pop_last():
    d = DequeDeque([nb(memory=4), nb(memory=8)])
    assert d.pop_last().memory == 8
    assert len(d) == 1


def test_deque_top_first_no_remove():
    d = DequeDeque([nb(memory=4)])
    assert d.top_first().memory == 4
    assert len(d) == 1


def test_deque_top_last_no_remove():
    d = DequeDeque([nb(memory=4)])
    assert d.top_last().memory == 4
    assert len(d) == 1


def test_deque_pop_first_empty():
    d = DequeDeque()
    with pytest.raises(IndexError):
        d.pop_first()


def test_deque_pop_last_empty():
    d = DequeDeque()
    with pytest.raises(IndexError):
        d.pop_last()


def test_deque_top_first_empty():
    d = DequeDeque()
    with pytest.raises(IndexError):
        d.top_first()


def test_deque_top_last_empty():
    d = DequeDeque()
    with pytest.raises(IndexError):
        d.top_last()


def test_deque_repr():
    d = DequeDeque([nb()])
    assert "Deque" in repr(d)


def test_deque_returns_notebook():
    d = DequeDeque([nb()])
    assert isinstance(d.pop_first(), Notebook)
