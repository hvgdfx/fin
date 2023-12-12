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
def requset_index_sz_element(index_code):
    try_count = 0
    while True:
        # 1. url
        _ = str(int(time.time() * 1000))
        url = f"https://query.sse.com.cn/commonSoaQuery.do?&sqlId=DB_SZZSLB_CFGLB&indexCode={index_code}&isPagination=false&_={_}"

        # 2. headers
        proxy_json = requests.get("http://stock_proxy:5010/get").json()
        #print(f"proxy_json: {proxy_json}")
        if proxy_json["https"]:
            #print("没有http代理可用")
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
        #print(f"headers: {headers}")
        #print(f"proxies: {proxies}")

        # 3. response

        try_count += 1
        try:
            resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=(1, 10))
        except Exception as e:
            #print(e)
            continue
        if try_count > 10:
            break
        if resp.status_code == 200:
            return resp
        else:
            #print(f"resp {try_count} status code {resp.status_code}")
            pass
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
def insert_data_list(index_code, data_list):
    for data in data_list:
        values = insert_data(data)
        todate = datetime.now()
        dt = todate.strftime('%Y-%m-%d')
        # client.client.execute(f"insert into stock.index_sz VALUES ('{index_code}', {values}, '{dt}')")
        sql = f"insert into stock.index_sz_element VALUES ('{index_code}', {values}, '{dt}')"
        #print(sql)
        client.client.execute(sql)


def insert_data(data):
    fileds = [
        "securityAbbrEn",
        "securityAbbr",
        "inDate",
        "securityCode",
        "marketSource",
    ]

    values = ""
    print_values = ""
    count = 0
    for k, v in data.items():
        count += 1
        if k in fileds:
            values += f" '{get_str(v)}'"
            print_values += f" '{get_str(v)}'"
        else:
            values += f" ''"
            print_values += f" ' ''"
        if count != len(fileds):
            values += ","
    # print(print_values)
    return values


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

def index_list():
    result = client.client.execute(f"select indexCode from stock.index_sz where indexCode != '';")
    result = [t[0] for t in result]
    return result


def run(index_code):
    resp = requset_index_sz_element(index_code)
    if resp is None:
        return
    #print(f"-----------------------------------------------")

    data = parse_response(resp)
    #print(type(data))
    #print(data[0])
    #print(f"-----------------------------------------------")

    insert_data_list(index_code, data)
    #print(f"-----------------------------------------------")


if __name__ == '__main__':
    index_list = index_list()
    for index_code in index_list:
        try:
            run(index_code)
            print(f"index_code: {index_code} success")
        except Exception as e:
            print(f"index_code: {index_code} fail {e}")
