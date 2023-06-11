import random
import numpy as np
from src.utils import *

# Based on https://github.com/greerviau/SnakeAI
class Generative_Neuronal_Network(object):
    def __init__(self, game):
        self.game = game

    def get_better_move(self):
        posible_moves = self.game.all_posibles_moves()
        if is_empty(posible_moves):
            return None

        return best_move

    def train_individual(self):
        game = self.game.new_game()
        #net_work

        #while not game.is_finish:
        #    move = self.get_better_move_train(game)
        #    next_game = game.move(move)
        #    next_score = self.score_function(next_game)
        #    self.q_learning(game, move, next_game, next_score)
        #    game = next_game

        return (neuronal_network, score)

    def train(self, generations=50, population_amount=2500, selection=100, mutation_rate=0.05):

        selection_amount = population_amount // selection
        next_gen = [random_network() for i in range(population_amount)]
        for generation in range(generations):


            population = [train_individual(g, selection_amount) for g in next_gen]
            population.sort(key=lambda item: item[1])

            next_gen = population[:selection_amount]
