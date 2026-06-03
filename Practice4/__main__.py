from Practice2.generator import Generator
from Practice4.linkedlist import LinkedList
from Practice1.notebook_dataclass import Notebook
from Practice1.abstract_object import AbstractObject


if __name__ == "__main__":

    g = Generator()
    g5 = [g.generate_single() for _ in range(5)]
    lst = g5
    tpl = tuple(g5)

    print("=== Створення зв'язаного списку з tuple ===")
    ll1 = LinkedList(tpl)
    print(ll1)

    print("\n=== Створення зв'язаного списку з list ===")
    ll2 = LinkedList(lst)
    print(ll2)

    print("\n=== Перевірка типів даних ===")
    print(type(ll2[0]))
    print("isinstance Notebook:", isinstance(ll2[0], Notebook))
    print("isinstance AbstractObject:", isinstance(ll2[0], AbstractObject))

    print("\n=== __len__ ===")
    print("Кількість елементів:", len(ll1))

    print("\n=== __getitem__ (індекс і зріз) ===")
    print("ll1[0]:", ll1[0])
    print("ll1[-1]:", ll1[-1])
    print("ll1[1:3]:", ll1[1:3])

    print("\n=== __setitem__ ===")
    new_nb = g.generate_single()
    ll1[2] = new_nb
    print("ll1[2] після заміни:", ll1[2])

    print("\n=== append ===")
    ll1.append(g.generate_single())
    print("Довжина після append:", len(ll1))

    print("\n=== insert (в початок) ===")
    ll1.insert(0, g.generate_single())
    print("Новий перший елемент:", ll1[0])
    print("Довжина після insert:", len(ll1))

    print("\n=== index ===")
    target = ll1[3]
    print("index елемента ll1[3]:", ll1.index(target))

    print("\n=== count ===")
    print("Кількість входжень ll1[3]:", ll1.count(target))

    print("\n=== remove ===")
    before = len(ll1)
    ll1.remove(ll1[0])
    print(f"Довжина: {before} -> {len(ll1)}")

    print("\n=== pop ===")
    popped = ll1.pop()
    print("Вилучено з кінця:", popped)
    print("Довжина після pop:", len(ll1))

    print("\n=== del (за індексом) ===")
    del ll1[0]
    print("Довжина після del ll1[0]:", len(ll1))

    print("\n=== iter / for ===")
    for i, nb in enumerate(ll1):
        print(f"  [{i}] {nb}")

    print("\n=== reverse ===")
    ll1.reverse()
    print("Після reverse, перший:", ll1[0])

    print("\n=== copy ===")
    backup = ll1.copy()
    print("Копія (list), довжина:", len(backup))

    print("\n=== extend ===")
    ll1.extend(g5)
    print("Довжина після extend на 5 елементів:", len(ll1))

    print("\n=== clear ===")
    ll1.clear()
    print("Довжина після clear:", len(ll1))
    print("Вміст:", ll1)
