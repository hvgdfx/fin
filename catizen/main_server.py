import time
import requests
import platform
import json
from pprint import pprint
from constant.constant import TOKEN
from constant.proxy import proxies
from methed.get_updates import handle_updates

last_update_id = None

os_name = platform.system()

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"offset": offset, "timeout": 30}  # 设置超时时间为30秒
    response = requests.get(url, params=params, proxies=proxies)
    print(f"updates:")
    pprint(response.json())
    return response.json()


def get_me(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url, proxies=proxies)
    print(f"getMe:")
    pprint(response.json())
    return response.json()


def run():
    global last_update_id
    while True:
        print("---------------------------------------------")
        # update
        updates = get_updates(offset=last_update_id)
        if updates["result"]:
            handle_updates(updates)
            last_update_id = updates["result"][-1]["update_id"] + 1
        # getMe
        get_me_response = get_me()
        time.sleep(1)  # 每秒轮询一次


if __name__ == "__main__":
    run()
