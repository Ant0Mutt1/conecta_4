import numpy as np
HUMAN = 1
BOT  = 2
EMPTY = 0
COLS = 7
ROWS = 6
FOUR_CONNECTED = 4
def find_lower_position(state, col):
    row = 5
    while row >= 0:
        if state[row][col] == EMPTY:
            return row
        row -= 1
    return None

def possible_new_states(state, is_maximizing):
    children = []
    player = BOT if is_maximizing else HUMAN

    for col in range(7):
        row = find_lower_position(state, col)
        if row is not None: 
            new_state = state.copy()
            new_state[row][col]=player
            children.append(new_state)
    return children

def check_four_connected(state, player):
    # Comprobar horizontal
    for c in range(COLS-3):
        for r in range(ROWS):
            if all([state[r][c+i] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if all([state[r+i][c] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar diagonal (positiva)
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if all([state[r+i][c+i] == player for i in range(FOUR_CONNECTED)]):
                return True

    # Comprobar diagonal (negativa)
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if all([state[r-i][c+i] == player for i in range(FOUR_CONNECTED)]):
                return True

    return False

def check_board(state, player):
    score = 0

    # Puntuación horizontal
    for r in range(ROWS):
        row_array = [int(i) for i in list(state[r, :])]
        for c in range(COLS-3):
            window = row_array[c:c+FOUR_CONNECTED]
            score += check_window(window, player)

    # Puntuación vertical
    for c in range(COLS):
        columna_array = [int(i) for i in list(state[:, c])]
        for r in range(ROWS-3):
            window = columna_array[r:r+FOUR_CONNECTED]
            score += check_window(window, player)

    # Puntuación diagonal positiva
    for r in range(ROWS-3):
        for c in range(COLS-3):
            window = [state[r+i][c+i] for i in range(FOUR_CONNECTED)]
            score += check_window(window, player)

    # Puntuación diagonal negativa
    for r in range(3, ROWS):
        for c in range(COLS-3):
            window = [state[r-i][c+i] for i in range(FOUR_CONNECTED)]
            score += check_window(window, player)

    return score


def check_window(window, player):
    # Está evaluando es una "ventana" de 4 celdas consecutivas en el tablero, 
    # tanto horizontal, vertical como diagonalmente. 
    # ("window" es una subsección de 4 espacios adyacentes en el tablero)
    score = 0
    oponente = HUMAN if player == BOT else BOT

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(oponente) == 3 and window.count(EMPTY) == 1:
        score -= 4

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

def minimax(state, is_maximizing, alpha, beta, depth = 4):

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


def play():
    board = np.zeros((ROWS, COLS))

    playing = True
    while playing:

        col= int(input('columna: '))


        row = find_lower_position(board, col)
        board[row][col]=HUMAN
        for line in board:
            print(line)
        print()

        board = best_move(board)[1]

        for line in board:
            print(line)
        print()
        winner = evaluate(board)
        if winner == -1:
            print('ganaste!')
            playing = False
        elif winner == 1:
            print('ganó el bot!')
            playing = False
     
    return True

play()