import time 
import requests
import socks
import socket

proxy_host = '127.0.0.1'
proxy_port = 7897

proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_host}:{proxy_port}'
}

TOKEN = '6955121712:AAHug7zbealQl4O1v4Milcrr6JQJKKTQ4rs'

last_update_id = None 

def get_updates(offset=None):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    params = {'offset': offset, 'timeout': 30}  # 设置超时时间为30秒
    response = requests.get(url, params=params)
    return response.json()

def get_me(offset=None):
    url = f'https://api.telegram.org/bot{TOKEN}/getMe'
    response = requests.get(url)
    return response.json()

def run():
    global last_update_id
    while True:
        updates = get_updates(offset=last_update_id)
        print(f"updates:\t" + updates)
        get_me_response = get_me()
        print(f"getMe:\t" + get_me_response)
        time.sleep(1)  # 每秒轮询一次


if __name__ == '__main__':
    print("123")
    run()
    print("234")