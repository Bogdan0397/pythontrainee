class Eclipse:
    def __init__(self, x1=None,y1=None,x2=None,y2=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __setattr__(self, key, value):
        if type(value) == int:
            object.__setattr__(self, key, value)

    def get_coords(self):
        if hasattr(self,'x1') and hasattr(self,'y1') and hasattr(self,'x2') and hasattr(self,'y2'):
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')

    def __bool__(self):
        try:
            self.get_coords()
            return True
        except:
            return False



lst_geom = [Eclipse(), Eclipse(), Eclipse(1, 0, 3, 5), Eclipse(2, 3, 4, 6)]

for i in lst_geom:
    if bool(i):
        i.get_coords()