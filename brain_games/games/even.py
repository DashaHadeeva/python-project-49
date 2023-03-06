from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0


def get_game():
    random_number = randint(1, 100)
    question = f'{random_number}'
    answer = is_even(random_number)
    if answer:
        right_answer = 'yes'
        return question, right_answer
    else:
        right_answer = 'no'
        return question, right_answer
