from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

import requests
import os


load_dotenv()
token = os.getenv('TOKEN')
admin = os.getenv('ADMIN_ID')


app = Flask(__name__)

# Токен вашего бота
BOT_TOKEN = token
# ID администратора (ваш ID в Telegram)
ADMIN_CHAT_ID = admin

# Функция для отправки сообщения администратору
def send_to_admin(stars, full_name, phone_number):
    message = (
        f"Новый запрос на продажу Stars!\n\n"
        f"Количество Stars: {stars}\n"
        f"ФИО: {full_name}\n"
        f"Номер телефона: {phone_number}"
    )
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": ADMIN_CHAT_ID,
        "text": message
    }
    
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    stars = data.get('stars')
    full_name = data.get('full_name')
    phone_number = data.get('phone_number')
    
    # Отправляем данные администратору
    send_to_admin(stars, full_name, phone_number)
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)