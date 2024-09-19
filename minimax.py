from utils import possible_new_states
from evaluation import evaluate
from constants import *
import numpy as np
def minimax(state, depth, is_maximizing, alpha, beta):
    score = evaluate(state)

    # Retornar la puntuación si hay un resultado terminal
    if depth == 0 or abs(score) == 100 or all(state[r][c] != EMPTY for r in range(ROWS) for c in range(COLS)):
        return score

    if is_maximizing:
        best_score = -float('inf')
        for new_state in possible_new_states(state, True):
            score = minimax(new_state, depth - 1, False, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break 
        return best_score
    else:
        best_score = float('inf')
        for new_state in possible_new_states(state, False):
            score = minimax(new_state, depth - 1, True, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  
        return best_score

def best_move(state):
    best_score = -float('inf')
    best_state = None

    for new_state in possible_new_states(state, True):
        score = minimax(new_state, 4, False, -float('inf'), float('inf'))
        if score > best_score:
            best_score = score
            best_state = new_state

    return best_score, best_state


if __name__  == '__main__':
    lista_1 = np.array([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ])
    x = best_move(lista_1)

    print(x)
