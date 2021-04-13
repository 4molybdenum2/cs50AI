"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = 'X'
O = 'O'
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
    x = sum(row.count('X') for row in board)
    o = sum(row.count('O') for row in board)
    if x == o:
        return 'X'
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                actions.append((row,column))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board = copy.deepcopy(board)
    current_player = player(board)
    if current_player == 'X':
        temp_board[action[0]][action[1]] = X
    else:
        temp_board[action[0]][action[1]] = O

    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] is not EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] is not EMPTY:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] is not EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] is not EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_space = sum(row.count(EMPTY) for row in board)
    
    if empty_space == 0:
        return True
    else:
        if winner(board) is not None:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board)):
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0

def max_value(board):
    ''' 
    Returns the max value of the given state
    '''
    if(terminal(board)):
        return utility(board),None
    
    v = -2
    move = None
    for action in actions(board):
        temp,act = min_value(result(board,action))
        if v < temp:
            v = temp
            move = action
            if v == 1:
                return v,move
    
    return v,move

def min_value(board):
    ''' 
    Returns the max value of the given state
    '''
    if(terminal(board)):
        return utility(board),None
    
    v = 2
    move = None
    for action in actions(board):
        temp,act = max_value(result(board,action))
        if v > temp:
            v = temp
            move = action
            if v == -1:
                return v,move
    
    return v,move

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if(terminal(board)):
        return None
    else:
        if player(board) == 'X':
            value,move = max_value(board)
            return move
        else:
            value,move = min_value(board)
            return move
