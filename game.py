# game.py
import numpy as np
from constants import HUMAN, ROWS, COLS
from utils import find_lower_position
from minimax import best_move
from evaluation import evaluate

def play():
    board = np.zeros((ROWS, COLS))
    playing = True
    while playing:
        col = int(input('columna: '))
        row = find_lower_position(board, col)
        board[row][col] = HUMAN
        for line in board:
            print(line)
        print()

        board = best_move(board)[1]
        for line in board:
            print(line)
        print()

        winner = evaluate(board)
        if winner == -1:
            print('¡Ganaste!')
            playing = False
        elif winner == 1:
            print('¡Ganó el bot!')
            playing = False

    return True

if __name__ == "__main__":
    play()
