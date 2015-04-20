# tictac.py
# Main engine to simulate tictactoe

# For the board, (0, 0) is at the top left.
# So, the bottom right would be (3, 3)
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
    if type(coor) is not iter:
        PlotException('The coordinate given is not a tuple')
        
    if type(playerid) is not str:
        PlotException('The player given is not a string')

    x, y = coor

    board[x][y] = playerid
    return board

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
