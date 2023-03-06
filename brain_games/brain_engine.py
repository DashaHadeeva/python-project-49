import prompt


ROUNDS = 3


def get_welcome(game_rule):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rule)
    return name


def get_question(question):
    print(f'Question: {question}')
    ans = prompt.string('Your answer: ')
    return ans


def get_start_game(game):
    game_rule = game.GAME_RULE
    name = get_welcome(game_rule)
    for _ in range(ROUNDS):
        question, right_answer = game.get_game()
        user_answer = get_question(question)
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
