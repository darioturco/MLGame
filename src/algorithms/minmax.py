from src.utils import *

class Minmax(object):
    def __init__(self, game, score_function):
        self.game = game
        self.score_function = score_function

    def get_better_move(self):
        posible_moves = self.game.all_posibles_moves()
        if is_empty(posible_moves):
            return None

        best_move = max([(self.minmax(self.game.move(move), True), move) for move in posible_moves], key=lambda item:item[0])[1]
        return best_move

    def minmax(self, game, maximazing, depth=0):
        if game.is_finish is True:
            return self.score_function(game)

        if maximazing is True:
            score = NEG_INFINITY
            for posible_move in game.all_posibles_moves():
                next_game = game.move(posible_move)
                score = max(score, self.minmax(next_game, False))

        else:
            score = INFINITY
            for posible_move in game.all_posibles_moves():
                next_game = game.move(posible_move)
                score = min(score, self.minmax(next_game, True))

        return score
