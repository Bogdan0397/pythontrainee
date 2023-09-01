import sys

# здесь объявляйте класс

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

c = [x.split('; ') for x in lst_in]

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

in]

lst_bs = [BookStudy(*i.split('; ')) for i in lst_
unique_books = len({hash(x) for x in lst_bs})
print(unique_books)

