import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]

    hidden_index = random.randint(1, length - 2)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


def get_progression_game_data():
    return generate_progression()
