from random import randint
from random import choice
import operator


GAME_RULE = 'What is the result of the expression?'
OPERATORS = {'+': lambda num1, num2: num1 + num2,
             '-': lambda num1, num2: num1 - num2,
             '*': lambda num1, num2: num1 * num2}


def get_game():
    num1 = randint(10, 100)
    num2 = randint(1, 10)
    operator_rand = choice([*OPERATORS])
    right_answer = OPERATORS[operator_rand](num1, num2)
    question = f'{num1} {operator_rand} {num2}'
    return question, right_answer
