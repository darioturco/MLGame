import numpy as np

import src.algorithms.minmax
from src.games.tic_tac_toe import TicTacToe
from src.games.four_in_line import FourInLine
from src.algorithms.minmax import Minmax
from src.algorithms.q_learning import QLearning

def get_score(game):
    if (game.winner is None) or (game.winner == 'Draw'):
        return 0
    elif game.winner == 'X':
        return 1
    elif game.winner == 'O':
        return -1









def tic_tac_toe_test():
    import tests.test_tic_tac_toe
    ttt = TicTacToe()
    algorithm = Minmax(ttt, get_score)
    #algorithm = QLearning(ttt, get_score, 0.95, 0.25, 0.1)
    #algorithm.train()

    def player_human(game):
        game.print_board()
        x = int(input("\nX: "))
        y = int(input("Y: "))
        print("")
        return (x, y)

    def player_ia(game):
        return algorithm.get_better_move()

    ttt.make_move((1, 1))
    ttt.make_move((2, 2))
    ttt.make_move((0, 1))
    ttt.make_move((2, 1))
    ttt.make_move((2, 0))
    # ---
    ttt.make_move((0, 2))
    ttt.make_move((0, 0))
    ttt.print_board()
    print(ttt.turn)

    print(algorithm.get_better_move())

    #ttt.play(player_human, player_ia)

def four_in_line_test():
    import tests.four_in_line

    def player_human(game):
        game.print_board()
        x = int(input("\nX: "))
        print("")
        return (x, )

    def player_ia(game):
        m = algorithm.get_better_move()
        print(m)
        return m

    fil = FourInLine(4, 4)
    algorithm = Minmax(fil, get_score)


    fil.make_move((0, ))
    fil.make_move((0, ))
    #fil.make_move((1, ))
    #fil.make_move((2, ))
    #fil.make_move((2, ))
    #fil.make_move((3, ))
    #fil.make_move((0, ))



    #fil.print_board()
    #print(fil.turn)

    #print(algorithm.get_better_move())

    fil.play(player_human, player_ia)


    return False



if __name__ == '__main__':
    #tic_tac_toe_test()
    four_in_line_test()
