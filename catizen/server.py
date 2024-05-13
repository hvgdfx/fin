import requests
import time
from datetime import datetime


# 替换为您的 Telegram Bot Token
TOKEN = '6955121712:AAHug7zbealQl4O1v4Milcrr6JQJKKTQ4rs'

def get_updates(offset=None):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    params = {'offset': offset, 'timeout': 30}  # 设置超时时间为30秒
    response = requests.get(url, params=params)
    return response.json()

def handle_updates(updates):
    for update in updates['result']:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        if text == '/start':
            # 处理 /start 命令
            send_message(chat_id, "jump " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=params)
    return response.json()

def main():
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)
        print(f"updates: " + updates)
        if updates['result']:
            handle_updates(updates)
            last_update_id = updates['result'][-1]['update_id'] + 1
        time.sleep(1)  # 每秒轮询一次


if __name__ == '__main__':
    main()