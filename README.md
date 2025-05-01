# 🚚 Telegram Delivery Bot

Этот Telegram-бот написан на Python с использованием библиотеки **aiogram 3.x** (это учебный проект, чтобы показать ученикам работу бота). Он симулирует процесс оформления заказа доставки через Telegram.

## 📦 Возможности

- Приветствие пользователя
- Выбор товара
- Ввод адреса доставки
- Подтверждение заказа
- Симуляция обработки заказа

## 🛠️ Технологии

- Python 3.10+
- aiogram 3.18
- asyncio

## 📂 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/delivery-bot.git
cd delivery-bot
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```


### Структура Проекта
```bash
delivery-bot/
├── bot.py                # Главный файл запуска бота
├── handlers.py           # Обработчики команд и сообщений
├── keyboards.py          # Клавиатуры
├── config.py             # Конфигурация
├── requirements.txt      # Зависимости проекта
└── .env                  # Переменные окружения (не публикуйте!)
```
