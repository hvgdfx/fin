import sys

sys.path.append("../../")

import requests
import time
import json
from fake_useragent import UserAgent
from spider.utils.ck_utils import client
from datetime import datetime

ua = UserAgent()


# 1. request
def requset_index_eastmoney_board():
    try_count = 0
    while True:
        # 1. url
        url = "https://quote.eastmoney.com/center/api/sidemenu.json"

        # 2. headers

        proxy_json = requests.get("http://stock_proxy:5010/get").json()
        print(f"proxy_json: {proxy_json}")
        if proxy_json["https"]:
            print("没有http代理可用")
            continue

        proxies = {
            "http": f"http://{proxy_json['proxy']}"
        }

        headers = {
            "user-agent": ua.random,
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "quote.eastmoney.com",
            "Pragma": "no-cache",
            "Referer": "https://quote.eastmoney.com/center/boardlist.html",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Requested-With": "XMLHttpRequest",
        }
        print(f"headers: {headers}")
        print(f"proxies: {proxies}")

        # 3. response

        try_count += 1
        try:
            resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=(1, 10))
        except Exception as e:
            print(e)
            continue
        if try_count > 3:
            break
        if resp.status_code == 200:
            return resp
        else:
            print(f"resp {try_count} status code {resp.status_code}")
            print(resp.text)
    return None


# 2. parse data
def parse_response(resp):
    # 1. check data
    # 2. parse data
    data_list = []
    if resp is None:
        return None
    else:
        try:
            data = resp.json()
            if len(data) > 5:
                data = data[5]
            else:
                sys.exit(1)

            # layer1
            data = data["next"]
            # layer2
            # concept_board_data = data[0]
            # region_board_data = data[1]
            # industry_board_data = data[2]

            for board_data in data:
                board_type = board_data["key"]
                board_type_cn = board_data["title"]
                board_type_href = board_data["href"]
                for board in board_data["next"]:
                    board_key = board["key"]
                    board_id = board["key"].split(".")[1]
                    board_name = board["title"]
                    board_href = board["href"]
                    board_order = board["order"]
                    tmp = [board_type, board_type_cn, board_type_href, board_key, board_id, board_name, board_href,
                           board_order]
                    data_list.append(tmp)
            return data_list
        except Exception as e:
            print(e)
            # print(f"parse response {data_list}")
    return data_list


# 3. insert data
def insert_data_list(data_list, dt):
    for data in data_list:
        values = []
        for _ in data:
            values.append(f"'{str(_)}'")
        values = ",".join(values)
        # print(values)
        sql = f"insert into stock.index_eastmoney_board VALUES ({values}, '{dt}')"
        print(sql)
        client.client.execute(sql)


def get_str(v):
    if isinstance(v, int):
        v = str(v)
    elif isinstance(v, float):
        v = str(v)
    elif isinstance(v, str):
        v = v.replace("\'", "")
    else:
        v = json.dumps(v)
    return v


def run(dt):
    resp = requset_index_eastmoney_board()
    if resp is None:
        return
    print(f"-----------------------------------------------")

    data = parse_response(resp)
    print(f"-----------------------------------------------")

    insert_data_list(data, dt)
    print(f"-----------------------------------------------")


if __name__ == '__main__':
    todate = datetime.now()
    dt = todate.strftime('%Y-%m-%d')

    run(dt)
