Paper Rock Scissor
__________________

This is an exercise in making a python module, learning python and unit testing
The exercise can be found here:
https://github.com/sheilatron/shiny_code_quest

This will compare two inputs from the classic paper rock scissor game, and return "player1", "player2", or "tie" based on the combination passed.

Example usage:
______________
>>> import paperrockscissor

>>> paperrockscissor.challenge('paper', 'rock')


>>> paperrockscissor.challenge(paperrockscissor.PAPER, paperrockscissor.ROCK)


>>> paperrockscissor.challenge(paperrockscissor.get_random_choice(), paperrockscissor.get_random_choice())

