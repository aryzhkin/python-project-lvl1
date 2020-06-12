from brain_games import cli
ROUND_COUNT = 3


def start_game():

    print('Welcome to the Brain Games!\n'
          'Answer "yes" if number even otherwise answer "no".')

    cli.welcome_user()
    i = 0
    while i < ROUND_COUNT:

        (answer, result) = cli.give_question()

        if result is True:
            print('Correct!')
            i += 1
        else:
            correct_answer = 'yes' if answer == 'no' else 'no'
            print("'" + str(answer) + "' is wrong answer ;(. "
                  "Correct answer was '" + correct_answer + "'.\n"
                  "Let's try again, Bill!")

    print('Congratulations, Bill!')
