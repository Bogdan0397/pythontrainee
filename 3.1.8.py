import time


class Mechanical:
    def __init__(self,date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key not in self.__dict__.keys() and type(value) == float and value>0:
            object.__setattr__(self, key, value)



class Aragon:
    def __init__(self,date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key not in self.__dict__.keys() and type(value) == float and value > 0:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self,date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key not in self.__dict__.keys() and type(value) == float and value > 0:
            object.__setattr__(self, key, value)

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot1 = 0
        self.slot2 = 0
        self.slot3 = 0

    def __setattr__(self, key, value):
        if key == "slot1" and type(value) in (Mechanical,int) or value == 0:
            object.__setattr__(self, key, value)
        if key == "slot2" and type(value) in (Aragon,int) or value == 0:
            object.__setattr__(self, key, value)
        if key == "slot3" and type(value) in (Calcium,int) or value == 0:
            object.__setattr__(self, key, value)



    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.slot1 == 0:
            self.slot1 = filter
        if slot_num == 2 and self.slot2 == 0:
            self.slot2 = filter
        if slot_num == 3 and self.slot3 == 0:
            self.slot3 = filter



    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.__dict__['slot1'] = 0
        if slot_num == 2:
            self.__dict__['slot2'] = 0
        if slot_num == 3:
            self.__dict__['slot3'] = 0




    def get_filters(self):
        return (self.slot1,self.slot2,self.slot3, )


    def get_limit(self, filter):
        return 0<=(time.time()-filter.date)<=GeyserClassic.MAX_DATE_FILTER


    def water_on(self):
        return True if 0 not in (self.slot1,self.slot2,self.slot3) and self.get_limit(self.slot1) and self.get_limit(self.slot2) and self.get_limit(self.slot3) else False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))

my_water.add_filter(2, Aragon(time.time()))


assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))

assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
print(my_water.get_filters())
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"