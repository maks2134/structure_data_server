from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = '7324173757:AAHQFc7tuZEMrmBtj2Nr3IAjEI8H441m-ro'
CHAT_ID = '488862472'  # Имя пользователя вместо URL

def send_message(text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': 'Ваш уникальный ID: ' + text,
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code}, {response.text}")

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get('message', '')
    send_message(message)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)