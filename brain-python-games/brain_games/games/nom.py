import math
import random

def lcm(a, b, c):
    return math.lcm(a, b, c)

def get_lcm_game_data():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = str(lcm(*numbers))
    return question, correct_answer
