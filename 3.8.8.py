class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        if not isinstance(item,slice):
            return self.coords[item]
        return tuple(self.coords[item])


    def __setitem__(self,key,value):
        self.coords[key] = value


r = RadiusVector(1,2,23,4,5,6)


print(r[2])