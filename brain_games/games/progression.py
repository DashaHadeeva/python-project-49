from random import randint


GAME_RULE = 'What number is missing in the progression?'


def get_game():
    progression, length = get_progression()
    position = randint(0, length - 1)
    right_answer = str(progression[position])
    progression[position] = '..'
    collect = ' '.join(map(str, progression))
    question = f'{collect}'
    return question, right_answer


def get_progression():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = list(range(start, start + step * length, step))
    return progression, length
