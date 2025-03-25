# Brain Games

[![Maintainability](https://api.codeclimate.com/v1/badges/22dd2837ef0c911e6562)](https://codeclimate.com/github/blackshinobi5/brain-python-games)
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

### Установка

git clone https://github.com/blackshinobi5/brain-python-games.git
cd brain-python-games/brain-python-games
pip install -e .

### Запуск
python -m main

### Демонстрация ----------------------------------------------------------------------------------------
Игра НОК
Игра Прогрессия

### Структура проекта
brain-games-python/
├── brain_games/
│   ├── games/
│   │   ├── lcm.py          # Игра "НОК"
│   │   └── progression.py  # Игра "Прогрессия"
│   └── engine.py           # Общая логика
├── main.py                 # Запуск игры
├── README.md               # Описание проекта
└── Ruff.toml               # Настройки линтера

### Проверка кода
ruff check .  # Проверка стиля
ruff --fix .  # Автоисправления

### CodeClimate
Проект проверяется на:
Поддерживаемость кода
Отсутствие дублирований
Соблюдение стиля
