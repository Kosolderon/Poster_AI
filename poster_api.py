import os
import requests

def get_sales_data():
    token = os.getenv("POSTER_API_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    # Здесь заглушка — можно вставить реальный запрос к Poster
    return "🔸 Латте — 145 шт. — 34 500₽\n🔸 Асаи боул — 92 шт. — 28 400₽"
