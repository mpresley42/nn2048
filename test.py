import unittest
from game import Game
import numpy as np


class TestBoardSetup(unittest.TestCase):
    # def test_game_init(self):
    #     game = Game()
    #     print(game)

    def test_add_tile(self):
        game = Game()
        game.add_tile()
        self.assertTrue(np.count_nonzero(game.board) == 1)
        score = np.sum(game.board)
        self.assertTrue(score == 2 or score == 4)

    def test_game_over(self):
        game = Game()
        self.assertFalse(game.is_game_over())
        game.add_tile()
        self.assertFalse(game.is_game_over())
        game.board = 2 * np.ones_like(game.board)
        self.assertFalse(game.is_game_over())

        b1 = np.array([[2, 4, 2, 4],
                       [4, 2, 4, 2],
                       [2, 4, 2, 4],
                       [4, 2, 4, 2]])
        game.board = b1
        self.assertTrue(game.is_game_over())

    def test_slide_arr(self):
        game = Game()
        a1 = np.array([2,2,0,0])
        a2 = np.array([4,0,0,0])
        a1s, a1sc = game.slide_arr(a1)
        self.assertTrue(np.array_equal(a1s, a2))
        self.assertTrue(a1sc==4)

        a1 = np.array([2,2,2,2])
        a2 = np.array([4,4,0,0])
        a1s, a1sc = game.slide_arr(a1)
        self.assertTrue(np.array_equal(a1s, a2))

        a1 = np.array([4, 2, 2, 0])
        a2 = np.array([4, 4, 0, 0])
        a1s, a1sc = game.slide_arr(a1)
        self.assertTrue(np.array_equal(a1s, a2))

        a1 = np.array([0, 0, 2, 0])
        a2 = np.array([2, 0, 0, 0])
        a1s, a1sc = game.slide_arr(a1)
        self.assertTrue(np.array_equal(a1s, a2))

    def test_slide_board(self):
        game = Game()

        b1 = np.array([[2, 2, 0, 4],
                       [2, 0, 0, 0],
                       [2, 0, 4, 0],
                       [0, 0, 0, 2]])
        b2 = np.array([[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [2, 0, 0, 4],
                       [4, 2, 4, 2]])

        game.board = np.copy(b1)
        new_board, add_score = game.slide_board(game.board,'down')
        self.assertTrue(np.array_equal(new_board, b2))

        b3 = np.array([[4, 4, 0, 0],
                       [2, 0, 0, 0],
                       [2, 4, 0, 0],
                       [2, 0, 0, 0]])

        game.board = np.copy(b1)
        new_board, add_score = game.slide_board(game.board,'left')
        self.assertTrue(np.array_equal(new_board, b3))

        b4 = np.array([[0, 0, 0, 0],
                       [2, 0, 0, 0],
                       [4, 0, 2, 2],
                       [2, 32, 128, 512]])
        b5 = np.array([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [0, 0, 4, 4],
                       [2, 32, 128, 512]])

        game.board = np.copy(b4)
        new_board, add_score = game.slide_board(game.board,'right')
        self.assertTrue(np.array_equal(new_board, b5))

        b6 = np.array([[4, 2, 4, 4],
                       [2, 0, 0, 2],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]])
        game.board = np.copy(b1)
        new_board, add_score = game.slide_board(game.board,'up')
        self.assertTrue(np.array_equal(new_board, b6))


if __name__ == '__main__':
    unittest.main()
