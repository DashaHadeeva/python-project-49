#!/usr/bin/env python3
from random import randint


def brain_progression():
    start = randint(1, 20)
    finish = randint(120, 150)
    step = randint(1, 10)
    position = randint(0, 9)
    progression = range(start, finish, step)
    list_progr = list(progression)
    result = str(progression[position])
    list_progr[position] = '..'
    collect = ''
    for i in list_progr(randint(5,10)):
        collect = collect + ' ' + str(i)
    question = f'Question: {collect}'
    task = 'What number is missing in the progression?'
    return result, task, question
