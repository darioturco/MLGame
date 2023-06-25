import numpy as np
import random
from src.games.game import Game, MultiDiscrete

class TicTacToe(Game):
    def __init__(self, render_mode, reward_function=None):
        self.name = "Tic Tac Toe"
        self._render_mode = render_mode
        self._player1 = 1
        self._player2 = 2
        self._empty = 0

        if reward_function is None:
            reward_function = self.default_reward_function
        self._reward_function = reward_function

        self.observation_space = MultiDiscrete([[3, 3, 3],
                                                [3, 3, 3],
                                                [3, 3, 3]])
        self.action_space = MultiDiscrete([3, 3])

        self.reset()

    def reset(self):
        self._state = [[self._empty, self._empty, self._empty],
                        [self._empty, self._empty, self._empty],
                        [self._empty, self._empty, self._empty]]

        self._turn = self._player1

        self._is_finish = False
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
            x, y = action
            self._state[y][x] = self._player1
            done = self.check_if_ended()

            if not done:
                oponent_action_x, oponent_action_y = random.choice(self.all_posibles_moves())
                self._state[oponent_action_y][oponent_action_x] = self._player2

        self.check_if_ended()

        new_state = self._state
        reward = self._reward_function()
        done = self._is_finish
        trucated = False
        info = {}
        return new_state, reward, done, trucated, info

    # ---------------

    def default_reward_function(self):
        if (self.winner is None) or (self.winner == 'Draw'):
            return 0
        elif self.winner == self._player1:
            return 1
        elif self.winner == self._player2:
            return -1

    def all_posibles_moves(self):
        res = []
        if not self._is_finish:
            for y in range(3):
                for x in range(3):
                    if self._state[y][x] == self._empty:
                        res.append((x, y))

        return res

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

    def check_if_player_won(self, board, player_value):
        res = False

        # Check if some row is all equal
        for r in board:
            res = res or self.all_equal_to(r, player_value)

        # Check if some column is all equal
        for c in board.T:
            res = res or self.all_equal_to(c, player_value)

        # Check if some diagonal is all equal
        res = res or self.all_equal_to(board.diagonal(), player_value) or \
                     self.all_equal_to(np.fliplr(board).diagonal(), player_value)

        return res

    def all_equal_to(self, arr, val):
        for elem in arr:
            if elem != val:
                return False
        return True

    def is_posible_move(self, move):
        x, y = move

        ### It shold be a warning
        #if self._is_finish:
        #    raise Exception("Error. Can't play a finished game.")

        is_move_in_range = not (self.is_in_range(x) and self.is_in_range(y))
        is_empty = self._state[y][x] == self._empty

        if is_move_in_range or (not is_empty):
            self._is_finish = True
            self.winner = self._player2

        return self._is_finish

    def is_in_range(self, val):
        return val >= 0 and val < 3
