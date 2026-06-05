from Practice2.generator import Generator
from Practice5.limitstructures import ArrayStack, LinkedPriorityQueue
from Practice1.notebook_dataclass import Notebook
from Practice1.abstract_object import AbstractObject


if __name__ == "__main__":

    g = Generator()
    data = [g.generate_single() for _ in range(5)]

    print("=" * 70)
    print("СТЕК (LIFO) на основі масиву ArrayParts (Практична робота №3)")
    print("=" * 70)

    stack = ArrayStack()
    print("\n--- push 5 об'єктів ---")
    for nb in data:
        stack.push(nb)
        print(f"  push: {nb}")
    print(f"\nДовжина стека: {len(stack)}")
    print(f"repr: {stack}")

    print(f"\n--- top (без видалення) ---")
    print(f"  Вершина: {stack.top()}")
    print(f"  Довжина не змінилась: {len(stack)}")

    print(f"\n--- pop усіх елементів (порядок LIFO) ---")
    while len(stack) > 0:
        print(f"  pop: {stack.pop()}")
    print(f"Довжина після спорожнення: {len(stack)}")

    print("\n--- pop з порожнього стека ---")
    try:
        stack.pop()
    except IndexError as e:
        print(f"  IndexError: {e}")

    print("\n")
    print("=" * 70)
    print("ПРІОРИТЕТНА ЧЕРГА на основі зв'язаного списку LinkedList (ПР №4)")
    print("Пріоритет = обсяг RAM (більше RAM -> вищий пріоритет)")
    print("=" * 70)

    pq = LinkedPriorityQueue()
    print("\n--- enqueue 5 об'єктів (у довільному порядку RAM) ---")
    for nb in data:
        pq.enqueue(nb)
        print(f"  enqueue (RAM={nb.memory}GB): {nb}")
    print(f"\nДовжина черги: {len(pq)}")
    print(f"repr: {pq}")

    print(f"\n--- top (найвищий пріоритет без видалення) ---")
    print(f"  RAM={pq.top().memory}GB: {pq.top()}")

    print(f"\n--- dequeue усіх (порядок за спаданням RAM) ---")
    while len(pq) > 0:
        nb = pq.dequeue()
        print(f"  dequeue (RAM={nb.memory}GB): {nb}")
    print(f"Довжина після спорожнення: {len(pq)}")

    print("\n--- dequeue з порожньої черги ---")
    try:
        pq.dequeue()
    except IndexError as e:
        print(f"  IndexError: {e}")

    print("\n--- перевірка типів ---")
    pq2 = LinkedPriorityQueue(data)
    value = pq2.dequeue()
    print(f"  type: {type(value).__name__}")
    print(f"  isinstance Notebook: {isinstance(value, Notebook)}")
    print(f"  isinstance AbstractObject: {isinstance(value, AbstractObject)}")
