# minimax.py
from utils import possible_new_states
from evaluation import evaluate

def minimax(state, is_maximizing, alpha, beta, depth=4):
    if depth == 0:
        return evaluate(state)

    score = evaluate(state)
    if score != 0:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for new_state in possible_new_states(state, True):
            score = minimax(new_state, False, alpha, beta, depth=depth-1)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for new_state in possible_new_states(state, False):
            score = minimax(new_state, True, alpha, beta, depth=depth-1)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def best_move(state):
    best_score = -float('inf')
    best_state = None
    for new_state in possible_new_states(state, True):
        score = minimax(new_state, False, -float('inf'), float('inf'))
        if score > best_score:
            best_score = score
            best_state = new_state
    return best_score, best_state
