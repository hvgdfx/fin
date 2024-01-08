import sys

sys.path.append("../../")

import requests
import time
import json
from fake_useragent import UserAgent
from spider.utils.ck_utils import client
from datetime import datetime

ua = UserAgent()

board_dict = {}


# 1. request
def requset_index_eastmoney_board_element(borad_id):
    try_count = 0
    while True:
        # 1. url
        _ = str(int(time.time() * 1000))
        # url = "https://80.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407406103905453114_1704696146206&pn=3&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=b:BK0726+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1704696146231"
        # "&cb=jQuery112407406103905453114_1704696146206" \
        # "&ut=bd1d9ddb04089700cf9c27f6f7426281" \
        url = f"https://80.push2.eastmoney.com/api/qt/clist/get?" \
              "pn=1" \
              "&pz=2000" \
              "&po=1" \
              "&np=1" \
              "&fltt=2" \
              "&invt=2" \
              "&wbp2u=|0|0|0|web" \
              "&fid=f3" \
              f"&fs=b:{borad_id}+f:!50" \
              "&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45" \
              f"&_={str(int(time.time() * 1000))}"

        # 2. headers
        proxy_json = requests.get("http://stock_proxy:5010/get").json()
        # print(f"proxy_json: {proxy_json}")
        if proxy_json["https"]:
            # print("没有http代理可用")
            continue

        proxies = {
            "http": f"http://{proxy_json['proxy']}"
        }

        headers = {
            "user-agent": ua.random,
            #     "Accept": "*/*",
            #     "Accept-Encoding": "gzip, deflate, br",
            #     "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            #     "Cache-Control": "no-cache",
            #     "Connection": "keep-alive",
            #     "Host": "80.push2.eastmoney.com",
            #     "Pragma": "no-cache",
            #     "Referer": "https://quote.eastmoney.com/center/boardlist.html",
            #     "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            #     "Sec-Ch-Ua-Mobile": "?0",
            #     "Sec-Ch-Ua-Platform": '"Windows"',
            #     "Sec-Fetch-Dest": "script",
            #     "Sec-Fetch-Mode": "no-cors",
            #     "Sec-Fetch-Site": "same-site",
        }
        # print(f"headers: {headers}")
        # print(f"proxies: {proxies}")
        # print(f"url: {url}")

        # 3. response

        try_count += 1
        try:
            resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=(1, 10))
        except Exception as e:
            print(e)
            continue
        if try_count > 10:
            break
        if resp.status_code == 200:
            return resp
        else:
            # print(f"resp {try_count} status code {resp.status_code}")
            pass
    return None


# 2. parse data
def parse_response(resp, board_id):
    # 1. check data
    # 2. parse data
    data_list = []
    if resp is None:
        return None
    else:
        try:
            data = resp.json()["data"]
            diffs = data["diff"]
            for diff in diffs:
                data_list.append([diff["f12"], diff["f14"]])
        except Exception as e:
            print(e)
            print(f"parse response {data_list}")
    return data_list


# 3. insert data
def insert_data_list(board_id, data_list, dt):
    for data in data_list:
        data = [f"'{str(d)}'" for d in data]
        values = ",".join(data)
        board_name = board_dict[board_id]
        sql = f"insert into stock.index_eastmoney_board_element VALUES ('{board_id}', '{board_name}', {values}, '{dt}')"
        # print(sql)
        client.client.execute(sql)


def get_index_list(dt):
    result = client.client.execute(
        f"select distinct board_id, board_name from stock.index_eastmoney_board where board_id != '' and dt='{dt}';")
    result = {t[0]: t[1] for t in result}
    return result


def run(board_id, dt):
    resp = requset_index_eastmoney_board_element(board_id)
    if resp is None:
        return
    # print(f"-----------------------------------------------")

    data_list = parse_response(resp, board_id)
    # print(f"-----------------------------------------------")

    insert_data_list(board_id, data_list, dt)
    # print(f"-----------------------------------------------")


def runall(dt):
    global board_dict
    board_dict = get_index_list(dt)
    for board_id, board_name in board_dict.items():
        try:
            run(board_id, dt)
            print(f"board_id: {board_id} success")
        except Exception as e:
            print(f"board_id: {board_id} fail {e}")


if __name__ == '__main__':
    todate = datetime.now()
    dt = todate.strftime('%Y-%m-%d')

    board_dict = get_index_list(dt)
    # run("BK0726", dt)
    runall(dt)
