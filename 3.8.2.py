class Record:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
        self.keys = list(self.__dict__.keys())
        self.p4 = 5555


    def __getitem__(self, item):
        if isinstance(item,int) and item<len(self.keys):
            return self.__dict__[self.keys[item]]
        raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        setattr(self,self.keys[key],value)


t1  = Record(p1='111',p2 = 111,p3=1)
t1[0] = 'kkkk'
print(t1.p1)
