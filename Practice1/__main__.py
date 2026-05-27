from Practice1.student_dataclass import Student
# from student_dataclass import Student


if __name__ == "__main__":
    # Демонстраційну частину коду винесено окремо для забезпечення коректних результатів покриття тестів

    st = Student("Тарас", "Тарасов", "АСД", 88)
    st2 = st
    print(st)
    print(st.get_info())
    print(st.get_message())
    print(st == st2)
    st3 = Student("Тарас", "Тарасов", "АСД", 88)
    print(st3)
    print(st3.get_info())
    print(st3.get_message())
    print(st == st3)
    st4 = Student("Петро", "Стеценко", "АСД", 67,"залік")
    print(st4)
    print(st4.get_info())
    print(st4.get_message())

    # Варіант з помилкою
    st5 = Student("Сергій", "Тимошко", "АСД", "45")
    print(st5)
    print(st5.get_info())
    print(st5.get_message())
