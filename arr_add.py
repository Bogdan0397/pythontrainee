class Vector:
    def __init__(self, *args):
        self.vector = list(args)


    def __add__(self,other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.vector[i]+(other.vector[i] if type(other)==Vector else other) for i in range(len(self.vector))])


    def __iadd__(self, other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        self.vector = [self.vector[i] + (other.vector[i] if type(other)==Vector else other) for i in range(len(self.vector))]
        return self


    def __sub__(self,other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.vector[i]-(other.vector[i] if type(other)==Vector else other) for i in range(len(self.vector))])

    def __isub__(self, other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        self.vector = [self.vector[i] - (other.vector[i] if type(other) == Vector else other) for i in range(len(self.vector))]
        return self
    def __mul__(self,other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.vector[i]*(other.vector[i] if type(other)==Vector else other) for i in range(len(self.vector))])

    def __imul__(self, other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        self.vector = [self.vector[i] * (other.vector[i] if type(other) == Vector else other) for i in range(len(self.vector))]
        return self

    def __eq__(self, other):
        if type(other) == Vector and len(self.vector) != len(other.vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return self.vector == other.vector

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)


print((v1 + v2).vector)  # [5, 7, 9]
print((v1 - v2).vector)  # [-3, -3, -3]
print((v1 * v2).vector)  # [4, 10, 18]

v1 += 10
print(v1.vector)  # [11, 12, 13]
v1 -= 10
print(v1.vector)  # [1, 2, 3]
v1 += v2
print(v1.vector)  # [5, 7, 9]
v2 -= v1
print(v2.vector)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True