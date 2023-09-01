class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_mass(self):
        return self.ro * self.volume

    def __eq__(self, other):
        val = other.get_mass if type(other) == Body else other
        return self.get_mass == val

    def __lt__(self, other):
        val = other.get_mass if type(other) == Body else other
        return self.get_mass < val





b1 = Body("rock", 1, 10)
b2 = Body("rock", 1, 20)

print(b1<2000)
