import time

from Practice2.generator import Generator
from Practice5.limitstructures import ArrayStack, LinkedPriorityQueue, DequeDeque

N = 10_000


def timeit(func) -> float:
    start = time.perf_counter()
    func()
    return (time.perf_counter() - start) * 1000


def bench_stack(data):
    s = ArrayStack()
    t_push = timeit(lambda: [s.push(x) for x in data])
    t_top = timeit(lambda: [s.top() for _ in range(N)])
    t_pop = timeit(lambda: [s.pop() for _ in range(N)])
    return t_push, t_top, t_pop


def bench_priority_queue(data):
    q = LinkedPriorityQueue()
    t_enq = timeit(lambda: [q.enqueue(x) for x in data])
    t_top = timeit(lambda: [q.top() for _ in range(N)])
    t_deq = timeit(lambda: [q.dequeue() for _ in range(N)])
    return t_enq, t_top, t_deq


def bench_deque(data):
    d = DequeDeque()
    t_push = timeit(lambda: [d.push_last(x) for x in data])
    t_top = timeit(lambda: [d.top_first() for _ in range(N)])
    t_pop = timeit(lambda: [d.pop_first() for _ in range(N)])
    return t_push, t_top, t_pop


def main():
    print(f"Генерація {N} об'єктів Notebook...")
    gen = Generator()
    data = [gen.generate_single() for _ in range(N)]

    s_push, s_top, s_pop = bench_stack(data)
    q_enq, q_top, q_deq = bench_priority_queue(data)
    d_push, d_top, d_pop = bench_deque(data)

    print(f"\n{'Структура':<32}{'Вставка':>12}{'top':>12}{'Видалення':>12}")
    print(f"{'(основа)':<32}{'(ms)':>12}{'(ms)':>12}{'(ms)':>12}")
    print("-" * 68)
    print(f"{'Стек (ArrayParts, масив)':<32}{s_push:>12.2f}{s_top:>12.2f}{s_pop:>12.2f}")
    print(f"{'Пріор. черга (LinkedList)':<32}{q_enq:>12.2f}{q_top:>12.2f}{q_deq:>12.2f}")
    print(f"{'Дек (collections.deque)':<32}{d_push:>12.2f}{d_top:>12.2f}{d_pop:>12.2f}")
    print("-" * 68)


if __name__ == "__main__":
    main()
