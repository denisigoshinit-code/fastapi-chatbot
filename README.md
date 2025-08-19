# FastAPI Chatbot

Этот проект представляет собой простой чат-бот, созданный с использованием фреймворка FastAPI. Бот использует API OpenRouter для генерации ответов.

## Особенности
* **Технологии:** Python, FastAPI
* **API:** OpenRouter
* **Интерфейс:** Простой HTML и JavaScript для взаимодействия с ботом

## Установка и запуск локально

1.  Клонируйте репозиторий:
    ```bash
    git clone [https://github.com/denisigoshinit-code/fastapi-chatbot.git](https://github.com/denisigoshinit-code/fastapi-chatbot.git)
    ```
2.  Перейдите в папку проекта:
    ```bash
    cd fastapi-chatbot
    ```
3.  Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    ```
4.  Установите необходимые библиотеки:
    ```bash
    pip install -r requirements.txt
    ```
5.  Создайте файл `.env` и добавьте свой API-ключ:
    ```
    OPENROUTER_API_KEY="ВАШ_КЛЮЧ"
    ```
6.  Запустите приложение:
    ```bash
    uvicorn main:app --reload
    ```
    Бот будет доступен по адресу: `http://127.0.0.1:8000`

## Развернутая версия
Проект развернут на платформе Render и доступен по ссылке:
[https://fastapi-denis-chatbot.onrender.com/](https://fastapi-denis-chatbot.onrender.com/)
