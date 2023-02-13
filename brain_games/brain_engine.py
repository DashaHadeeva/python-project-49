import prompt


def brain_run(game_logic):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    res = game_logic()
    print(res[1])
    n = 3
    while n >= 1:
        n -= 1
        res = game_logic()
        print(res[2])
        ans = prompt.string('Your answer: ')
        if ans == res[0]:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{res[0]}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')