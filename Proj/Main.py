import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    #Instance BowlingGame Class as Game.
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 1):
            self.game.rolls[i]
        assert self.game.score()==0

    def testAllOnes(self):
        self.rollMany(20, 1)
        assert self.game.score()==20

    def testOneSpare(self):
        self.game.rolls[5]
        self.game.rolls[5]
        self.game.rolls[3]
        self.rollMany(16, 1)
        assert self.game.score()==16

    def testOneStrike(self):
        self.game.rolls[10]
        self.game.rolls[4]
        self.game.rolls[3]
        self.rollMany(16, 1)
        assert  self.game.score()==24

    def testPerfectGame(self):
        self.rollMany(12, 10)
        assert self.game.score()==300

    def testOneSpare(self):
        self.rollMany(21, 5)
        assert self.game.score()==150

    def rollMany(self, pins,rolls):
        for i in range(rolls):
            #self.game.rolls[i]
            self.game.rolls[pins]




































