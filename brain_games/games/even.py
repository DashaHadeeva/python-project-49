from random import randint


def is_even(random_number):
    return random_number % 2 == 0


def brain_even():
    random_number = randint(1, 100)
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = f'Question: {random_number}'
    answer = is_even(random_number)
    if answer:
        result = 'yes'
        return result, task, question
    else:
        result = 'no'
        return result, task, question
