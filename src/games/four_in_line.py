import copy
import random
import numpy as np
from src.games.game import Game, Discrete, MultiDiscrete


class FourInLine(Game):
    def __init__(self, render_mode='human', reward_function=None, **kwargs):
        self.name = "Four In Line"
        self._render_mode = render_mode
        self._player1 = 1
        self._player2 = 2
        self._empty = 0
        self._height = kwargs['height']
        self._width = kwargs['width']

        if reward_function is None:
            reward_function = self.default_reward_function
        self._reward_function = reward_function

        self.observation_space = MultiDiscrete([ [ 3 for _ in range(self._height)] for _ in range(self._width)])
        self.action_space = Discrete(self._width)

        self.reset()

    def reset(self):
        self._state = [[self._empty for _ in range(self._width)] for _ in range(self._height)]
        self._is_finish = False
        self._turn = self._player1
        self.winner = None
        info = {}
        return self._state, info

    def close(self):
        pass

    def render(self):
        ### Should define it game
        for row in self._state:
            print(row)

    def step(self, action):
        done = self.is_posible_move(action)

        if not done:
            #x = action
            y = self.get_drop_row(action)
            self._state[y][action] = self._player1
            done = self.check_if_ended()

            if not done:
                oponent_action_x = random.choice(self.all_posibles_moves())
                oponent_action_y = self.get_drop_row(oponent_action_x)
                self._state[oponent_action_y][oponent_action_x] = self._player2

        self.check_if_ended()

        new_state = self._state
        reward = self._reward_function()
        done = self._is_finish
        trucated = False
        info = {}
        return new_state, reward, done, trucated, info

    # -------------

    def is_posible_move(self, move):

        ### It shold be a warning
        #if self._is_finish:
        #    raise Exception("Error. Can't play a finished game.")

        is_move_in_range = self.in_range_width(move)
        is_empty = self._state[0][move] == self._empty

        if (not is_move_in_range) or (not is_empty):
            self._is_finish = True
            self.winner = self._player2

        return self._is_finish

    def default_reward_function(self):
        if (self.winner is None) or (self.winner == 'Draw'):
            return 0
        elif self.winner == self._player1:
            return 1
        elif self.winner == self._player2:
            return -1



    def in_range_width(self, val):
        return val >= 0 and val < self._width

    def in_range_height(self, val):
        return val >= 0 and val < self._height


    def get_drop_row(self, x):
        for i in range(self._height):
            if self._state[self._height - 1 - i][x] == self._empty:
                return self._height - 1 - i

        return -1



    def is_board_full(self):
        for r in self._state:
            for e in r:
                if e == self._empty:
                    return False
        return True

    def check_if_ended(self):
        board = np.array(self._state)

        # Check if the player "O" won
        won_1 = self.check_if_player_won(board, self._player1)

        # Check if the player "X" won
        won_2 = self.check_if_player_won(board, self._player2)

        # Check if there is a free spot in the board
        is_full = self.is_board_full()

        end_game = won_1 or won_2 or is_full
        if end_game:
            self._is_finish = True
            if won_1:
                self.winner = self._player1
            elif won_2:
                self.winner = self._player2
            else:
                self.winner = 'Draw'

        return self._is_finish

    # The board shold be a 2D-numpy array
    def check_if_player_won(self, board, player_str):
        res = False

        # Check if some row is all equal
        for r in board:
            for i in range((self._width-4) + 1):
                res = res or self.all_equal_to(r[i:i+4], player_str)

        # Check if some column is all equal
        for c in board.T:
            for i in range((self._height-4) + 1):
                res = res or self.all_equal_to(c[i:i+4], player_str)

        # Check if some diagonal is all equal
        for i in range((self._height-4) + 1):
            for j in range((self._width-4) + 1):
                #print(board[i:].diagonal(j)[:4], i, j)
                res = res or self.all_equal_to(board[i:].diagonal(j)[:4], player_str) or \
                             self.all_equal_to(np.fliplr(board[i:]).diagonal(j)[:4], player_str)

        return res

    def all_equal_to(self, arr, val):
        for elem in arr:
            if elem != val:
                return False
        return True

    def all_posibles_moves(self):
        res = []
        if not self._is_finish:
            for c in range(self._width):
                if self._state[0][c] == self._empty:
                    res.append(c)

        return res
