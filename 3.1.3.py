


class Lessonitem:
    def __init__(self,title,practices,duration):
        self.title = title
        self.practices = practices
        self.duration = duration


    def __setattr__(self, key, value):
        if key == 'title' and type(value) == str:
            object.__setattr__(self,key,value)
        elif key in ('practices','duration'):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title','practice','duration'):
            pass
        else:
            object.__delattr__(self,item)


class Module:
    def __init__(self,name):
        self.name = name
        self.lessons = []


    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        indx = indx-1
        self.lessons.pop(indx)

class Course:

    def __init__(self,name):
        self.name = name
        self.modules = []


    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        indx = indx-1
        self.lessons.pop(indx)