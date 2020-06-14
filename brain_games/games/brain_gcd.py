"""
Игра "Наибольший общий делитель (НОД)"
Суть игры в следующем: пользователю показывается два случайных
числа, например, 25 50. Пользователь должен вычислить
и ввести наибольший общий делитель этих чисел.
"""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """

    question = ''
    correct_answer = ''

    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    question = str(num1) + ' ' + str(num2)

    # Используем алгоритм Евклида для нахождения
    # наибольшего общего делителя (НОД)
    #  Вычислим, какое из чисел больше
    (bigger_num, smaller_num) = (num1, num2) if num1 > num2 else (num2, num1)
    #  Вычсислим сам НОД
    while bigger_num % smaller_num > 0:
        temp_smaller_num = smaller_num
        smaller_num = bigger_num % smaller_num
        bigger_num = temp_smaller_num

    correct_answer = str(smaller_num)

    return question, correct_answer
