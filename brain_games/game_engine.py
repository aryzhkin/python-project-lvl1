"""Основной движок, содержащий общую логику для игр."""
import prompt


ROUNDS_COUNT = 3  # кол-во раундов для игрока


def play_game(game):
    """Launches the selected game
    """

    print('Welcome to the Brain Games!')
    print(game.GAME_DESCRIPTION)

    user_name = ask('May I have your name? ')
    print('Hello, ' + user_name + '!\n')

    i = 0
    while i < ROUNDS_COUNT:

        (question, correct_answer) = game.generate_question_and_answer()

        print('Question: ' + question)
        user_answer = ask('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print("'" + str(user_answer) + "' is wrong answer ;(. "
                  "Correct answer was '" + str(correct_answer) + "'.\n"
                  "Let's try again, " + str(user_name) + "!")
            return

    print('Congratulations, ' + user_name + '!')


def ask(question):
    return prompt.string(question)
