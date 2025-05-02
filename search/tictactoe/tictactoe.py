"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        for column in row:
            if column == X:
                countX+=1
            elif column == O:
                countO+=1
    
    if countX - countO == 0:
        return X
    else:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise NameError('Invalid Action')
    
    new_board = copy.deepcopy(board)
    next_player = player(new_board)
    
    new_board[action[0]][action[1]] = next_player
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontally
    for row in board:
        winner = 0
        for column in row:
            if column == X: winner+=1
            elif column == O: winner-=1
        if winner == 3: return X
        elif winner == -3: return O
        
    # Vertically
    for column in range(0,3):
        winner = 0
        for row in enumerate(board):
            if row[1][column] == X: winner+=1
            elif row[1][column] == O: winner-=1
        if winner == 3: return X
        elif winner == -3: return O
    
    # Diagonally left to right
    winner = 0
    for i, row in enumerate(board):
        if row[i] == X: winner+=1
        elif row[i] == O: winner-=1
        
        if winner == 3: return X
        elif winner == -3: return O
    
    # Diagonally right to left
    winner = 0
    for i, row in enumerate(board):
        if row[-i - 1] == X: winner+=1
        elif row[-i - 1] == O: winner-=1
        
        if winner == 3: return X
        elif winner == -3: return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    
    return _minimax_recursive(board)[1]
    
def _minimax_recursive(board):
    if terminal(board): return (utility(board), None)
    
    current_player = player(board)
    utilities = set()
    possible_actions = actions(board)
    
    for action in possible_actions:
        # Recursive call to evaluate the result of the action
        result_board = result(board, action)
        result_tuple = _minimax_recursive(result_board)
        utilities.add((result_tuple[0], action))
        
    if current_player == X:
        return max(utilities, key=lambda x: x[0])
    elif current_player == O:
        return min(utilities, key=lambda x: x[0])