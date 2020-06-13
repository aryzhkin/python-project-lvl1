from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    number = randint(1, 20)

    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer
