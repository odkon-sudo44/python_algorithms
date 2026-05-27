from generator import Generator
from Practice1.notebook_dataclass import Notebook


if __name__ == "__main__":

    nb = Notebook("Dell", "XPS 13", 13.3, 16, "Intel i7", 512)
    print(nb.get_info())
    print(nb)

    g = Generator()
    print(g.generate_single())

    g1000 = g.generate_1000()
    print(g1000)

    print(g1000[100].get_message())
    print(g1000[101].get_message())
    print(g1000[102].get_message())
    print(g1000[103].get_message())
    print(g1000[104].get_message())
    print(g1000[999].get_message())

