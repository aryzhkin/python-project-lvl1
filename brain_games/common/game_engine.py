from brain_games.common import cli


ROUND_COUNT = 3


def play_game(game):

    print('(new)Welcome to the Brain Games!')
    print(game.DESCRIPTION)

    user_name = cli.welcome_user()
    i = 0
    while i < ROUND_COUNT:

        (question, correct_answer) = game.generate_question_and_answer()

        print('Question: ' + question)
        answer = cli.ask_answer()

        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(answer)
            print("'" + str(answer) + "' is wrong answer ;(. "
                  "Correct answer was '" + str(correct_answer) + "'.\n"
                  "Let's try again, " + str(user_name) + "!")

    print('Congratulations, ' + user_name + '!')
