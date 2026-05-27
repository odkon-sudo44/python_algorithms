import datetime
from Practice1.notebook_dataclass import Notebook


if __name__ == "__main__":
    # Демонстраційну частину коду винесено окремо для забезпечення коректних результатів покриття тестів

    nb = Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)
    nb2 = nb
    print(nb)
    print(nb.get_info())
    print(nb.get_message())
    print(nb == nb2)
    nb3 = Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)
    print(nb3)
    print(nb3.get_info())
    print(nb3.get_message())
    print(nb == nb3)
    nb4 = Notebook("ASUS", "ROG Strix", 15.6, 16, "AMD Ryzen 7", 1024, datetime.date(2023, 6, 15))
    print(nb4)
    print(nb4.get_info())
    print(nb4.get_message())

    # Варіант з помилкою
    nb5 = Notebook("HP", "Pavilion", 4.0, 4, "Intel Celeron", 128)
    print(nb5)
    print(nb5.get_info())
    print(nb5.get_message())
