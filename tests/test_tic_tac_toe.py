from tests.test import Tests
import numpy as np
from src.games.tic_tac_toe import TicTacToe

class GeneralTests(Tests):

    def test_new_board_is_full_of_zeros(self):
        ttt = TicTacToe()
        board = ttt.board
        self.assert_true(np.array_equal(board, [['', '', ''], ['', '', ''], ['', '', '']]), f"Wrong init board: {board}", "Succeful Test 1")

    def test_new_game_is_not_finish(self):
        ttt = TicTacToe()
        self.assert_false(ttt.is_finish, f"Error, the game is finished", "Succeful Test 2")

    def test_new_game_strat_with_O(self):
        ttt = TicTacToe()
        self.assert_true(ttt.turn == 'O', f"Error, is not the turn of O", "Succeful Test 3")

    def test_new_game_strat_with_O(self):
        ttt = TicTacToe()
        self.assert_true(ttt.turn == 'O', f"Error, is not the turn of O", "Succeful Test 3")

    def test_all_equal_true(self):
        ttt = TicTacToe()
        arr = np.array(['O', 'O', 'O'])
        self.assert_true(ttt.all_equal_to(arr, 'O'), f"Error", "Succeful Test 4")

    def test_all_equal_false(self):
        ttt = TicTacToe()
        arr = np.array(['O', '', 'O'])
        self.assert_false(ttt.all_equal_to(arr, 'O'), f"Error", "Succeful Test 5")

    def test_no_winner_in_empty_board(self):
        ttt = TicTacToe()
        board = np.array([['', '', ''], ['', '', ''], ['', '', '']])
        self.assert_false(ttt.check_if_player_won(board, 'O'), f"Error", "Succeful Test 6")

    def test_O_winner_by_row(self):
        ttt = TicTacToe()
        board = np.array([['O', 'O', 'O'], ['X', '', 'X'], ['', '', '']])
        self.assert_true(ttt.check_if_player_won(board, 'O'), f"Error", "Succeful Test 7")

    def test_X_winner_by_row(self):
        ttt = TicTacToe()
        board = np.array([['O', '', 'O'], ['X', 'X', 'X'], ['', '', '']])
        self.assert_true(ttt.check_if_player_won(board, 'X'), f"Error", "Succeful Test 8")

    def test_winner_by_column(self):
        ttt = TicTacToe()
        board = np.array([['O', '', 'O'], ['X', 'X', 'O'], ['', '', 'O']])
        self.assert_true(ttt.check_if_player_won(board, 'O'), f"Error", "Succeful Test 9")

    def test_winner_by_main_diagonal(self):
        ttt = TicTacToe()
        board = np.array([['O', '', 'O'], ['X', 'O', ''], ['', '', 'O']])
        self.assert_true(ttt.check_if_player_won(board, 'O'), f"Error", "Succeful Test 10")

    def test_winner_by_oposite_diagonal(self):
        ttt = TicTacToe()
        board = np.array([['O', '', 'O'], ['X', 'O', ''], ['O', '', 'X']])
        self.assert_true(ttt.check_if_player_won(board, 'O'), f"Error", "Succeful Test 11")

    def test_before_wining_the_game_is_finish(self):
        ttt = TicTacToe()
        ttt.board = [['O', '', 'O'], ['X', 'O', ''], ['O', '', 'X']]
        ttt.check_if_ended()
        self.assert_true(ttt.is_finish, f"Error", "Succeful Test 12")

    def test_before_one_move_board_is_correct(self):
        ttt = TicTacToe()
        ttt.make_move((1, 1))
        self.assert_true(np.array_equal(ttt.board, [['', '', ''], ['', 'O', ''], ['', '', '']]), f"Error", "Succeful Test 13")

    def test_before_two_move_board_is_correct(self):
        ttt = TicTacToe()
        ttt.make_move((0, 0))
        ttt.make_move((1, 1))
        self.assert_true(np.array_equal(ttt.board, [['O', '', ''], ['', 'X', ''], ['', '', '']]), f"Error: {ttt.board}", "Succeful Test 14")

    def test_before_tree_move_board_is_correct(self):
        ttt = TicTacToe()
        ttt.make_move((0, 0))
        ttt.make_move((1, 1))
        ttt.make_move((2, 1))
        self.assert_true(np.array_equal(ttt.board, [['O', '', ''], ['', 'X', 'O'], ['', '', '']]), f"Error: {ttt.board}", "Succeful Test 15")

    def test_before_multiple_moves_board_is_correct(self):
        ttt = TicTacToe()
        ttt.make_move((0, 0))
        ttt.make_move((1, 0))
        ttt.make_move((2, 0))
        ttt.make_move((0, 1))
        ttt.make_move((1, 2))
        ttt.make_move((1, 1))
        self.assert_true(np.array_equal(ttt.board, [['O', 'X', 'O'], ['X', 'X', ''], ['', 'O', '']]), f"Error: {ttt.board}", "Succeful Test 16")

    def test_O_can_win(self):
        ttt = TicTacToe()
        ttt.make_move((0, 0))
        ttt.make_move((1, 0))
        ttt.make_move((1, 1))
        ttt.make_move((0, 1))
        ttt.make_move((2, 2))
        self.assert_true(ttt.winner == 'O', f"Error: {ttt.board}", "Succeful Test 17")

    def test_X_can_win(self):
        ttt = TicTacToe()
        ttt.make_move((1, 0))
        ttt.make_move((0, 0))
        ttt.make_move((0, 1))
        ttt.make_move((1, 1))
        ttt.make_move((2, 1))
        ttt.make_move((2, 2))
        self.assert_true(ttt.winner == 'X', f"Error: {ttt.board}", "Succeful Test 18")

    def test_can_draw(self):
        ttt = TicTacToe()
        ttt.make_move((0, 0))
        ttt.make_move((1, 0))
        ttt.make_move((2, 0))
        ttt.make_move((0, 1))
        ttt.make_move((1, 2))
        ttt.make_move((1, 1))
        ttt.make_move((2, 1))
        ttt.make_move((2, 2))
        ttt.make_move((0, 2))
        self.assert_true(ttt.winner == 'Draw', f"Error: {ttt.board}", "Succeful Test 19")

GeneralTests().run_all_tests()
