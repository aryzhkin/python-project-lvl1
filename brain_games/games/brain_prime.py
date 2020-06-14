import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    division_num = 2

    while num % division_num != 0:
        division_num += 1

    return division_num == num


def generate_question_and_answer():

    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'

    question = str(question)

    return question, correct_answer
