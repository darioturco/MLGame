import copy
import numpy as np
from icecream import ic
from src.games.game import Game

class FourInLine(Game):
    def __init__(self, height, width):

        self._name = "Four In Line"
        self._player1 = 'O'
        self._player2 = 'X'
        self._empty = ' '
        self._height = height
        self._width = width
        self._board = [[self._empty for _ in range(width)] for _ in range(height)]
        self._is_finish = False
        self._turn = self._player1
        self._winner = None

    @classmethod
    def game_with_board_and_turn(cls, height, width, board, turn):
        new_game = cls(height, width)
        new_game._board = board
        new_game._turn = turn

        new_game.check_if_ended()

        return new_game

    def print_board(self):
        for row in self._board:
            print(row)

    @property
    def name(self):
        return self._name

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        ### Check if is a valid board and check the turn
        self._board = board

    @property
    def is_finish(self):
        return self._is_finish

    @property
    def turn(self):
        return self._turn

    @property
    def winner(self):
        return self._winner

    def in_range_width(self, val):
        return val >= 0 and val < self._width

    def in_range_height(self, val):
        return val >= 0 and val < self._height

    def next_player(self):
        if self._turn == 'O':
            return 'X'
        return 'O'

    def check_posible_move(self, x):
        if self._is_finish:
            raise Exception("Error. Can't play a finished game.")
        if not (self.in_range_width(x)):
            raise Exception("Error. Invalid coodinated to play.")
        if self._board[0][x] != self._empty:
            raise Exception("Error. Can't play in a full column.")
        return True

    def get_drop_row(self, x):
        for i in range(self._height):
            if self._board[self._height - 1 - i][x] == self._empty:
                return self._height - 1 - i

        return -1

    def make_move(self, move):
        x = move[0]
        self.check_posible_move(x)
        y = self.get_drop_row(x)

        self._board[y][x] = self._turn
        self._turn = self.next_player()

        return self.check_if_ended()

    # Is the same function of make_move but returning a copy
    def move(self, move):
        x = move[0]
        self.check_posible_move(x)
        y = self.get_drop_row(x)

        new_board = copy.deepcopy(self._board)
        new_board[y][x] = self._turn

        return self.__class__.game_with_board_and_turn(self._height, self._width,new_board, self.next_player())

    def is_board_full(self):
        for r in self._board:
            for e in r:
                if e == self._empty:
                    return False
        return True

    def check_if_ended(self):
        board = np.array(self._board)
        res = False

        # Check if the player "O" won
        O_won = self.check_if_player_won(board, 'O')

        # Check if the player "X" won
        X_won = self.check_if_player_won(board, 'X')

        # Check if there is a free spot in the board
        is_full = self.is_board_full()

        end_game = O_won or X_won or is_full
        if end_game:
            self._is_finish = True
            if O_won:
                self._winner = 'O'
            elif X_won:
                self._winner = 'X'
            else:
                self._winner = 'Draw'

        return end_game


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

        res = set()
        if not self._is_finish:
            for c in range(self._width):
                if self._board[0][c] == self._empty:
                    res.add((c, ))

        return res

    def new_game(self):
        return self.__class__(self._height, self._width)

    def get_state(self):
        return tuple([elem for row in self._board for elem in row])

    def play(self, player1, player2):

        while not self._is_finish:
            if self._turn == 'O':
                move = player1(self)
            else:
                move = player2(self)

            self.make_move(move)

        print("\n\n----------------------")
        self.print_board()
        print("----------------------\n")
        print(f"The winner is: {self._winner}")
