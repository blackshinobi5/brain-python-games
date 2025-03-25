# Brain Games

[![Maintainability](https://api.codeclimate.com/v1/badges/22dd2837ef0c911e6562/maintainability)](https://codeclimate.com/github/blackshinobi5/brain-python-games/maintainability)  
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Набор консольных математических игр, написанных на Python.

## Игры

### 1. Наименьшее общее кратное (НОК)
Пользователю показывается три случайных числа, которые нужно вычислить.

**Пример:**

Вопрос: 5 7 15  
Твой ответ: 105  
Верно!  

### 2. Геометрическая прогрессия
Нужно найти пропущенное число в последовательности.

**Пример:**

Вопрос: 1 2 .. 8 16  
Твой ответ: 4  
Верно!  


## Установка
```bash
git clone https://github.com/blackshinobi5/brain-python-games.git
cd brain-python-games/brain-python-games
pip install -e .
```
## Запуск
```bash
python -m main
```
## Демонстрация 
Игра НОК:  
  
[![Demo](https://asciinema.org/a/E9A4BcxlgvmZnADiU8xZyaCGB.png)](https://asciinema.org/a/E9A4BcxlgvmZnADiU8xZyaCGB)

Игра Прогрессия:
  
[![Demo](https://asciinema.org/a/MgfrSBbw1X6QthlUIrK5zOsRL.png)](https://asciinema.org/a/MgfrSBbw1X6QthlUIrK5zOsRL) 

## Структура проекта
```bash
brain-games-python/
├── brain_games/
│   ├── games/
│   │   ├── nom.py          # Игра "НОК"
│   │   └── gp.py           # Игра "Прогрессия"
│   └── engine.py           # Общая логика
├── main.py                 # Запуск игры
├── README.md               # Описание проекта
└── Ruff.toml               # Настройки линтера
```
## Проверка кода
```bash
ruff check .  # Проверка стиля
ruff --fix .  # Автоисправления
```
## CodeClimate
Проект проверяется на:  
Поддерживаемость кода  
Отсутствие дублирований  
Соблюдение стиля  
