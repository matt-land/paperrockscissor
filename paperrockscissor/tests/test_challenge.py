__author__ = 'blitzcat'
from unittest import TestCase

import paperrockscissor


class TestChallenge(TestCase):
    def test_challenge_test(self):
        val = paperrockscissor.challenge(paperrockscissor.ROCK, paperrockscissor.ROCK)
        self.assertEqual(paperrockscissor.TIE, val)

    def test_player1_wins(self):
        val = paperrockscissor.challenge(paperrockscissor.ROCK, paperrockscissor.SCISSOR)
        self.assertEqual(paperrockscissor.PLAYER1, val)

    def test_player2_wins(self):
        val = paperrockscissor.challenge(paperrockscissor.PAPER, paperrockscissor.SCISSOR)
        self.assertEqual(paperrockscissor.PLAYER2, val)

    def test_guardians(self):
        try:
            paperrockscissor.challenge('banana', paperrockscissor.ROCK)
            self.fail('exception should have been raised, ' + paperrockscissor.PLAYER1)
        except Exception:
            var = 2
        try:
            paperrockscissor.challenge(paperrockscissor.ROCK, 'biscuit')
            self.fail('exception should have been raised, ' + paperrockscissor.PLAYER2)
        except Exception:
            var = 2
