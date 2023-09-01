from random import choice, randint as r

class GamePole:
    is_pole = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for i in range(self.M)] for j in range(self.N)]
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def __new__(cls, *args, **kwargs):
        if cls.is_pole is None:
            cls.is_pole = super().__new__(cls)
        return cls.is_pole

    def init_pole(self):
        m = 0

        while m<self.total_mines:
            i = r(0, self.N - 1)
            j = r(0, self.M - 1)
            if self.pole[i][j].is_mine:
                continue
            self.pole[i][j].is_mine = True
            m+=2

            indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
            for x in range(self.N):
                for y in range(self.M):
                    if not self.pole[x][y].is_mine:
                        mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self.N and 0 <= y + j < self.M))
                        self.pole[x][y].number = mines



    def open_cell(self,i, j):
        self.pole[i][j].is_open = True


    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))




################################################################################

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.__number = around_mines
        self.__is_mine = mine
        self.__is_open = True


    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, value):
        if 0<=value<=8  and type(value) == int:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, value):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")


    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) == bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1
p2.show_pole()
assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"

