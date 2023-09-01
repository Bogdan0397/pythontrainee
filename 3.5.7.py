class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c


    @classmethod
    def dim_check(cls, val):
        return cls.MIN_DIMENSION<=val<=cls.MAX_DIMENSION

    def volume(self):
        return self.a*self.b*self.c



    def __eq__(self, other):
        return self.dim_v() == other.dim_v()

    def __gt__(self, other):
        return self.dim_v() > other.dim_v()

    def __ge__(self, other):
        return self.dim_v() >= other.dim_v()


    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, val):
        if self.dim_check(val):
            self.__a = val

    @property
    def b(self):
        return self.__a
    @b.setter
    def b(self, val):
        if self.dim_check(val):
            self.__b = val

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, val):
        if self.dim_check(val):
            self.__c = val


class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


    def __setattr__(self, key, value):
        if key == "name" and type(value) == str:
            object.__setattr__(self, key, value)

        if key == "price" and type(value) in (int, float):
            object.__setattr__(self, key, value)

        if key == "dim" and type(value) == Dimensions:
            object.__setattr__(self, key, value)

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
