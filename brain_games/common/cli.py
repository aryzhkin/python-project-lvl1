"""Command line interface for brain-games."""
import prompt


def welcome_user():
    """Get an user name and promt user."""
    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!\n')
    return name


def ask_answer():
    return prompt.string('Your answer: ')
