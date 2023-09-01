class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for i in range(3)] for j in range(3)]


    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = True
                j.value = 0


    def __getitem__(self, item):
        res = []
        if isinstance(item,tuple) and type(item[0]) != slice and type(item[1]) != slice:
            i,j = item
            return self.pole[i][j].value
        elif isinstance(item[0],slice):
            sl,indx = item
            for i in range(len(self.pole[sl])):
                res.append(self.pole[i][indx].value)
            return tuple(res)
        elif isinstance(item[1],slice):
            indx,sl = item
            for i in range(len(self.pole[sl])):
                res.append(self.pole[indx][i].value)
            return tuple(res)


    def __setitem__(self, key, value):
        try:
            i,j = key
            if self.pole[i][j].is_free == True:
                self.pole[i][j].value = value
            else:
                raise ValueError('клетка уже занята')
        except:
            raise IndexError('неверный индекс клетки')
class Cell:
    def __init__(self,is_free = True, value = 0):
        self.is_free = is_free
        self.value = value


    def __setattr__(self, key, value):
        if key == 'is_free' and type(value) == bool:
            object.__setattr__(self, key, value)
        elif key == 'value' and 0<=value<=3:
            object.__setattr__(self, key, value)

    def __bool__(self):
        return self.is_free


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
print(g[:, 0])
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
