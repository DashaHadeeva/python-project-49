#!/usr/bin/env python3
from random import randint


def is_even(number):
    return number % 2 == 0


def brain_even():
    number = randint(1, 100)
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = f'Question: {number}'
    unswer = is_even(number)
    if unswer:
        result = 'yes'
        return result, task, question
    else:
        result = 'no'
        return result, task, question