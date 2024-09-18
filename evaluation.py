# evaluation.py
from constants import HUMAN, BOT, EMPTY, COLS, ROWS, FOUR_CONNECTED

def check_four_connected(state, player):
    # Comprobar horizontal
    for c in range(COLS - 3):
        for r in range(ROWS):
            if all([state[r][c + i] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all([state[r + i][c] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar diagonal positiva
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if all([state[r + i][c + i] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar diagonal negativa
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if all([state[r - i][c + i] == player for i in range(FOUR_CONNECTED)]):
                return True

    return False

def check_window(window, player):
    score = 0
    opponent = HUMAN if player == BOT else BOT

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def check_board(state, player):
    score = 0

    # Puntuación horizontal
    for r in range(ROWS):
        row_array = [int(i) for i in list(state[r, :])]
        for c in range(COLS - 3):
            window = row_array[c:c + FOUR_CONNECTED]
            score += check_window(window, player)

    # Puntuación vertical
    for c in range(COLS):
        column_array = [int(i) for i in list(state[:, c])]
        for r in range(ROWS - 3):
            window = column_array[r:r + FOUR_CONNECTED]
            score += check_window(window, player)

    # Puntuación diagonal positiva
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [state[r + i][c + i] for i in range(FOUR_CONNECTED)]
            score += check_window(window, player)

    # Puntuación diagonal negativa
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [state[r - i][c + i] for i in range(FOUR_CONNECTED)]
            score += check_window(window, player)

    return score

def evaluate(state):
    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            if state[row][col] == HUMAN:
                score -= check_board(state, HUMAN)
            elif state[row][col] == BOT:
                score += check_board(state, BOT)
    if check_four_connected(state, BOT):
        return 1
    elif check_four_connected(state, HUMAN):
        return -1
    return score
