from utils import possible_new_states
from evaluation import evaluate
from constants import EMPTY, ROWS, COLS

def minimax(state, is_maximizing, alpha, beta, depth=3):
    score = evaluate(state)

    if depth == 0 or abs(score) == 100 or all(state[r][c] != EMPTY for r in range(ROWS) for c in range(COLS)):
        return score

    if is_maximizing:
        best_score = -float('inf')
        for new_state in possible_new_states(state, True):
            score = minimax(new_state, False, alpha, beta, depth - 1)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break 
        return best_score
    else:
        best_score = float('inf')
        for new_state in possible_new_states(state, False):
            score = minimax(new_state, True, alpha, beta, depth - 1)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  
        return best_score

def best_move(state):
    best_score = -float('inf')
    best_state = None
    possible_states = possible_new_states(state, True)

    # Ordena los posibles movimientos, antes de evaluarlos, de acuerdo a su probabilidad 
    # de ser los mejores (por ejemplo, probando primero movimientos que se consideran más prometedores). 
    # Esto puede aumentar la efectividad de la poda Alpha-Beta.
    possible_states.sort(key=lambda x: evaluate(x), reverse=True)

    for new_state in possible_states:
        score = minimax(new_state, False, -float('inf'), float('inf'))
        if score > best_score:
            best_score = score
            best_state = new_state

    return best_score, best_state