class NewList:
    def __init__(self, l=[]):
        self.l = l

    def __sub__(self, obj):
        refl = self.l.copy()
        cl = obj
        if isinstance(obj,NewList):
            cl = obj.l


        for item1 in cl:
            if item1 in refl:
                for index, item2 in enumerate(refl):

                    if type(item1) is type(item2) and \
                            item1 == item2:
                        del refl[index]
                        break

        return NewList(refl)



    def __rsub__(self, obj):
        return NewList(obj) - self
    def get_list(self):
        return self.l


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4. 5]- lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
print(res3.get_list())
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"