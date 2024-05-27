from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
TOKEN = '7324173757:AAHQFc7tuZEMrmBtj2Nr3IAjEI8H441m-ro'
CHAT_ID = None  # Изначально идентификатор чата пуст

def send_message(text):
    global CHAT_ID
    if CHAT_ID is None:
        print("Chat ID is not set.")
        return
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': "Ваш уникальный ID: " + text
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code}, {response.text}")

@app.route('/set_chat_id', methods=['POST'])
def set_chat_id():
    global CHAT_ID
    data = request.json
    chat_id = data.get('chat_id', '')
    if not chat_id:
        return jsonify({'error': 'No chat_id provided'}), 400
    CHAT_ID = chat_id
    return jsonify({'message': ''}), 200

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    send_message(message)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)