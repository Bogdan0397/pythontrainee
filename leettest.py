import sys
class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = {}


    def write(self, record):
        self.dict_db.setdefault(record,[]).append(record)

    def read(self, pk):
        for i in self.dict_db.keys():
            if i.pk == pk:
                return i

class Record:
    count = 0
    def __new__(cls, *args, **kwargs):
        cls.count+=1
        return object.__new__(cls)

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.count

    def __setattr__(self, key, value):
        if key in ("fio", "descr") and type(value) == str:
            object.__setattr__(self, key, value)
        if key == "old" and type(value) == int:
            object.__setattr__(self, key, value)
        if key == 'pk':
            object.__setattr__(self, key, value)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

db = DataBase('1')
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i in lst_in:
    x = i.split("; ")
    db.write(Record(x[0],x[1],int(x[2])))

print(db.dict_db)
