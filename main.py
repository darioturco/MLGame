import numpy as np

import src.algorithms.minmax
from src.games.tic_tac_toe import TicTacToe
from src.algorithms.minmax import Minmax
from src.algorithms.q_learning import QLearning

# Test imports
import tests.test_tic_tac_toe

def get_score(game):
    if (game.winner is None) or (game.winner == 'Draw'):
        return 0
    elif game.winner == 'X':
        return 1
    elif game.winner == 'O':
        return -1





def player_human(game):
    game.print_board()
    x = int(input("\nX: "))
    y = int(input("Y: "))
    print("")
    return (x, y)

if __name__ == '__main__':
    ttt = TicTacToe()
    #algorithm = Minmax(ttt, get_score)
    # BORRAR: def __init__(self, game, score_function, alpha, discount_factor, explore_rate):
    algorithm = QLearning(ttt, get_score, 0.95, 0.25, 0.1)
    algorithm.train()

    def player_ia(game):
        return algorithm.get_better_move()

    #ttt.make_move((1, 1))
    #ttt.make_move((2, 2))
    #ttt.make_move((0, 1))
    #ttt.make_move((2, 1))
    #ttt.make_move((2, 0))
    # ---
    #ttt.make_move((0, 2))
    #ttt.make_move((0, 0))

    #print(algorithm.get_better_move())

    ttt.play(player_human, player_ia)
