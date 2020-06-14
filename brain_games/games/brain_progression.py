"""
Игра "Арифметическая прогрессия"
Суть игры в следующем: Показываем игроку ряд чисел, образующий
арифметическую прогрессию, заменив любое из чисел двумя точками.
Игрок должен определить это число.
"""

import random

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_SIZE = 10


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """

    question = ''
    correct_answer = ''

    step = random.randint(1, 10)  # шаг
    hidden_step = random.randint(1, 10)  # скрытый от игрока шаг

    # от 1 до [step*10] (10 чисел) с шагом [step]
    i = 1
    for number in range(1, step*10, step):
        if i == hidden_step:
            question = question + '..' + ' '
            correct_answer = str(number)
        else:
            question = question + str(number) + ' '
        i += 1

    return question, correct_answer
