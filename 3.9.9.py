

import numpy as np
class Matrix:
    def __init__(self,*args):
        l_2d = list(args)
        if len(l_2d) == 1:
            self.matrix = l_2d[0]
            self.rows = len(l_2d[0])
            self.cols = len(l_2d[0][0])
        else:
            self.rows = l_2d[0]
            self.cols = l_2d[1]
            self.fill_value = l_2d[2]
            self.matrix = [[self.fill_value for x in range(self.cols)]for j in range(self.rows)]

    def __setattr__(self,key,value):
        if key in ('rows','cols') and type(value) == int:
            object.__setattr__(self,key,value)
        elif key == 'fill_value' and type(value) in (int,float):
            object.__setattr__(self,key,value)
        elif type(value) == list:
            for i in value:
                for j in i:
                    if len(i) != len(value[0]) or type(j) not in (int,float):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            object.__setattr__(self, key, value)
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def matrix_check(self,matr):
        if len(self.matrix[0]) != len(matr[0]):
            raise ValueError('операции возможны только с матрицами равных размеров')
    def __add__(self, other):
        if type(other) == Matrix:
            other = other.matrix
            self.matrix_check(other)
        return Matrix(np.add(self.matrix,other).tolist())

    def __sub__(self, other):
        if type(other) == Matrix:
            other = other.matrix
            self.matrix_check(other)
        return Matrix(np.subtract(self.matrix,other).tolist())


    def __getitem__(self, item):
        if type(item[1]) != int or type(item[0]) != int or item[0]>self.rows-1 or item[1]>self.cols-1 or item[0]<0 or item[1]<0:
            raise IndexError('недопустимые значения индексов')
        return self.matrix[item[0]][item[1]]

    def __setitem__(self, key, value):
        if type(value) not in (int,float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[key[0]][key[1]] = value


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)

assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])

matrix = m1 + m2

assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"