import unittest
import numpy as np
from minimax import minimax, best_move
from constants import HUMAN, BOT

class TestMinimax(unittest.TestCase):

    def test_best_move(self):
   
        board = np.zeros((6, 7))

        board[5][0:3] = HUMAN

        score, new_state = best_move(board)

        self.assertIsNotNone(new_state)
        self.assertNotEqual(board.tolist(), new_state.tolist())

    def test_best_win_move(self):
        board = np.zeros((6, 7))
        
        board[3:,2] = HUMAN
        board[3:,0] = BOT

        score, new_state = best_move(board)
        print(new_state)

        output_board = board.copy()
        output_board[2][0] = BOT

        self.assertEqual(best_move(board)[1].tolist(), output_board.tolist())


if __name__ == '__main__':
    unittest.main()

