from random import randint
from math import sqrt


def is_not_prime(number):
    i = 1
    if number == 2:
        return number != 2
    while i < sqrt(number):
        i += 1
        if number % i == 0:
            return number % i == 0
    return number % i == 0


def brain_prime():
    number = randint(1, 1000)
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f'Question: {number}'
    answer = is_not_prime(number)
    if answer:
        result = 'no'
        return result, task, question
    else:
        result = 'yes'
        return result, task, question
