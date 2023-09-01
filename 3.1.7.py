class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        self.__c = val

    def __setattr__(self, key, value):
        if key == "MIN_DIMENSION" or key == "MAX_DIMENSION":
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if type(value) in (int, float) and Dimensions.MIN_DIMENSION<= value <=Dimensions.MAX_DIMENSION:
            object.__setattr__(self, key, value)



d = Dimensions(10,20,30)
print(d.__dict__)