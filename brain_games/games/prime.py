from random import randint
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_not_prime(number):
    i = 1
    if number == 2:
        return number != 2
    while i < sqrt(number):
        i += 1
        if number % i == 0:
            return number % i == 0
    return number % i == 0


def get_game():
    number = randint(1, 1000)
    question = f'{number}'
    answer = is_not_prime(number)
    if answer:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    return question, right_answer
