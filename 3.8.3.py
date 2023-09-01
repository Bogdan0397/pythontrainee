class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

        self.track_list = []

    def add_point(self, x, y, speed):
        self.track_list.append([(x, y), speed])

    def __getitem__(self, item):
        if type(item) == int and 0 <= item < len(self.track_list):
            return self.track_list[item]
        raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if type(key) == int and 0 <= key < len(self.track_list):
            self.track_list[key][1] = value
        else:
            raise IndexError('некорректный индекс')



tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError


# t1 = Track(1,1)
#
# t1.add_point(2,2,60)
# print(t1.track_list)
# coords, speed =
