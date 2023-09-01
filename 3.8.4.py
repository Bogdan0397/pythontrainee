class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, num):
        if type(num) != int:
            raise ValueError('должно быть целое число')
        self.__value = num


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.ar = [cell() for _ in range(max_length)]

    def __check_value(self, value):
        if type(value) != int or not 0 <= value < self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        return self.ar[item].value

    def __setitem__(self, key, item):
        self.__check_value(key)
        self.ar[key].value = item

    def __str__(self):
        return ' '.join([str(x.value) for x in self.ar])

ar_int = Array(10, cell=Integer)
print(ar_int[0])


