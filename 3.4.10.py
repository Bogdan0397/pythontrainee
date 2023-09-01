class MaxPooling:
    def __init__(self, step=(2, 2), size=(3, 3)):
        self.step = step
        self.size = size


    def __call__(self, obj, *args, **kwargs):
        return self.max_pool(obj)

    def __l





    def max_pool(self, matr):
        l = []
        tmp = 0
        res = []
        if  False not in list(map(lambda x: len(x)==len(matr),matr)):
            for x in matr:
                for j in x:
                    if type(j) not in (int,float):
                        raise ValueError("Неверный формат для первого параметра matrix.")
        else:
            raise ValueError("Неверный формат для первого параметра matrix.")

        for i in range(0,len(matr), self.step[1]):
            for j in range(0,len(matr[0]), self.step[0]):
                # try:
                #     l = [matr[i + x][j:j + self.size[0]]for x in range(self.size[1])]
                # except:
                #     continue
                for x in range(self.size[1]):
                    if j+self.size[0] > len(matr[0]) or i+self.size[1] > len(matr):
                        break
                    else:
                        tmp = matr[i+x]
                        l.append(tmp[j:j+self.size[0]])



        r = [item for sublist in l for item in sublist]
        res = [max(r[i:i+self.size[0]**2]) for i in range(0,len(r),self.size[0]**2)]
        res = [res[i:i+2] for i in range(0, len(res), 2)]
        return res



mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"