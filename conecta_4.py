from random import randint
JUGADOR = 'A'
BOT  = 'B'
VACIO = ' '
def find_lower_position(state, col):
    row = 5
    while row >= 0:
        if state[row][col] == VACIO:
            return row
        row -= 1
    return None

def possible_new_states(state, is_maximizing):
    children = []
    player = BOT if is_maximizing else JUGADOR

    for col in range(7):
        row = find_lower_position(state, col)
        if row is not None: 
            new_state = [row[:] for row in state]
            new_state[row][col]=player
            children.append(new_state)
    return children


def evaluate(state):
    if all(cell != ' ' for row in state for cell in row):
        return 0            
    for row in range(6):
        for col in range(7):
            axis = [(0, 1), (1, 0), (1, 1), (1, -1)]
            if state[row][col] != VACIO:
                if state[row][col] == BOT:
                    for d in axis:
                        count = 1
                        
                        for dir in [1, -1]:

                            dx = d[0] * dir
                            dy = d[1] * dir

                            x = row + dx
                            y = col + dy
                            while 0 <= x < len(state) and 0 <= y < len(state[0]) and state[x][y] == BOT:                        
                                count += 1
                                if count == 4:
                                    return 1

                                x += dx
                                y += dy
                elif state[row][col] == JUGADOR:

                    for d in axis:
                        count = 1
                        
                        for dir in [1, -1]:

                            dx = d[0] * dir
                            dy = d[1] * dir

                            x = row + dx
                            y = col + dy
                            while 0 <= x < len(state) and 0 <= y < len(state[0]) and state[x][y] == JUGADOR:
                                count += 1
                                if count == 4:

                                    return -1
                                
                                x += dx
                                y += dy
    return 0

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
    board = [
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]


    playing = True
    while playing:

        col= int(input('columna: '))


        row = find_lower_position(board, col)
        board[row][col]=JUGADOR
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