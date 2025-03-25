import random


def play():
    print("Какое число пропущено в моей прогрессии???")
    for _ in range(3):
        step = random.randint(2, 5)
        length = random.randint(5, 10)
        start_power = random.randint(0, 6)  # 2^0=1, 2^6=64
        start = step ** start_power
        progression = [start * (step ** i) for i in range(length)]
        hidden_index = random.randint(0, length - 1)
        answer = progression[hidden_index]
        progression[hidden_index] = ".."

        print(" ".join(map(str, progression)))
        user_answer = int(input("Твой ответ: "))

        if user_answer != answer:
            print(f"Ты умер(ла)! {user_answer} это неправильный ответ :<."
                  f" Правильный ответ был - {answer}.")
            return False
        print("Молодец! Уровень пройден!")
    return True
