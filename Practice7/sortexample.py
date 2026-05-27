from AlgorithmsCourse.Practice1.student_dataclass import Student
from AlgorithmsCourse.Practice2.generator import Generator
from AlgorithmsCourse.Practice3.structureexamples import StructureExample


class Sort(StructureExample):
    _list: list[Student] = []

    def sort(self):
        for i in range(len(self._list) - 1, 0, -1):
            for k in range(0, i):
                if self._list[k] > self._list[k+1]:
                    # tmp = self._list[k]
                    # self._list[k] = self._list[k+1]
                    # self._list[k+1] = tmp
                    self._list[k], self._list[k+1] = self._list[k+1], self._list[k]

    # _5, 3, 9, 2_, 7
    #  5, 3
    #  3, 5
    #     5, 9
    #        9, 2
    #        2, 9
    #           9, 7
    #  _3, 5, 2_, 7, _9_
    #  3, 5
    #     2--5
    #        5, 7
    #  _3, 2_, 5, 7, 9
    #  2--3
    #     3, 5

    def sort_by(self):
        for i in range(len(self._list) - 1, 0, -1):
            for k in range(0, i):
                if self._list[k].surname > self._list[k+1].surname:
                    # tmp = self._list[k]
                    # self._list[k] = self._list[k+1]
                    # self._list[k+1] = tmp
                    self._list[k], self._list[k+1] = self._list[k+1], self._list[k]

    def sort_by_lambda(self, func):
        for i in range(len(self._list) - 1, 0, -1):
            for k in range(0, i):
                if func(self._list[k], self._list[k+1]):
                    # tmp = self._list[k]
                    # self._list[k] = self._list[k+1]
                    # self._list[k+1] = tmp
                    self._list[k], self._list[k+1] = self._list[k+1], self._list[k]


if __name__ == "__main__":

    gen = Generator()
    st = [gen.generate_single() for _ in range(5)]
    print(st)
    print('---')

    sort = Sort()
    sort.append(st[0])
    sort.append(st[1])
    sort.append(st[2])
    sort.append(st[3])
    sort.append(st[4])
    for s in sort:
        print(s)

    print('---')
    sort.sort()
    print(sort[0])
    print(sort[1])
    print(sort[2])
    print(sort[3])
    print(sort[4])


    print('---')
    func1 = lambda x, y: (x.surname, x.name) > (y.surname, y.name)
    func2 = lambda x, y: (x.discipline, x.mark) > (y.discipline, y.mark)

    sort.sort_by_lambda(func2)
    for i in range(len(sort)):
        print(sort[i])

    print()
    sort.sort_by_lambda(func1)
    for i in range(len(sort)):
        print(sort[i])
