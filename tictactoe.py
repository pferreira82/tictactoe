"""
Tic Tac Toe Player
"""
import copy
import math

import helpers as helper

x_player = "X"
o_player = "O"
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
    # Assign X and O to 0 turns for start of the game
    x_turn = 0
    o_turn = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == x_player:
                x_turn += 1
            elif board[row][col] == o_player:
                o_turn += 1
    return x_player if x_turn == o_turn else o_player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    # Assign a set of possible actions that can be taken on a given board
    possible_actions = set()
    # loop through rows and columns of board to add set to possible actions where row col is EMPTY
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    #  Assign action to given board state
    (x, y) = action
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError

    # Deep copy board to a new board
    new_board = copy.deepcopy(board)
    new_board[x][y] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    # accept board as input and return the winner if there is one
    if helper.check_rows(board, x_player) or helper.check_columns(board, x_player) or helper.check_top_to_bottom_diagonal(board, x_player) or helper.check_bottom_to_top_diagonal(board, x_player):
        return x_player
    elif helper.check_rows(board, o_player) or helper.check_columns(board, o_player) or helper.check_top_to_bottom_diagonal(board, o_player) or helper.check_bottom_to_top_diagonal(board, o_player):
        return o_player
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) or helper.is_tie(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if winner(board) == x_player:
        return 1
    elif winner(board) == o_player:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    if terminal(board):
        return None
    elif player(board) == x_player:
        places = []
        for action in actions(board):
            places.append([min_value(result(board, action)), action])
        return sorted(places, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == o_player:
        places = []
        for action in actions(board):
            places.append([max_value(result(board, action)), action])
        return sorted(places, key=lambda x: x[0])[0][1]
