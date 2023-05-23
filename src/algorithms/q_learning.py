import random
import numpy as np
from src.utils import *

class QLearning(object):
    def __init__(self, game, score_function, alpha, discount_factor, explore_rate):
        self.Q = {}
        self.game = game
        self.score_function = score_function
        self.alpha = alpha
        self.discount_factor = discount_factor
        self.explore_rate = explore_rate

    def get_Q_value(self, state, move):
        if (state, move) not in self.Q:
            self.Q[(state, move)] = 0.0

        return self.Q[(state, move)]

    ### It should be two get_better_move functions, one for training proces (with emploration) and other for plaing
    def get_better_move_train(self, game):
        posible_moves = game.all_posibles_moves()
        if is_empty(posible_moves):
            return None

        if self.explore_rate > random.random(): # Explore
            # Usa a ramdom movement
            best_move = random.sample(posible_moves, 1)[0]
        else:   # Exploit
            state = game.get_state()
            Q_values = [(self.get_Q_value(state, move), move) for move in game.all_posibles_moves()]

            print(Q_values)
            best_Q_value = max(Q_values, key=lambda item:item[0])[0]
            best_moves = [move for (Q_value, move) in Q_values if are_equal(Q_value, best_Q_value)]
            best_move = random.choice(best_moves)

        return best_move

    def get_better_move(self):
        posible_moves = self.game.all_posibles_moves()
        if is_empty(posible_moves):
            return None

        state = self.game.get_state()
        Q_values = [(self.get_Q_value(state, move), move) for move in self.game.all_posibles_moves()]

        best_Q_value = max(Q_values, key=lambda item:item[0])[0]
        best_moves = [move for (Q_value, move) in Q_values if are_equal(Q_value, best_Q_value)]
        best_move = random.choice(best_moves)

        return best_move

    ### Create sintetic data and train
    def train(self, train_iterations=50000):

        for i in range(train_iterations):
            game = self.game.new_game()
            while not game.is_finish:
                move = self.get_better_move_train(game)
                next_game = game.move(move)
                next_score = self.score_function(next_game)
                self.q_learning(game, move, next_game, next_score)
                game = next_game

    def q_learning(self, game, move, next_game, next_score):
        state = game.get_state()
        next_state = next_game.get_state()
        next_Q_values = [self.get_Q_value(next_state, next_move) for next_move in next_game.all_posibles_moves()]
        max_next_Q = max(next_Q_values) if next_Q_values else 0.0
        self.Q[(state, move)] += self.alpha * (next_score + self.discount_factor * max_next_Q - self.Q[(state, move)])
