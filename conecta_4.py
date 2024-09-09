from os import system
import platform
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

    def show_board(self):
        # self.clear_screen()
        print('a  b  c  d  e  f  g')
        for row in self.board:
            for cell in row:
                print(cell, end="  ")
            print(end="\n")

    def shift_disc(self):
        if self.disc == 'A':
            self.disc = 'B'
        else:
            self.disc = 'A'

    def check_winner(self, row, col, disc):
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
                        print('ganador jugador', disc)
                        return True
                    
                    # Continua revisando las celdas en el mismo eje hasta que encuentre 4 discos 
                    # iguales consecutivos o encuentre una celda vacía.
                    x += dx
                    y += dy
     
        return False
    def check_immediate_threat(self):

        for i, row in enumerate(self.board):
            for j, disc in enumerate(row):
                if disc == 'A':
                    axis = [(0,1), (1,0), (1,1), (1,-1)]

                    for d in axis:
                        count = 1
                        for dir in [1,2,3]:
                            dx = d[0] * dir
                            dy = d[1] * dir

                            x = i + dx
                            y = j + dy
                            if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]):
                                if self.board[x][y] == 'A':
                                    count +=1
                                elif self.board[x][y] == 'B':
                                    count -=1
                        if count == 3:
                            print('amenaza') 
                            return                             

    def play(self):
        playing = True
        row = 5
        disc_in_game = False
        while playing:
            # Controla si ya se introdujo el disco
            if not disc_in_game:
                col= int(input('columna: '))
            disc_in_game = True

            if row >= 0 and self.board[row][col] == 'O':
                self.board[row][col]=self.disc
                self.check_immediate_threat()
                self.show_board()
                winner = self.check_winner(row, col, self.disc)
                if winner:
                    playing = False
                self.shift_disc()
                row = 5
                disc_in_game = False
            elif row < 0:
                row = 5
                disc_in_game = False
            elif not self.board[row][col] == 'O':
                row -= 1 
                

        return True

if __name__ == '__main__':
    game = Game()
    game.play()
