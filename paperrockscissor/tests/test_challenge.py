__author__ = 'matt-land'
from unittest import TestCase

import paperrockscissor


class TestChallenge(TestCase):
    def test_challenge_test(self):
        val = paperrockscissor.challenge(
            paperrockscissor.ROCK, paperrockscissor.ROCK)
        self.assertEqual(paperrockscissor.TIE, val)

    def test_player1_wins(self):
        val = paperrockscissor.challenge(
            paperrockscissor.ROCK, paperrockscissor.SCISSOR)
        self.assertEqual(paperrockscissor.PLAYER1, val)
        val = paperrockscissor.challenge(
            paperrockscissor.PAPER, paperrockscissor.ROCK)
        self.assertEqual(paperrockscissor.PLAYER1, val)
        val = paperrockscissor.challenge(
            paperrockscissor.SCISSOR, paperrockscissor.PAPER)
        self.assertEqual(paperrockscissor.PLAYER1, val)

    def test_player2_wins(self):
        val = paperrockscissor.challenge(
            paperrockscissor.PAPER, paperrockscissor.SCISSOR)
        self.assertEqual(paperrockscissor.PLAYER2, val)
        val = paperrockscissor.challenge(
            paperrockscissor.ROCK, paperrockscissor.PAPER)
        self.assertEqual(paperrockscissor.PLAYER2, val)
        val = paperrockscissor.challenge(
            paperrockscissor.SCISSOR, paperrockscissor.ROCK)
        self.assertEqual(paperrockscissor.PLAYER2, val)

    def test_guardians(self):
        try:
            paperrockscissor.challenge('banana', paperrockscissor.ROCK)
            self.fail('exception should have been raised, '
                      + paperrockscissor.PLAYER1)
        except Exception:
            var = 0
        try:
            paperrockscissor.challenge(paperrockscissor.ROCK, 'biscuit')
            self.fail('exception should have been raised, '
                      + paperrockscissor.PLAYER2)
        except Exception:
            var = 0

    def test_get_random_choice(self):
        val = paperrockscissor.get_random_choice()
        self.assertTrue(val in paperrockscissor.CHOICES)
