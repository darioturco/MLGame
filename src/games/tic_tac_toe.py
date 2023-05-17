import numpy as np
from icecream import ic
from src.games.game import Game





class TicTacToe(Game):

  def __init__(self):
    # Execute the upper class __init__
    self.name = "Tic Tac Toe"
    self._board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self._is_finish = False
    self._turn = 'O'

  def print_board(self):
    for row in self._board:
      print(row)

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
    return self.turn

  def make_move(self, x, y):

    if self._turn == 'O':
      turn = 'X'
    elif self._turn == 'X':
      turn = 'O'
    else:
      raise Exeption("Error turn value.")

  def check_if_ended(self):
    board = np.arry(self._board)

    

  def all_equal_to(self, arr):
    np.all(arr == 0)
