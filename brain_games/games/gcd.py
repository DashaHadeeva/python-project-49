from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    number1 = randint(10, 99)
    number2 = randint(10, 99)
    question = (f'{number1} {number2}')
    right_answer = str(math.gcd(number1, number2))
    return question, right_answer
