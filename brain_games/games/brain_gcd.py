"""
Игра "Наибольший общий делитель (НОД)"
Суть игры в следующем: пользователю показывается два случайных
числа, например, 25 50. Пользователь должен вычислить
и ввести наибольший общий делитель этих чисел.
"""
import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
RANDOM_FROM = 10
RANDOM_TO = 100


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """

    num1 = random.randint(RANDOM_FROM, RANDOM_TO)
    num2 = random.randint(RANDOM_FROM, RANDOM_TO)
    question = str(num1) + ' ' + str(num2)

    correct_answer = str(get_gcd(num1, num2))

    return question, correct_answer


def get_gcd(num1, num2):
    """Find a greatest common divider
    We use the Euclidean algorithm to find the greatest common divisor (GCD)
    """

    (bigger_num, smaller_num) = (num1, num2) if num1 > num2 else (num2, num1)

    while bigger_num % smaller_num > 0:
        temp_smaller_num = smaller_num
        smaller_num = bigger_num % smaller_num
        bigger_num = temp_smaller_num

    return smaller_num
