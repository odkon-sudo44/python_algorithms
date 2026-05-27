from AlgorithmsCourse.Practice1.student_dataclass import Student
from AlgorithmsCourse.Practice2.generator import Generator
from AlgorithmsCourse.Practice3.structureexamples import StructureExample


class Find(StructureExample):
    _list: list[Student] = []

    # def append(self, value: Student) -> None:
    #     pass
    #     # 2, 5, 9 -> 7
    #     # 2, 5, _7_, 9

    def find(self, value: Student) -> int | None:
        for (i, item) in enumerate(self._list):
            if item == value:
                return i
        # raise ValueError
        return None
        # return -1

    def find_by(self, value: Student):
        for (i, item) in enumerate(self._list):
            if (item.surname, item.name) == (value.surname, value.name):
                return i
        # raise ValueError
        return None

    def find_by_attr(self, value: Student, attr: str):
        for (i, item) in enumerate(self._list):
            if getattr(item, attr) == getattr(value, attr):
                return i
        # raise ValueError
        return None

    def find_by_lambda(self, value: Student, func):
        for (i, item) in enumerate(self._list):
            if func(item, value):
                return i
        # raise ValueError
        return None



if __name__ == "__main__":

    gen = Generator()
    st = [gen.generate_single() for _ in range(5)]
    for s in st:
        print(s)

    f = Find()
    f.append(st[0])
    f.append(st[1])
    f.append(st[2])
    f.append(st[3])
    f.append(st[4])

    print(f)
    print(f[0])

    print(  f.find(st[4]))
    print(  f.find_by(st[4]))

    print("---")
    print(  f.find_by_attr(st[4], 'surname'))
    print(  f.find_by_attr(st[4], 'discipline'))
    # [ 'surname', 'name']

    print("---")
    func = lambda x, y: x.surname == y.surname
    func2 = lambda x, y: (x.surname, x.name) == (y.surname, y.name)
    func3 = lambda x, y: (x.discipline) == (y.discipline)
    print(  f.find_by_lambda(st[4], func))
    print(  f.find_by_lambda(st[4], func2))
    print(  f.find_by_lambda(st[4], func3))





