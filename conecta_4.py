from os import system
class Game:
    def __init__(self) -> None:
        self.n_row = 6
        self.n_col = 7
        self.disc = 'A'
        self.disc_lacated = 0
        self.board = [['O' for _ in range(self.n_col)] for _ in range(self.n_row)] 

    def show_board(self):
        system('cls')
        print('a  b  c  d  e  f  g')
        print()
        for row in self.board:
            for cell in row:
                print(cell, end="  ")
            print(end="\n")

    def shift(self):
        if self.disc == 'A':
            self. disc = 'B'
        else:
            self.disc = 'A'

    def check_full_col(self, input: int):
        if self.board[0][input] == 'A' or self.board[0][input] == 'B':
            self.n_row = 6
            self.disc_lacated -=1
            return False
        return True
    
    def play(self, input: int):

        self.n_row -= 1        
        if not self.check_full_col(input):
            
            return
        if self.board[self.n_row][input] == 'O':
            self.board[self.n_row][input] = self.disc
            self.show_board()
            self.n_row = 6
            return True
        elif self.n_row == 0:
                self.n_row=6
                return
            
        self.play(input)

    def start(self):
        while True:
            pos = int(input('columna: '))
            self.play(pos)
            self.disc_lacated +=1
            self.shift()

            if self.disc_lacated == 42:
                break

if __name__ == '__main__':
    game = Game()
    game.start()
