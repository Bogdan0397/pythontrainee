class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        now = self.clock1.get_time() - self.clock2.get_time()
        if now <0:
            return f"00: 00: 00"
        hours = int(now / 3600)
        rest = now % 3600
        minutes = int(rest / 60)
        rest = rest % 60
        seconds = rest
        return f"{str(hours).rjust(2,'0')}: {str(minutes).rjust(2,'0')}: {str(seconds).rjust(2,'0')}"

    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time()

    def __call__(self,*args, **kwargs):
        print(str(self))



class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __setattr__(self, key, value):
        if type(value) == int and value > 0:
            object.__setattr__(self, key, value)

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

s = Clock(10,35,58)
s1 = Clock(10,34,58)
res = DeltaClock(s,s1)

print(str(res))