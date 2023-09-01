import sys
class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(float(self.score))



lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*i.split("; ")) for i in lst_in]
players_filtered = list(filter(lambda x: bool(x),players))
print(players_filtered)