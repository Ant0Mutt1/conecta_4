import unittest
import numpy as np
from evaluation import check_four_connected, evaluate
from constants import HUMAN, BOT

class TestEvaluation(unittest.TestCase):

    def test_check_four_connected(self):
        # Crear un tablero vacío
        board = np.zeros((6, 7))

        # Añadir una conexión horizontal de 4 para el BOT
        board[5][0:4] = BOT
        self.assertTrue(check_four_connected(board, BOT))

        # Añadir una conexión vertical de 4 para el HUMAN
        board = np.zeros((6, 7))
        board[2:6, 0] = HUMAN
        self.assertTrue(check_four_connected(board, HUMAN))

        # Añadir una conexión diagonal (positiva)
        board = np.zeros((6, 7))
        for i in range(4):
            board[5 - i][i] = BOT
        self.assertTrue(check_four_connected(board, BOT))

        # Añadir una conexión diagonal (negativa)
        board = np.zeros((6, 7))
        for i in range(4):
            board[i][i] = HUMAN
        self.assertTrue(check_four_connected(board, HUMAN))

    def test_evaluate(self):
        # Crear un tablero vacío
        board = np.zeros((6, 7))

        # Añadir 3 fichas para el BOT
        board[5][0:3] = BOT
        score = evaluate(board)
        self.assertTrue(score > 0)

        # Añadir 3 fichas para el HUMAN
        board[5][0:3] = HUMAN
        score = evaluate(board)
        self.assertTrue(score < 0)

if __name__ == '__main__':
    unittest.main()
