class Budget:
    def __init__(self):
        self.budget_l = []

    def add_item(self, it):
        self.budget_l.append(it)

    def remove_item(self, indx):
        self.budget_l.pop(indx)

    def get_items(self):
        return self.budget_l


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money


    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return self + other




