import math
import random


def find_lcm(a, b, c):
    lcm_ab = (a * b) // math.gcd(a, b)
    lcm_abc = (lcm_ab * c) // math.gcd(lcm_ab, c)
    return lcm_abc


def play():
    print("Найди наименьшее общее кратное для чисел ниже.")
    for _ in range(3):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        lcm = find_lcm(a, b, c)

        print(f"{a} {b} {c}")
        user_answer = int(input("Твой ответ: "))

        if user_answer != lcm:
            print(f"Ты умер(ла)! {user_answer} - это неправильный ответ :<."
                  f" Правильный ответ был - {lcm}.")
            return False
        print("Молодец! Ты прошел уровень!")
    return True
