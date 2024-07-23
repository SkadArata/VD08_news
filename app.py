from flask import Flask, render_template, request
from config import NEWS_API
import requests
import random

# Создайте экземпляр Flask
app = Flask(__name__)

# Настройте ваш API ключ
NEWS_API_KEY = NEWS_API

def get_random_quote():
    # Запрос к News API
    url = f'https://newsapi.org/v2/top-headlines?language=ru&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Извлекаем цитаты из новостей
    articles = data.get('articles', [])
    quotes = [article['title'] for article in articles if article['title']]

    # Выбираем случайную цитату
    return random.choice(quotes) if quotes else "Нет доступных цитат"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Если POST-запрос, получаем новую случайную цитату
        quote = get_random_quote()
    else:
        # Если GET-запрос, тоже получаем цитату
        quote = get_random_quote()

    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)