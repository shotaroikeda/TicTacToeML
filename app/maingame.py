# Main Game for tictactoe.
# Wrapper method for the engine: takes engine and allows
# playing the game
import tictac as tt


def default():
    win = False
    previnput = None
    previnput = player1_turn(previnput, True)
    previnput = player2_turn(previnput)

    while not win:
        mark = player1_turn(previnput)
        previnput = mark
        win = tt.check_win(mark)

        if win:
            print "Player 1 has won!"
            print "Won by: %s" % (win[1])

        mark = player2_turn(previnput)
        previnput = mark
        win = tt.check_win(mark)

        if win:
            print "Player 2 has won!"
            print "Won by: %s" % (win[1])

def player1_turn(prev, first=False):
    if first:
        while True:
            char = raw_input("Enter symbol to play as (X or O): ")
            char = char.upper()
            if char is not "X" or char is not "O":
                print "Bad symbol."
            else:
                break
                # Should tell them to enter coordinates afterwards
    else:
        return player2_turn(prev)

def player2_turn(prev):
    while True:
        char = raw_input(">>> ")

