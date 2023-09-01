class Triangle_Desc:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self._name, value)

import math
class Triangle:
    a = Triangle_Desc()
    b = Triangle_Desc()
    c = Triangle_Desc()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check()

    def check(self):
        if self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")


    def __len__(self):
        return int(self.a+self.b+self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)/2
        return math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))