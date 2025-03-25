from brain_games.games import gp, nom
from brain_games.unreal_engine import run_game


def main():
    print("1. НОМ\n2. Геометическая прогрессия")
    choice = input("Выбери игрульку (1 или 2): ")
    if choice == "1":
        run_game(nom)
    elif choice == "2":
        run_game(gp)
    else:
        print("Error! Ты не выбрал игру?")


if __name__ == "__main__":
    main()
