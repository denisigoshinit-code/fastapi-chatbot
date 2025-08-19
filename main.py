# main.py

from fastapi import FastAPI
from openai import OpenAI
import os
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Указываем имя модели. Удобно вынести в константу для быстрой замены.
MODEL_NAME = "mistralai/mixtral-8x7b-instruct"

# Создаем главный объект FastAPI-приложения
app = FastAPI()

# Подключаем папку со статическими файлами (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создаем клиент для работы с API OpenRouter.
# Ключ берется из переменной окружения для безопасности.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# Функция для отправки запроса в OpenRouter и получения ответа от ИИ.
def ask_openrouter(prompt):
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Ты полезный ассистент. Отвечай ВСЕГДА ТОЛЬКО НА РУССКОМ ЯЗЫКЕ."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Произошла ошибка при обращении к OpenRouter."
    
# Маршрут для главной страницы. Возвращает файл index.html.
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()

# Маршрут для чат-бота. Принимает вопрос и возвращает ответ от ИИ.
@app.get("/ask/")
def ask_bot(q: str):
    response = ask_openrouter(q)
    return {"response": response}