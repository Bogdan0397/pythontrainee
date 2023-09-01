class PolyLine:
    def  __init__(self, start, *args):
        self.coords = [start] + list(args)


    def add_coord(self, x, y):
        self.coords.append(tuple(x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords


