"""
Игра "Калькулятор"
Суть игры в следующем: пользователю показывается случайное математическое
выражение, например 35 + 16, которое нужно вычислить
и записать правильный ответ.
"""
import random
import operator

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """

    question = ''
    correct_answer = ''

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Choose operation
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    # список операторов
    list_operations = operation.keys()
    # делаем коллекцию
    list_operations = list(list_operations)
    # выбираем один из операторов
    operator_str = random.choice(list_operations)

    # действие, которое требуется произвести
    action = operation.get(operator_str)
    correct_answer = str(action(num1, num2))

    question = str(num1) + ' ' + operator_str + ' ' + str(num2)

    return question, correct_answer
