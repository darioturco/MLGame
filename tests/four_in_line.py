from tests.test import Tests
import numpy as np
from src.games.four_in_line import FourInLine

emp = ' '

class GeneralTests(Tests):

    def test_new_board_is_full_of_zeros(self):
        fil = FourInLine(6, 8)
        board = fil.board
        self.assert_true(np.array_equal(board, [[emp, emp, emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp, emp, emp]]), f"Wrong init board: {board}", "Succeful Test 1")

    def test_new_game_is_not_finish(self):
        fil = FourInLine(6, 8)
        self.assert_false(fil.is_finish, f"Error, the game is finished", "Succeful Test 2")

    def test_new_game_strat_with_O(self):
        fil = FourInLine(6, 8)
        self.assert_true(fil.turn == 'O', f"Error, is not the turn of O", "Succeful Test 3")

    def test_new_game_move_in_0_column(self):
        fil = FourInLine(6, 6)
        self.assert_true(fil.check_posible_move(0), f"Error", "Succeful Test 4")

    def test_first_move_is_correct(self):
        fil = FourInLine(6, 6)
        fil.make_move((1,))
        board = fil.board
        self.assert_true(np.array_equal(board, [[emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, 'O', emp, emp, emp, emp]]), f"Error", "Succeful Test 5")

    def test_second_move_is_correct(self):
        fil = FourInLine(6, 6)
        fil.make_move((1,))
        fil.make_move((0,))
        board = fil.board
        self.assert_true(np.array_equal(board, [[emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                ['X', 'O', emp, emp, emp, emp]]), f"Error", "Succeful Test 6")

    def test_third_move_is_correct(self):
        fil = FourInLine(6, 6)
        fil.make_move((1,))
        fil.make_move((0,))
        fil.make_move((0,))
        board = fil.board
        self.assert_true(np.array_equal(board, [[emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                [emp, emp, emp, emp, emp, emp],
                                                ['O', emp, emp, emp, emp, emp],
                                                ['X', 'O', emp, emp, emp, emp]]), f"Error", "Succeful Test 7")

    def test_player_X_not_win_in_empty_board(self):
        fil = FourInLine(6, 6)
        self.assert_false(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 8")

    def test_player_X_win_in_board_with_row_fill(self):
        fil = FourInLine(6, 6)
        fil.board = [[emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    ['X', 'X', 'X', 'X', 'X', 'X']]
        self.assert_true(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 9")


    def test_player_X_win_in_board_with_column_fill(self):
        fil = FourInLine(6, 6)
        fil.board = [['X', emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp]]
        self.assert_true(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 10")

    def test_player_X_win_in_board_with_up_diagonal(self):
        fil = FourInLine(6, 6)
        fil.board = [[emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, 'X', emp, emp],
                    [emp, emp, 'X', 'O', emp, emp],
                    [emp, 'X', 'O', 'O', emp, emp],
                    ['X', 'O', 'O', 'O', emp, emp]]
        self.assert_true(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 11")

    def test_player_X_win_in_board_with_down_diagonal(self):
        fil = FourInLine(6, 6)
        fil.board = [[emp, emp, emp, emp, emp, emp],
                    [emp, emp, emp, emp, emp, emp],
                    ['X', emp, emp, emp, emp, emp],
                    ['O', 'X', emp, emp, emp, emp],
                    ['O', 'X', 'X', emp, emp, emp],
                    ['X', 'O', 'O', 'X', 'X', emp]]
        self.assert_true(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 12")

    def test_player_X_not_win_in_semi_full_board(self):
        fil = FourInLine(4, 4)
        fil.board = [
                    ['O', 'X', 'O', emp],
                    ['X', 'O', 'O', 'X'],
                    ['O', 'O', 'O', 'X'],
                    ['O', 'X', 'X', 'X']]
        self.assert_false(fil.check_if_player_won(np.array(fil.board), 'X'), f"Error", "Succeful Test 13")

    def test_empty_board_is_not_finish(self):
        fil = FourInLine(6, 6)
        self.assert_false(fil.check_if_ended(), f"Error", "Succeful Test 14")

GeneralTests().run_all_tests()
