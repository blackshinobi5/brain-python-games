def run_game(game_module):
    # Определяем название игры по имени модуля
    game_name = {
        'nom': '"Наименьшее общее кратное"',
        'gp': '"Геометрическая прогрессия"'
    }.get(game_module.__name__.split('.')[-1])

    print(f"Добро пожаловать в игру {game_name}!")
    name = input("Введите ваше имя: ")
    print(f"Добро пожаловать, {name}!")

    if game_module.play():
        print(f"Поздравляю! Ты прошел игру, {name}!")
    else:
        print(f"Давай по новой, {name}!")
