import unittest
import numpy as np
from minimax import minimax, best_move
from constants import HUMAN, BOT, EMPTY

class TestBestMove(unittest.TestCase):

    def test_best_move_vertical_win(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0]
        ])

        _, new_state = best_move(board)

        expected_state = board.copy()
        expected_state[2][3] = BOT

        self.assertEqual(new_state.tolist(), expected_state.tolist())

    def test_best_move_horizontal_win(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0]
        ])

        _, new_state = best_move(board)

        expected_state = board.copy()
        expected_state[5][3] = BOT

        self.assertEqual(new_state.tolist(), expected_state.tolist())

    def test_block_opponent_win(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0]
        ])

        _, new_state = best_move(board)

        expected_state = board.copy()
        expected_state[5][3] = BOT

        self.assertEqual(new_state.tolist(), expected_state.tolist())

    def test_best_move_diagonal_win(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 2, 1, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [2, 1, 1, 2, 0, 0, 0]
        ])

        _, new_state = best_move(board)

        expected_state = board.copy()
        expected_state[2][3] = BOT

        self.assertEqual(new_state.tolist(), expected_state.tolist())

    def test_block_diagonal_opponent(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [1, 1, 2, 1, 0, 0, 0]
        ])

        _, new_state = best_move(board)

        expected_state = board.copy()
        expected_state[2][3] = BOT

        self.assertEqual(new_state.tolist(), expected_state.tolist())

if __name__ == '__main__':
    unittest.main()

