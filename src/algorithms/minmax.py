from src.utils import *

class Minmax(object):
    def __init__(self, game, score_function):
        self.game = game
        self.score_function = score_function

    def get_better_move(self, depth=100):
        posible_moves = self.game.all_posibles_moves()
        if is_empty(posible_moves):
            return None

        xs = [(self.minmax(self.game.move(move), False, depth-1), move) for move in posible_moves]
        best_move = max(xs, key=lambda item:item[0])[1]
        return best_move

    def minmax(self, game, maximazing, depth=0):

        #if(depth == 0):
            #print("Max depth reached")
            ### Lock what has to be done when the depth limit is reached
        #    return 0

        if game.is_finish is True:
            return self.score_function(game)

        if maximazing is True:
            score = NEG_INFINITY
            for posible_move in game.all_posibles_moves():
                next_game = game.move(posible_move)
                score = max(score, self.minmax(next_game, False, depth-1))

        else:
            score = INFINITY
            for posible_move in game.all_posibles_moves():
                next_game = game.move(posible_move)
                score = min(score, self.minmax(next_game, True, depth-1))

        return score
