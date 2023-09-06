
import random
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2

    TURNS = 0


    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.TURNS = 0
        self.DFlag = False
        self.CFlag = False
        self.Hflag = False



    def __bool__(self):
        if not self.is_human_win or not self.is_computer_win or not self.is_draw:
            return True
        else:
            return False
    def check_index(self, i):
        if type(i) != int or i not in (0,1,2):
            raise IndexError('некорректно указанные индексы')
    def __getitem__(self, item):
        i,j = item
        self.check_index(i)
        self.check_index(j)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i,j = key
        self.check_index(i)
        self.check_index(j)
        self.pole[i][j].value = value

    def show(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].value == TicTacToe.FREE_CELL:
                    print('E',end=" ")
                elif self.pole[i][j].value == TicTacToe.HUMAN_X:
                    print('X',end=" ")
                elif self.pole[i][j].value == TicTacToe.COMPUTER_O:
                    print('0',end=" ")
            print('\n')


    def human_go(self,item):
        i,j = item
        self.pole[i][j].value = TicTacToe.HUMAN_X
        self.TURNS +=1


    def computer_go(self):
        i = random.randint(0,2)
        j = random.randint(0,2)
        counter = 0
        while self.pole[i][j].value == self.FREE_CELL and counter <=3:
            if self.pole[i][j].value == self.FREE_CELL:
                self.pole[i][j].value = self.COMPUTER_O
                counter += 1
            else:
                i = random.randint(0, 2)
                j = random.randint(0, 2)
        self.TURNS +=1
    @property
    def is_human_win(self):
        self.Hflag = False
        counterx = 0
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].value == self.HUMAN_X:
                    counterx +=1
            if counterx == 3:
                self.Hflag = True
            counterx = 0


        for i in range(len(self.pole[0])):
            for j in range(len(self.pole)):
                if self.pole[j][i].value == self.HUMAN_X:
                    counterx += 1
            if counterx == 3:
                self.Hflag = True

            counterx = 0

        # Diagonals
        counter_fd = 0
        counter_sd = 0
        for i in range(len(self.pole)):
            if self.pole[i][i].value == self.HUMAN_X:
                counter_fd += 1
            if self.pole[i][-1-i].value == self.HUMAN_X:
                counter_sd += 1
        if counter_fd == 3 or counter_sd == 3:
            self.Hflag = True

        return self.Hflag

    @property
    def is_computer_win(self):
        self.CFlag = False
        counterc = 0
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].value == self.COMPUTER_O:
                    counterc += 1
            if counterc == 3:
                self.CFlag = True
            counterc = 0

        for i in range(len(self.pole[0])):
            for j in range(len(self.pole)):
                if self.pole[j][i].value == self.COMPUTER_O:
                    counterc += 1
            if counterc == 3:
                self.CFlag = True
            counterc = 0

        #Diagonals
        counter_fd = 0
        counter_sd = 0
        for i in range(len(self.pole)):
            if self.pole[i][i].value == self.COMPUTER_O:
                counter_fd +=1
            if self.pole[i][-1-i].value == self.COMPUTER_O:
                counter_sd +=1
        if counter_fd == 3 or counter_sd == 3:
            self.CFlag = True


        return self.CFlag

    @property
    def is_draw(self):
        self.DFlag = False
        if self.TURNS == 9:
            self.DFlag = True
        return self.DFlag
class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False

    def __setattr__(self, key, value):
        if key == "value" and type(value) == int and value in (0,1,2):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверное значение")
