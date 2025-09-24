import unittest
from casino import Game

class TestGame(unittest.TestCase):
    def test_new_round(self):
        game = Game(numPlayers=4)
        self.assertEqual(game.round, 1)

    def test_2_players(self):
        game = Game(numPlayers=2)
        self.assertEqual(game.deck.size(), 40)

    def test_3_players(self):
        game = Game(numPlayers=3)
        self.assertEqual(game.deck.size(), 36)

    def test_4_players(self):
        game = Game(numPlayers=4)
        self.assertEqual(game.deck.size(), 32)

    def test_5_players(self):
        with self.assertRaises(ValueError):
            game = Game(numPlayers=5)


if __name__ == "__main__":
    unittest.main()