class Stack:
    tmp = None
    def __init__(self, top=None):
        self.top = top


    def push_back(self, obj):
        if self.top == None:
            self.top = obj
            self.tmp = obj
        else:
            self.tmp.next = obj
            self.tmp = obj




    def pop_back(self):
        tmp = self.top
        res = None
        if self.top.next == None:
            self.top = None

        else:
            while tmp.next != None:
                res = tmp
                tmp = tmp.next


            else:
                res.next = None

    def __add__(self, other):
        self.push_back(other)
        return self



    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, val):
        self.__next = val


st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"




