import random
__author__ = 'matt-land'

PAPER = 'paper'
ROCK = 'rock'
SCISSOR = 'scissor'

PLAYER1 = 'player1'
PLAYER2 = 'player2'
TIE = 'tie'

CHOICES = [PAPER, ROCK, SCISSOR]


def get_random_choice():
    return random.choice(CHOICES)


def challenge(player1val, player2val):
    """
    :param player1val: string
    :param player2val: string
    :return:
    """
    # guardians, because return early...
    if player1val not in CHOICES:
        raise Exception('invalid input ' + PLAYER1)
    if player2val not in CHOICES:
        raise Exception('invalid input ' + PLAYER2)

    if player1val is player2val:
        return TIE

    if player1val is PAPER:
        if player2val is ROCK:
            return PLAYER1
        else:
            return PLAYER2
    elif player1val is ROCK:
        if player2val is PAPER:
            return PLAYER2
        else:
            return PLAYER1
    else:
        if player2val is PAPER:
            return PLAYER1
        elif player2val is ROCK:
            return PLAYER2
