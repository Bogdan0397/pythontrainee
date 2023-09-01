class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self,val):
        self.__prev = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next= val
class LinkedList:
    tmp = None
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def next(self, val):
        self.__head = val

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def next(self, val):
        self.__tail = val
    def add_obj(self, obj):

        if self.__head == None:
            self.__head = obj
            self.__tail = obj
            LinkedList.tmp = obj
        elif LinkedList.tmp != obj and self.__head == self.__tail:
            self.__tail = obj
            obj.prev = self.__head
            self.__head.next = self.__tail
            LinkedList.tmp = obj
        else:
            self.__tail = obj
            obj.prev = LinkedList.tmp
            LinkedList.tmp.next = obj
            LinkedList.tmp = obj

    def remove_obj(self, indx):
        tmp = self.__head
        counter = 0

        while counter < indx:
            tmp = tmp.next
            counter += 1
        else:

            if self.__head == self.__tail and indx == 0:
                self.__head = None
                self.__tail = None
            elif tmp == self.__head:
                self.__head = tmp.next
                tmp.next.prev = None
            elif tmp == self.__tail:
                self.__tail = tmp.prev
                self.__tail.next = None
                LinkedList.tmp = LinkedList.tmp.prev
            else:
                tmp.next.prev = tmp.prev
                tmp.prev.next = tmp.next

    def __len__(self):
        counter = 1
        if self.__head == None:
            return 0
        tmp = self.__head
        while tmp.next != None:
            tmp = tmp.next
            counter += 1
        return counter

    def __call__(self,indx, *args, **kwargs):
        tmp = self.__head
        counter = 0
        while counter < indx and tmp != None:
            tmp = tmp.next
            counter += 1
        return tmp.data


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))

assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"

h = LinkedList()
h.add_obj(ObjList('Hello'))
h.remove_obj(0)
print(h.__dict__)