import numpy as np

from src.utils import *
import src.algorithms.minmax
from src.games.tic_tac_toe import TicTacToe

# Test imports
import tests.test_tic_tac_toe


def get_better_move(game):
    posible_moves = game.all_posibles_moves()
    if is_empty(posible_moves):
        return None

    best_move = max([(minmax(game.move(move), True), move) for move in posible_moves], key=lambda item:item[0])[1]
    return best_move

def get_score(game):
    if (game.winner is None) or (game.winner == 'Draw'):
        return 0
    elif game.winner == 'X':
        return 1
    elif game.winner == 'O':
        return -1



def minmax(game, maximazing, depth=0):

    if game.is_finish is True:
        return get_score(game)

    if maximazing is True:
        score = NEG_INFINITY
        for posible_move in game.all_posibles_moves():
            next_game = game.move(posible_move)
            score = max(score, minmax(next_game, False))

    else:
        score = INFINITY
        for posible_move in game.all_posibles_moves():
            next_game = game.move(posible_move)
            score = min(score, minmax(next_game, True))

    return score

def player_human(game):
    game.print_board()
    x = int(input("\nX: "))
    y = int(input("Y: "))
    print("")
    return (x, y)

def player_ia(game):
    return get_better_move(game)

if __name__ == '__main__':
    ttt = TicTacToe()

    ttt.make_move((1, 1))
    ttt.make_move((2, 2))
    ttt.make_move((0, 1))
    ttt.make_move((2, 1))
    ttt.make_move((2, 0))
    # ---
    #ttt.make_move((0, 2))
    #ttt.make_move((0, 0))

    #print(get_better_move(ttt))

    #ttt.play(player_human, player_ia)
