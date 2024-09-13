from os import system
import platform
from random import randint
import time
class Game:
    def __init__(self) -> None:
        self.disc = 'A'
        self.board = [['O' for _ in range(7)] for _ in range(6)] 

    def clear_screen(self):
        op_sys = platform.system()
        if op_sys=='Linux':
            system('clear')
        elif op_sys == 'Windows':
            system('cls')

    def _show_board(self):
        # self.clear_screen()
        print('a  b  c  d  e  f  g')
        for row in self.board:
            for cell in row:
                print(cell, end="  ")
            print(end="\n")

    def _shift_disc(self):
        if self.disc == 'A':
            self.disc = 'B'
        else:
            self.disc = 'A'

    def _check_winner(self, row, col, disc):
        # Raliza una búsqueda de patrones en una matriz bidimensional
    
        # Define las direcciones en las que se verificará (horizontal, vertical, diagonal)
        axis = [(0, 1), (1, 0), (1, 1), (1, -1)]
        
        for d in axis:
            count = 1
            
            # Verifica en ambas direcciones (+d y -d)
            for dir in [1, -1]:
                # Cuanto se va a mover en el eje X y en el eje Y
                dx = d[0] * dir
                dy = d[1] * dir

                # Indices de la celda que debe verificar
                x = row + dx
                y = col + dy
                
                # Controla que la celda a verificar no esté fuera de rango (0 a 6 en el eje x, 0 a 5 el eje y)
                # y que el valor de la celda sea el mismo que el disco introducido.
                while 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == disc:
                    count += 1
                    if count == 4:
                        print('ganador player', disc)
                        return True
                    
                    # Continua revisando las celdas en el mismo eje hasta que encuentre 4 discos 
                    # iguales consecutivos o encuentre una celda vacía.
                    x += dx
                    y += dy
     
        return False
    def _find_col(self, disc, i_row, i_col):
        if disc == 'B':
            axis = [(0,1), (1,0), (1,1), (1,-1)]

            for d in axis:

                direc = [[1,2,3],[-1,-2,-3]]
                for dirs in direc:
                    values = []
                    for dir in dirs:
                        dx = d[0] * dir
                        dy = d[1] * dir

                        x = i_row + dx
                        y = i_col + dy
                        if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]):
                            values.append(self.board[x][y])

                            if self.board[x][y]=='O':
                                print(y)
                                col = y
                    if len(values) == 3 and values.count('B') == 2 and values.count('O')==1:
                        # Le suma 1 a la columna porque 0 es igual a False. el 
                        # metodo que lo utilice deberá restarle 1
                        return col +1            
                    
        return False
         
    def _check_immediate_threat(self):
        # TODO: mejora la deteccion en diagonales

        for i_row, row in enumerate(self.board):
            for i_col, disc in enumerate(row):
               col = self._find_col(disc, i_row, i_col)
               if col:
                   return col-1                                              
        return randint(0,6)
    
    def _find_lower_position(self, col):
        row = 5
        while True: 
            if self.board[row][col]=='O':
                return row
            row -= 1

    def play(self, bot=True):
        player = 'bot'
        playing = True
        while playing:
            if bot == False or player == 'human':
                col= int(input('columna: '))

            elif bot == True and player == 'bot':
                col = self._check_immediate_threat()

            row = self._find_lower_position(col)
            self.board[row][col]=self.disc
            self._show_board()
            winner = self._check_winner(row, col, self.disc)
            if winner:
                playing = False
            self._shift_disc()    
            player = 'human' if player == 'bot' else 'bot'
            if bot == True:
                time.sleep(1)
            
        return True
    
if __name__ == '__main__':
    game = Game()
    game.play()