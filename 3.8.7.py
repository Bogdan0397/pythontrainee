class StackObj:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    top = None
    tmp = 0
    counter = -1

    def push(self, obj):

        if Stack.top == None:
            Stack.top = obj
            Stack.tmp = obj
            Stack.counter +=1

        elif Stack.top.next == None and Stack.top != None:
            Stack.top.next = obj
            Stack.tmp = obj
            Stack.counter += 1

        else:
            Stack.tmp.next = obj
            Stack.tmp = obj
            Stack.counter += 1


    def pop(self):
        tmp = 0
        obj = Stack.top
        while obj.next.next != None:
            obj = obj.next
        else:
            tmp = obj.next
            obj.next = None
            Stack.counter -= 1
            Stack.tmp = obj
        return tmp


    def __getitem__(self, item):

        if 0 > item or item > Stack.counter:
            raise IndexError('неверный индекс')
        res = Stack.top
        for i in range(item):
            res = res.next

        return res


    def __setitem__(self, key, value):
        if 0 > key or key > Stack.counter:
            raise IndexError('неверный индекс')
        res = Stack.top
        tmp = 0
        for i in range(key):
            tmp = res
            res = res.next

        tmp.next = value
        value.next = res.next


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")

assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"
print(Stack.counter)

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
#
#
# s1 = StackObj(1)
# s2 = StackObj(2)
# s3 = StackObj(3)
# s4 = StackObj(4)
# s5 = StackObj(5)
#
# st = Stack()
#
# st.push(s1)
# st.push(s2)
# st.push(s3)
# st.push(s4)
# st.push(s5)
