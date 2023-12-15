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
def requset_index_zz():
    try_count = 0
    while True:
        # 1. url
        url = f"https://www.csindex.com.cn/csindex-home/index-list/query-index-item?type__1773=CqfxRDuDBDnD0ADlg%2BG7Ktq0KuiErKDRrnbD"

        # 2. headers
        proxy_json = requests.get("http://stock_proxy:5010/get").json()
        #print(f"proxy_json: {proxy_json}")
        if proxy_json["https"]:
            print("没有http代理可用")
            continue

        proxies = {
            "http": f"http://{proxy_json['proxy']}"
        }

        headers = {
            "user-agent": ua.random,
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate,br",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "www.csindex.com.cn",
            "Origin": "https://www.csindex.com.cn",
            "Pragma": "no-cache",
            "Referer": "https://www.csindex.com.cn/",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
        print(f"headers: {headers}")
        print(f"proxies: {proxies}")

        # 3. response
        post_param = {}
        indexFilter = {"indexSeries": ["1"]}
        pager = {"pageNum": 1, "pageSize": 300}
        sorter = {"sortField": "null", "sortOrder": None}
        post_param["indexFilter"] = indexFilter
        post_param["pager"] = pager
        post_param["sorter"] = sorter

        try_count += 1
        try:
            resp = requests.post(url=url, headers=headers, proxies=proxies, timeout=(1, 10), data=post_param, json=False)
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
    resp = requset_index_zz()
    if resp is None:
        return
    print(f"-----------------------------------------------")

    data = parse_response(resp)
    print(f"-----------------------------------------------")

    insert_data_list(data)
    print(f"-----------------------------------------------")


if __name__ == '__main__':
    run()
