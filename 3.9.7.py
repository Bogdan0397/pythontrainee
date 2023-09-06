
import pytest

class StackObj:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None

    def push_front(self, obj):
        if self.top:
            temp = self.top
            self.top = obj
            self.top.next = temp
        else:
            self.top = obj

    def __len__(self):
        counter = 0
        temp = self.top
        while temp != None:
            temp = temp.next
            counter += 1
        return counter

    def index_check(self,indx):
        if indx>len(self)-1 or type(indx) != int:
            raise IndexError('неверный индекс')

    def push_back(self, obj):
        if self.top:
            temp = self.top
            last = None
            while temp.next != None:
                last = temp
                temp = last.next
            if self.top.next != None:
                last.next.next = obj
            else:
                self.top.next = obj
        else:
            self.top = obj

    def __setitem__(self, key, value):
        self.index_check(key)
        counter = 0
        temp = self.top
        while counter < key:
            temp = temp.next
            counter +=1
        temp.data = value

    def __getitem__(self, item):
        self.index_check(item)
        counter = 0
        temp = self.top
        while counter < item:
            temp = temp.next
            counter += 1
        return temp.data

    def __iter__(self):
        temp = self.top
        elem = 0
        while temp != None:
            elem = temp
            temp = temp.next
            yield elem


def push_back(stack: Stack, obj: StackObj):
    """ Add StackObj to the end. """
    stack._length += 1
    if not stack.top:
        return _push_back_in_empty_stack(stack, obj)
    _push_back_in_filled_stack(stack, obj)  # 1+ nodes in stack


def get_node(stack: Stack, key: int) -> StackObj:
    node = stack.top
    for _ in range(key):
        node = node.next
    return node


def _push_back_in_empty_stack(stack: Stack, obj: StackObj):
    if stack.top is None:  # empty stack
        stack.top = obj


def _push_back_in_filled_stack(stack: Stack, obj: StackObj):
    current_node = stack.top  # not empty stack
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = obj



c1 = Stack()

c1.push_front(StackObj('1'))
c1.push_back(StackObj('2'))
c1.push_front(StackObj('3'))
c1.push_back(StackObj('4'))


print(c1.top.data)
print(c1.top.next.data)
print(c1.top.next.next.data)
print(c1.top.next.next.next.data)
print('----------------------------------------')
c1[2] = 'sssss'
print(c1.top.data)
print(c1.top.next.data)
print(c1.top.next.next.data)
print(c1.top.next.next.next.data)
print('----------------------------------------')
for i in c1:
    print(i.data)

print('----------------------------------------')

print(c1[3])