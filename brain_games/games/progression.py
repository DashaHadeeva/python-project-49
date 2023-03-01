from random import randint


def brain_progression():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = list(range(start, start + step * length, step))
    position = randint(0, len(progression) - 1)
    result = str(progression[position])
    progression[position] = '..'
    collect = ' '.join(map(str, progression))
    question = f'Question: {collect}'
    task = 'What number is missing in the progression?'
    return result, task, question
