from tests.test import Tests
import numpy as np
from src.games.tic_tac_toe import TicTacToe

class GeneralTests(Tests):

  def test_positive_number(self):
    number = 532
    self.assert_true(number > 0, f"Number greater than 0 expected, got: {number}", "Succeful demo test.")

  def test_new_board_is_full_of_zeros(self):
    ttt = TicTacToe()
    board = ttt.board
    self.assert_true(np.allclose(board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), f"Wrong init board: {board}", "Succeful Test 1")

  def test_new_game_is_not_finish(self):
    ttt = TicTacToe()
    self.assert_false(ttt.is_finish, f"Error, the is finished", "Succeful Test 2")



GeneralTests().run_all_tests()
