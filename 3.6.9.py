class Dimensions:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        try:
            if int(value) <= 0:
                raise ValueError("габаритные размеры должны быть положительными числами")
            object.__setattr__(self, key, int(value))
        except:
            if float(value) <= 0:
                raise ValueError("габаритные размеры должны быть положительными числами")
            object.__setattr__(self, key, float(value))

    def __hash__(self):
        return hash((self.a, self.b, self.c))

s_inp = list(map(str, input().split("; ")))

lst_dims = [Dimensions(*i.split()) for i in s_inp]
lst_dims = sorted(lst_dims, key= lambda x: hash(x))
