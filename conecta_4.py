from os import system
import platform
class Game:
    def __init__(self) -> None:
        self.n_row = 6
        self.n_col = 7
        self.disc = 1
        self.disc_lacated = 0
        self.board = [[0 for _ in range(self.n_col)] for _ in range(self.n_row)] 

    def clear_screen(self):
        op_sys = platform.system()
        if op_sys=='Linux':
            system('clear')
        elif op_sys == 'Windows':
            system('cls')

    def show_board(self):
        # self.clear_screen()
        print('a  b  c  d  e  f  g')
        for row in self.board:
            for cell in row:
                print(cell, end="  ")
            print(end="\n")

    def shift(self):
        if self.disc == 1:
            self. disc = 2
        else:
            self.disc = 1

    def check_winner(self, row, col, disc):
    
        # Definir las directions en las que se verificará (horizontal, vertical, diagonal)
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        
        for d in directions:
            count = 1
            
            # Verificar en ambas directions (+d y -d)
            for dir in [1, -1]:
                dx = d[0] * dir
                dy = d[1] * dir

                x = row + dx
                y = col + dy
                
                while 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == disc:
                    count += 1
                    if count == 4:
                        print('ganador jugador', disc)
                        return True
                    x += dx
                    y += dy
        print('no hay ganador')            
        return False


    def check_full_col(self, input: int):
        if self.board[0][input] == 1 or self.board[0][input] == 2:
            self.n_row = 6
            self.disc_lacated -=1
            return False
        return True
    
    def play(self, input: int):

        self.n_row -= 1        
        if not self.check_full_col(input):
            
            return
        if self.board[self.n_row][input] == 0:
            self.board[self.n_row][input] = self.disc
            self.check_winner(self.n_row, input, self.disc)
            self.show_board()
            self.n_row = 6
            return True
        elif self.n_row == 0:
                self.n_row=6
                return
            
        self.play(input)

    def start(self):
        while True:
            pos = int(input('col: '))
            self.play(pos)
            self.disc_lacated +=1
            self.shift()

            if self.disc_lacated == 42:
                break

if __name__ == '__main__':
    game = Game()
    game.start()
