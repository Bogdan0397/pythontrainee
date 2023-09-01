class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val


    def take(self):
        return self.__getattr__('_Circle__x')

    @property
    def y(self):
        return self.__y


    @y.setter
    def y(self, val):
        self.__y = val



    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        self.__radius = val

    def __setattr__(self, key, value):
        if not isinstance(value,(int,float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ("_Circle__x","_Circle__y") and type(value) in (int, float):
            object.__setattr__(self, key, value)
        elif key == "_Circle__radius" and type(value) in (int, float) and value>0:
            object.__setattr__(self, key, value)
        else:
            pass

    def __getattr__(self, item):
        return False



s = Circle(3,4,10)

print(s.take())