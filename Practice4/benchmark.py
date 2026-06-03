import time

from Practice2.generator import Generator
from Practice4.linkedlist import LinkedList
from Practice3.structureexamples import ArrayParts

N = 10_000
MID = N // 2


def timeit(func) -> float:
    start = time.perf_counter()
    func()
    return (time.perf_counter() - start) * 1000


def bench_prepend(cls, data) -> float:
    struct = cls()
    def run():
        for item in data:
            struct.insert(0, item)
    return timeit(run)


def bench_append(cls, data) -> float:
    struct = cls()
    def run():
        for item in data:
            struct.append(item)
    return timeit(run)


def bench_setitem_middle(struct, data) -> float:
    def run():
        for item in data:
            struct[MID] = item
    return timeit(run)


def bench_search(struct, first, last, middle) -> float:
    def run():
        struct.index(first)
        struct.index(last)
        struct.index(middle)
    return timeit(run)


def bench_access(struct) -> float:
    def run():
        _ = struct[0]
        _ = struct[MID]
        _ = struct[N - 1]
    return timeit(run)


def bench_pop_ends(cls, data) -> float:
    struct = cls(data)
    def run():
        for _ in range(1000):
            struct.pop(0)
        for _ in range(1000):
            struct.pop()
    return timeit(run)


def row(label, t_ll, t_arr):
    ratio = f"{t_ll / t_arr:6.1f}x" if t_arr > 0 else "   n/a"
    print(f"{label:<42} {t_ll:10.2f} {t_arr:10.2f}   {ratio}")


def main():
    print(f"Генерація {N} об'єктів Notebook...")
    gen = Generator()
    data = [gen.generate_single() for _ in range(N)]
    first, last, middle = data[0], data[-1], data[MID]

    print(f"\n{'Операція':<42} {'LinkedList':>10} {'ArrayParts':>10}   {'LL/Arr':>7}")
    print(f"{'':<42} {'(ms)':>10} {'(ms)':>10}")
    print("-" * 74)

    row("1. Вставка на початок (10000x insert(0))",
        bench_prepend(LinkedList, data), bench_prepend(ArrayParts, data))

    row("2. Додавання в кінець (10000x append)",
        bench_append(LinkedList, data), bench_append(ArrayParts, data))

    ll = LinkedList(data)
    arr = ArrayParts(data)
    row("3. Зміна центрального [5000] (10000x)",
        bench_setitem_middle(ll, data), bench_setitem_middle(arr, data))

    ll = LinkedList(data)
    arr = ArrayParts(data)
    row("4. Пошук першого/останнього/центру",
        bench_search(ll, first, last, middle),
        bench_search(arr, first, last, middle))

    row("5. Доступ за індексом [0]/[5000]/[9999]",
        bench_access(ll), bench_access(arr))

    row("6. Видалення з початку та кінця (2000x)",
        bench_pop_ends(LinkedList, data), bench_pop_ends(ArrayParts, data))


if __name__ == "__main__":
    main()
