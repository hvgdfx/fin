import requests
from datetime import datetime
from constant.constant import TOKEN
from constant.proxy import proxies

def text_hello(chat_id):
    # 处理 /start 命令
    send_message(chat_id, "hvgdfx 你好 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=params, proxies=proxies)
    return response.json()
