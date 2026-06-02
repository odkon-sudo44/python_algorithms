from Practice2.generator import Generator
from Practice3.structureexamples import ArrayParts
from Practice1.notebook_dataclass import Notebook
from Practice1.abstract_object import AbstractObject


if __name__ == "__main__":

    # Створення 5 об'єктів Notebook
    g = Generator()
    g5 = [g.generate_single() for _ in range(5)]
    lst = g5
    tpl = tuple(g5)

    print("=== Створення структури з tuple ===")
    arr1 = ArrayParts(tpl)
    print(arr1)

    print("\n=== Створення структури з list ===")
    arr2 = ArrayParts(lst)
    print(arr2)

    print("\n=== Перевірка типів даних ===")
    print(type(arr2[0]))
    print("isinstance Notebook:", isinstance(arr2[0], Notebook))
    print("isinstance AbstractObject:", isinstance(arr2[0], AbstractObject))

    print("\n=== __len__ ===")
    print("Кількість елементів:", len(arr1))

    print("\n=== __getitem__ (індекс і зріз) ===")
    print("arr1[0]:", arr1[0])
    print("arr1[-1]:", arr1[-1])
    print("arr1[1:3]:", arr1[1:3])

    print("\n=== __setitem__ ===")
    new_nb = g.generate_single()
    arr1[2] = new_nb
    print("arr1[2] після заміни:", arr1[2])

    print("\n=== append ===")
    arr1.append(g.generate_single())
    print("Довжина після append:", len(arr1))

    print("\n=== insert ===")
    arr1.insert(0, g.generate_single())
    print("Новий перший елемент:", arr1[0])
    print("Довжина після insert:", len(arr1))

    print("\n=== index ===")
    target = arr1[3]
    print("index елемента arr1[3]:", arr1.index(target))

    print("\n=== count ===")
    print("Кількість входжень arr1[3]:", arr1.count(target))

    print("\n=== remove ===")
    before = len(arr1)
    arr1.remove(arr1[0])
    print(f"Довжина: {before} -> {len(arr1)}")

    print("\n=== pop ===")
    popped = arr1.pop()
    print("Вилучено з кінця:", popped)
    print("Довжина після pop:", len(arr1))

    print("\n=== del (за індексом) ===")
    del arr1[0]
    print("Довжина після del arr1[0]:", len(arr1))

    print("\n=== iter / for ===")
    for i, nb in enumerate(arr1):
        print(f"  [{i}] {nb}")

    print("\n=== reverse ===")
    arr1.reverse()
    print("Після reverse, перший:", arr1[0])

    print("\n=== copy ===")
    backup = arr1.copy()
    print("Копія (list), довжина:", len(backup))

    print("\n=== extend ===")
    arr1.extend(g5)
    print("Довжина після extend на 5 елементів:", len(arr1))

    print("\n=== clear ===")
    arr1.clear()
    print("Довжина після clear:", len(arr1))
    print("Вміст:", arr1)