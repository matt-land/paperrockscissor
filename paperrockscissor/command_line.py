#!/usr/bin/env python3
__author__ = 'blitzcat'

import paperrockscissor

player2val = paperrockscissor.get_random_choice()
player1val = input('choose ' + paperrockscissor.PAPER + ', ' + paperrockscissor.ROCK + ', or ' + paperrockscissor.SCISSOR + ': ')
print(paperrockscissor.PLAYER2 + " choose " + player2val)
print(paperrockscissor.PLAYER1 + ' choose ' + player1val)
val = paperrockscissor.challenge(player1val, player2val)
print('winner: ' + val)