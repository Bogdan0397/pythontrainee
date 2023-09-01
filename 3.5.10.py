class Box:
    def __init__(self):
        self.InBox = []

    def add_thing(self, obj):
        self.InBox.append(obj)

    def get_things(self):
        return self.InBox

    def __eq__(self, other):
        if len(self) != len(other):
            return: False

        count = 0
        for i in self.InBox:
            for j in other.InBox:
                if i == j:
                    count+=1
        if counter < len(self):
            return False
        return True

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

r1 = Thing('тряпка', 200)
r2 = Thing('ряпка', 200)

print(r1==r2)