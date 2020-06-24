"""
Игра "Арифметическая прогрессия"
Суть игры в следующем: Показываем игроку ряд чисел, образующий
арифметическую прогрессию, заменив любое из чисел двумя точками.
Игрок должен определить это число.
"""

import random

GAME_DESCRIPTION = 'What number is missing in the progression?'
START_NUMBER = 1
PROGRESSION_SIZE = 10
STEPS_FROM = 1
STEPS_TO = 10


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """
    # шаг
    step = random.randint(STEPS_FROM, STEPS_TO)
    # индекс скрытого от игрока шага
    hidden_step_index = random.randint(STEPS_FROM, STEPS_TO)
    question = ''

    i = 0
    while i < PROGRESSION_SIZE:
        number = str(START_NUMBER + step * i)

        if hidden_step_index == i+1:
            correct_answer = number
            number = '..'

        question = number if i == 0 else question + ' ' + str(number)

        i += 1

    return question, correct_answer
