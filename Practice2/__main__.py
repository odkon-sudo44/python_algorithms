from generator import Generator
from AlgorithmsCourse.Practice1.student_dataclass import Student


if __name__ == "__main__":

    st = Student("Тарас", "Тарасов", "АСД", 88)
    print(st.get_info())
    print(st)

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

