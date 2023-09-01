class SparseTable:
    def __init__(self, rows = 0, cols = 0):
        self.rows = rows
        self.cols = cols
        self.matr = []
        self.added_cells = []

    def row_cols_counter(self):

        self.rows = len(self.matr)
        self.cols = len(self.matr[0])

    def __getitem__(self, item):
        if item[0]>self.rows-1 or item[1]>self.cols-1 or self.matr[item[0]][item[1]] == 0:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.matr[item[0]][item[1]][(item[0],item[1])].value if type(self.matr[item[0]][item[1]]) != int else self.matr[item[0]][item[1]]

    def __setitem__(self, key, value):
        if key[0]> self.rows-1 or key[1]> self.cols-1:
            self.add_data(key[0], key[1], value)
        elif type(self.matr[key[0]][key[1]]) in (int,float):
            self.matr[key[0]][key[1]] = value
        else:
            self.matr[key[0]][key[1]][(key[0],key[1])].value = value

    def add_data(self, row, col, data):
        if self.matr == []:
            self.matr = [[0 for i in range(col+1)] for j in  range(row+1)]
            self.matr[row][col] = {(row, col):data}
            self.row_cols_counter()
            self.added_cells.append((row, col))

        elif row<self.rows and col<self.cols:
            self.matr[row][col] = {(row, col): data}
            self.added_cells.append((row, col))

        else:
            rplus = row - self.rows
            cplus = col - self.cols


            if rplus>=0:
                for i in range((rplus)+1):
                    self.matr.append([0 for i in range(len(self.matr[0]))])

            if cplus>=0:
                for i in range(len(self.matr)):
                    for j in range((cplus)+1):
                        self.matr[i].append(0)

            self.matr[row][col] = {(row, col):data} if type(data) != int else data
            self.row_cols_counter()
            self.added_cells.append((row, col))


    def remove_data(self,row, col):
        if row > self.rows - 1 or col > self.cols - 1 or self.matr[row][col] == 0:
            raise IndexError('ячейка с указанными индексами не существует')
        self.added_cells.remove((row,col))
        print(self.added_cells)
        del self.matr[row][col]
        self.added_cells = sorted(self.added_cells,reverse=True)
        self.rows = self.added_cells[0][0]
        self.cols = self.added_cells[0][1]



class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
print(st.matr)
st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"



st.remove_data(1, 1)
print(st.rows,st.cols)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"