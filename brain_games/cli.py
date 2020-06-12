"""Command line interface for brain-games."""
# тут только ввод и вывод
import prompt
import random


def welcome_user():
    """Get an user name and promt user."""
    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!\n')


def give_question():
    rand_num = random.randint(1, 20)

    print('Question: ' + str(rand_num))

    answer = prompt.string('Your answer: ')

    if answer == 'yes' and rand_num % 2 == 0:
        return (answer, True)
    elif answer == 'no' and rand_num % 2 != 0:
        return (answer, True)
    else:
        return (answer, False)

