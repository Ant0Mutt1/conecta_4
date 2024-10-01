import numpy as np
from constants import HUMAN
from utils import find_lower_position
from minimax import best_move
from evaluation import evaluate


class Game():

    board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])
    playing = True

    def show_board(self):
        for line in self.board:
            print(line)
        print()

    def human_move(self):
        while True:
            col = input('column (0-6, q to quit): ')
            if col == 'q':
                self.playing = False
                return
            try:
                col = int(col)
                row = find_lower_position(self.board, col)
                if row is not None:
                    self.board[row][col] = HUMAN
                    self.show_board()
                    return
                else:
                    print("Column full, try again.")
            except (ValueError, IndexError):
                print('Invalid movement. Try again.')

    def bot_move(self):
        self.board = best_move(self.board)[1]
        self.show_board()       

    def check_winner(self):
        winner = evaluate(self.board)
        if winner == -100:
            print('You have won!')
            self.playing = False
        elif winner == 100:
            print('You have lost!')
            self.playing = False

    def play(self):
        while self.playing:
            self.human_move()
            self.check_winner()  
            
            if not self.playing: 
                break
            
            self.bot_move()
            self.check_winner()  

        return True

if __name__ == "__main__":
    game = Game()
    game.play()
