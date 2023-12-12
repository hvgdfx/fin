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
def requset_index_sz():
    try_count = 0
    while True:
        # 1. url
        _ = str(int(time.time() * 1000))
        jsonCallBack = "jsonpCallback311835"
        isPagination = "false"
        sqlId = "DB_SZZSLB_ZSLB"
        # url = f"http://query.sse.com.cn/commonSoaQuery.do?jsonCallBack={jsonCallBack}&isPagination={isPagination}&sqlId={sqlId}&_={_}"
        url = f"http://query.sse.com.cn/commonSoaQuery.do?isPagination={isPagination}&sqlId={sqlId}&_={_}"

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
        if try_count > 3:
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
            data = resp.json()["result"]
        except Exception as e:
            print(e)
            print(f"parse response {data}")
    return data


def check_data(resp) -> bool:
    return False


def parse_data(resp):
    pass


# 3. insert data
def insert_data_list(data_list):
    for data in data_list:
        values = insert_data(data)
        # print(values)
        todate = datetime.now()
        dt = todate.strftime('%Y-%m-%d')
        sql = f"insert into stock.index_sz VALUES ({values}, {dt})"
        print(sql)
        client.client.execute(f"insert into stock.index_sz VALUES ({values}, '{dt}')")


def insert_data(data):
    fileds = [
        "handbookUrl",
        "nIndexFullNameEn",
        "nIndexNameEn",
        "tIndexCode",
        "nIndexCode",
        "indexReleaseChannel",
        "indexCode",
        "introEn",
        "indexFullName",
        "nIndexFullName",
        "totalReturnIntro",
        "tIndexNameEn",
        "indexFullNameEn",
        "isNetLncomeIndex",
        "intro",
        "tIndexFullName",
        "indexBaseDay",
        "ifIndexCode",
        "numOfStockes",
        "netReturnIntroEn",
        "indexBasePoint",
        "indicsSeqDescEn",
        "indexName",
        "netReturnIntro",
        "isPriceIndex",
        "updateTime",
        "indicsSeqDesc",
        "indexDataSourceType",
        "launchDay",
        "methodologyNameEn",
        "methodologyName",
        "tIndexFullNameEn",
        "handbookEnUrl",
        "indicsSeq",
        "nIndexName",
        "indexNameEn",
        "totalReturnIntroEn",
        "tIndexName",
        "isTotalReturnIndex",
    ]

    print_fields = ["indexCode", "indexName"]

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
        v = v.replace("\'", "")
    else:
        v = json.dumps(v)
    return v


def run():
    resp = requset_index_sz()
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
