"""
Игра "Калькулятор"
Суть игры в следующем: пользователю показывается случайное математическое
выражение, например 35 + 16, которое нужно вычислить
и записать правильный ответ.
"""
import random
import operator

GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Choose operation
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    # список операторов
    signs = list(operations.keys())
    # выбираем один из операторов случайным образом
    chosen_operator = random.choice(signs)

    # действие, которое требуется произвести
    action = operations.get(chosen_operator)
    correct_answer = str(action(num1, num2))

    question = str(num1) + ' ' + chosen_operator + ' ' + str(num2)

    return question, correct_answer
