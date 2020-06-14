"""
Игра "Проверка на четность"
Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное,
или no - если нечетное.
"""
from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(num):
    """Check if num is even.
    Returns:
        true or false: boolean
    """
    return num % 2 == 0


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """
    number = randint(1, 20)

    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer
