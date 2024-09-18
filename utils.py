# utils.py
import numpy as np
from constants import EMPTY, HUMAN, BOT, COLS, ROWS

def find_lower_position(state, col):
    row = ROWS - 1
    while row >= 0:
        if state[row][col] == EMPTY:
            return row
        row -= 1
    return None

def possible_new_states(state, is_maximizing):
    children = []
    player = BOT if is_maximizing else HUMAN

    for col in range(COLS):
        row = find_lower_position(state, col)
        if row is not None:
            new_state = state.copy()
            new_state[row][col] = player
            children.append(new_state)
    return children
