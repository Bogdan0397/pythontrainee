class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.l = list(self.__dict__)
        self.attr = [self.fio,self.job,self.old,self.salary,self.year_job]


    def __iter__(self):
        self.val = -1
        return self

    def index_checker(self,indx):
        if indx>=len(self.attr):
            raise IndexError('неверный индекс')


    def __getitem__(self, indx):
        self.index_checker(indx)
        return self.attr[indx]

    def __setitem__(self, key, value):
        self.index_checker(key)
        self.attr[key] = value


    def __next__(self):
        if self.val < (len(self.attr)-1):
            self.val += 1
            return self.attr[self.val]
        else:
            raise StopIteration


p = Person('ss','sss',30,2500,15)

print(p.l)

for v in p:
    print(v)