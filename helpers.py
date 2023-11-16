x_player = "X"
o_player = "O"
EMPTY = None


def check_rows(board, player):
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False


def check_columns(board, player):
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][col] == player:
                count += 1
        if count == len(board):
            return True
    return False


def check_top_to_bottom_diagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row == col and board[row][col] == player:
                count += 1
    return count == len(board[0])


def check_bottom_to_top_diagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    return count == len(board[0])


def is_tie(board):
    count_empty = (len(board) * len(board[0]))
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                count_empty -= 1
    return count_empty == 0
