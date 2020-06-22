"""
Игра "Арифметическая прогрессия"
Суть игры в следующем: Показываем игроку ряд чисел, образующий
арифметическую прогрессию, заменив любое из чисел двумя точками.
Игрок должен определить это число.
"""

import random

GAME_DESCRIPTION = 'What number is missing in the progression?'
START_NUMBER = 5
PROGRESSION_SIZE = 10


def generate_question_and_answer():
    """Generate question and answer for user
    Returns:
        question: string
        correct_answer: string
    """
    # шаг
    step = random.randint(START_NUMBER, PROGRESSION_SIZE)
    # индекс скрытого от игрока шага
    hidden_step_index = random.randint(START_NUMBER, PROGRESSION_SIZE)

    i = 1
    question = str(START_NUMBER)
    while i < PROGRESSION_SIZE:
        number = str(START_NUMBER + step * i)
        if hidden_step_index == i:
            question = question + ' ' + '..'

            # правильный ответ, который скрыт от пользователя
            correct_answer = number
        else:
            question = question + ' ' + number

        i += 1

    return question, correct_answer
