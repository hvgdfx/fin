import sys

sys.path.append("../../")

import requests
import time
import json
from fake_useragent import UserAgent
from spider.utils.ck_utils import client

ua = UserAgent()


# 1. request
def requset_index_sz_element():
    try_count = 0
    while True:
        # 1. url
        _ = str(int(time.time() * 1000))
        url = f"https://query.sse.com.cn/commonSoaQuery.do?&sqlId=DB_SZZSLB_CFGLB&indexCode=000001&isPagination=false&_={_}"

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
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "query.sse.com.cn",
            "Pragma": "no-cache",
            "Referer": "http://www.sse.com.cn/",
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
        if try_count > 10:
            break
        if resp.status_code == 200:
            return resp
        else:
            print(f"resp {try_count} status code {resp.status_code}")
    return None


# 2. parse data
def parse_response(resp):
    # 1. check data
    # 2. parse data
    data = {}
    if resp is None:
        return None
    else:
        try:
            data = resp.json()["pageHelp"]["data"]
        except Exception as e:
            print(e)
            print(f"parse response {data}")
    return data


# 3. insert data
def insert_data_list(data_list):
    for data in data_list:
        values = insert_data(data)
        # print(values)
        # client.client.execute(f"insert into stock.index_sz VALUES ({values})")


def insert_data(data):
    fileds = [
        "securityAbbrEn",
        "securityAbbr",
        "inDate",
        "securityCode",
        "marketSource",
    ]

    valus = ""
    print_values = ""
    count = 0
    for k, v in data.items():
        count += 1
        if k in fileds:
            valus += f" '{get_str(v)}'"
            print_values += f" '{get_str(v)}'"
        else:
            valus += f" ''"
            print_values += f" ' ''"
        if count != len(fileds):
            valus += ","
    print(print_values)
    return valus


def get_str(v):
    if isinstance(v, int):
        v = str(v)
    elif isinstance(v, float):
        v = str(v)
    elif isinstance(v, str):
        v = v
    else:
        v = json.dumps(v)
    return v


def run():
    resp = requset_index_sz_element()
    if resp is None:
        return
    print(f"-----------------------------------------------")

    data = parse_response(resp)
    print(type(data))
    print(data[0])
    print(f"-----------------------------------------------")

    insert_data_list(data)
    print(f"-----------------------------------------------")


if __name__ == '__main__':
    run()