#!/usr/bin/env python3

from random import randint
from random import choice
import operator


def brain_calc():
    number1 = randint(10, 100)
    number2 = randint(1, 10)
    operator_str = ['+', '-', '*']
    operator_rand = choice(operator_str)
    task = 'What is the result of the expression?'
    question = f'Question: {number1} {operator_rand} {number2}'
    if operator_rand == '+':
        result = str(operator.add(number1, number2))
    elif operator_rand == '-':
        result = str(operator.sub(number1, number2))
    else:
        result = str(operator.mul(number1, number2))
    return result, task, question
