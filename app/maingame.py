# Main Game for tictactoe.
# Wrapper method for the engine: takes engine and allows
# playing the game
import tictac as tt


def default():
    win = False
    previnput = None
    while not win:
        mark = player1_turn(previnput)
        previnput = mark
        win = check_win(mark)
        if win:
            print "Player 1 has won!"
            print "Won by: %s" % (win[1])
        mark = player2_turn(previnput)
        previnput = mark
        win = check_win(mark)
        if win:
            print "Player 2 has won!"
            print "Won by: %s" % (win[1])

def player1_turn(prev):
    pass

def player2_turn(prev):
    pass

def check_win(mark):
    pass
