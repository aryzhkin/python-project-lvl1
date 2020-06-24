"""
Игра "Простое ли число?".
Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""
import random

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. ' \
                   'Otherwise answer "no".'
RANDOM_FROM = 1
RANDOM_TO = 100


def is_prime(num):
    """Check if num is prime.
    Returns:
        true or false: boolean
    """
    division_num = 2

    if num <= 1:
        return False

    while num % division_num != 0 and division_num * division_num <= num:
        division_num += 1

    return division_num * division_num > num


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """
    question = random.randint(RANDOM_FROM, RANDOM_TO)
    correct_answer = 'yes' if is_prime(question) else 'no'

    question = str(question)

    return question, correct_answer
