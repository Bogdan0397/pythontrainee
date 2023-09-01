class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []


    def add_product(self, product):
        self.goods.append(product)


    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    genid = 0
    @classmethod
    def idgen(cls):
        cls.genid+=1
        return cls.genid


    def __init__(self, name, weight, price):

        self.id = self.idgen()
        self.name = name
        self.weight = weight
        self.price = price


    def __setattr__(self, key, value):
        if key == "id" and isinstance(value, int):
            object.__setattr__(self, key, value)
        elif key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif key == "weight" and type(value) in (int, float) and value>0:
            object.__setattr__(self, key, value)
        elif key == "price" and type(value) in (int, float) and value>0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)








