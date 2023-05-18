import numpy as np
from icecream import ic
from src.games.game import Game





class TicTacToe(Game):

    def __init__(self):
        # Execute the upper class __init__
        self._name = "Tic Tac Toe"
        self._player1 = 'O'
        self._player2 = 'X'
        self._empty = ''
        self._board = [[self._empty, self._empty, self._empty],
                        [self._empty, self._empty, self._empty],
                        [self._empty, self._empty, self._empty]]
        self._is_finish = False
        self._turn = 'O'
        self._winner = None

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

    def in_range(self, val):
        return val >= 0 and val < 3

    def next_player(self):
        if self._turn == 'O':
            return 'X'
        return 'O'

    def make_move(self, move):
        x, y = move
        if self._is_finish:
            raise Exception("Error. Can't play a finished game.")

        if not (self.in_range(x) and self.in_range(y)):
            raise Exception("Error. Invalid coodinated to play.")

        if self._board[y][x] != self._empty:
            raise Exception("Error. Can't play where someone already played.")

        self._board[y][x] = self._turn
        self._turn = self.next_player()

        return self.check_if_ended()

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
            elif X_win:
                self._winner = 'X'
            else:
                self._winner = 'Draw'

        return end_game


    # The board shold be a 2D-numpy array
    def check_if_player_won(self, board, player_str):
        res = False

        # Check if some row is all equal
        for r in board:
            res = res or self.all_equal_to(r, player_str)

        # Check if some column is all equal
        for c in board.T:
            res = res or self.all_equal_to(c, player_str)

        # Check if some diagonal is all equal
        res = res or self.all_equal_to(board.diagonal(), player_str) or \
                     self.all_equal_to(np.fliplr(board).diagonal(), player_str)

        ### We need o check if the board is full

        return res


    def all_equal_to(self, arr, val):
        for elem in arr:
            if elem != val:
                return False
        return True

    def all_posibles_moves(self):
        res = Set()
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == '':
                    res.add((i, j))

        return res
