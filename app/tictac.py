# tictac.py
# Main engine to simulate tictactoe

# For the board, (0, 0) is at the top left.
# So, the bottom right would be (3, 3)
import os

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


class PlotException(Exception):
    """Custom Exception for the tictactoe board"""
    pass


# Functions used to draw on the board
def plot(coor, playerid):
    """Plots a playerid to a coordinate (in a tuple)"""
    if not hasattr(coor, '__iter__'):
        raise PlotException('The coordinate given is not an iterable.')

    if playerid is str:
        raise PlotException('The coordinate cannot be a string.')

    if type(playerid) is not str:
        raise PlotException('The player given is not a string.')

    playerid = playerid.upper()

    if playerid is not 'X' or playerid is not 'O':
        raise PlotException('Invalid Input')

    x, y = coor

    board[x][y] = playerid
    return board


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pretty_print_board():
    """Prints a pretty version of the board"""
    space_list = [' ', ' ', ' ']
    print_out = '   %s   |   %s   |   %s   '

    for char in board:
        print print_out % (space_list[0], space_list[1], space_list[2])
        print print_out % (char[0], char[1], char[2])
        print print_out % (space_list[0], space_list[1], space_list[2])
        if char is not board[2]:
            print "-" * 23

def check_correct_mark(previnput, nextinput):
    if nextinput is not 'X' or nextinput is not 'O':
        raise PlotException('The input was not an X or O.')
    if previnput is None:
        return True
    if previnput is nextinput:
        return False
    return True

# Functions that determine if you won
def win_row(playerid):
    """Determines if a player won with a row"""
    if board[0][0] is playerid and board[0][1] is playerid and board[0][2] is playerid:
        return (True, "Row 1")

    if board[1][0] is playerid and board[1][1] is playerid and board[1][2] is playerid:
        return (True, "Row 2")

    if board[2][0] is playerid and board[2][1] is playerid and board[2][2] is playerid:
        return (True, "Row 3")

    return None

    
def win_column(playerid):
    """Determines if a player won with a column"""

    if board[0][0] is playerid and board[1][0] is playerid and board[2][0] is playerid:
        return (True, "Column 1")

    if board[0][1] is playerid and board[1][1] is playerid and board[2][1] is playerid:
        return (True, "Column 2")

    if board[0][2] is playerid and board[1][2] is playerid and board[2][2] is playerid:
        return (True, "Column 3")

    return None

def win_diagonal(playerid):
    """Determines if a player won with a diagonal"""
    if board[0][0] is playerid and board[1][1] is playerid and board[2][2] is playerid:
        return (True, "Diagonal Left-up to Right-down")

    if board[0][2] is playerid and board[1][1] is playerid and board[2][0] is playerid:
        return (True, "Diagonal Right-up to Left-down")

    return None

def reset_board():
    global board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ]
    return board
