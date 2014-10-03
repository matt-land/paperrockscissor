import random
__author__ = 'blitzcat'

PAPER = 'paper'
ROCK = 'rock'
SCISSOR = 'scissor'

PLAYER1 = 'player1'
PLAYER2 = 'player2'
TIE = 'tie'

CHOICES = [ PAPER, ROCK, SCISSOR ]

def get_random_choice():
    return random.choice(CHOICES)

def challenge(player1, player2):
    """
    :param player1: string
    :param player2: string
    :return:
    """
    # if player1 is not ROCK:
    #     print (type(ROCK))
    #     print (type(player1))
    #     exit(player1 + ' is not ' + ROCK)
    if not (player1 == PAPER or player1 == ROCK or player1 == SCISSOR):
        raise Exception('invalid input ' + PLAYER1)
    if not (player2 == PAPER or player2 == ROCK or player2 == SCISSOR):
         raise Exception('invalid input ' + PLAYER2)
    if player1 is PAPER:
        if player2 is PAPER:
            return TIE
        elif player2 is ROCK:
            return PLAYER1
        else:
            return PLAYER2
    elif player1 is ROCK:
        if player2 is PAPER:
            return PLAYER2
        elif player2 is ROCK:
            return TIE
        else:
            return PLAYER1
    else:
        if player2 is PAPER:
            return PLAYER1
        elif player2 is ROCK:
            return PLAYER2
        else:
            return TIE