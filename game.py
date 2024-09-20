import numpy as np
from constants import HUMAN
from utils import find_lower_position
from minimax import best_move
from evaluation import evaluate

def play():
    board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
       ])
    playing = True
    while playing:
        col = input('column (0-6): ')
        try:
            if col == 'q':
                break
            col = int(col)
            row = find_lower_position(board, col)
            board[row][col] = HUMAN
            for line in board:
                print(line)
            print()
        except: 
            print('Invalid movement. Try again')
            continue

        board = best_move(board)[1]
        for line in board:
            print(line)
        print()

        winner = evaluate(board)
        if winner == -100:
            print('You have won!')
            playing = False
        elif winner == 100:
            print('You have lost!')
            playing = False

    return True

if __name__ == "__main__":
    play()
