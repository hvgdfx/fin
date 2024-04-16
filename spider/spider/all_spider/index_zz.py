import sys

sys.path.append("../../")

import requests
import time
import json
from fake_useragent import UserAgent
from spider.utils.ck_utils import client
from datetime import datetime
from spider.utils.check_table_util import check_row_num

ua = UserAgent()

TABLE_NAME = "stock.index_zz"


# 1. request
def requset_index_zz():
    try_count = 0
    while True:
        # 1. url
        url = f"https://www.csindex.com.cn/csindex-home/index-list/query-index-item?type__1773=CqfxRDuDBDnD0ADlg%2BG7Ktq0KuiErKDRrnbD"

        # 2. headers
        proxy_json = requests.get("http://stock_proxy:5010/get").json()
        # print(f"proxy_json: {proxy_json}")
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
        pager = {"pageNum": 1, "pageSize": 3000}
        sorter = {"sortField": "null", "sortOrder": None}
        post_param["indexFilter"] = indexFilter
        post_param["pager"] = pager
        post_param["sorter"] = sorter

        try_count += 1
        try:
            resp = requests.post(url=url, headers=headers, proxies=proxies, timeout=(1, 10), json=post_param)
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
            code = resp.json()["code"]
            if "200" == code:
                data = resp.json()["data"]
            else:
                data
        except Exception as e:
            print(e)
            print(f"parse response {data}")
    return data


# 3. insert data
def insert_data_list(data_list, dt):
    for data in data_list:
        values = insert_data(data)
        # print(values)
        sql = f"insert into {TABLE_NAME} VALUES ({values}, '{dt}')"
        print(sql)
        client.client.execute(sql)


def insert_data(data):
    fileds = [
        "indexCompliance",
        "indexComplianceEn",
        "ifTracked",
        "ifTrackedEn",
        "indexSeries",
        "indexSeriesEn",
        "key",
        "indexCode",
        "indexName",
        "indexNameEn",
        "consNumber",
        "latestClose",
        "monthlyReturn",
        "indexType",
        "assetsClassify",
        "assetsClassifyEn",
        "hotSpot",
        "hotSpotEn",
        "region",
        "regionEn",
        "currency",
        "currencyEn",
        "ifCustomized",
        "ifCustomizedEn",
        "indexClassify",
        "indexClassifyEn",
        "ifWeightCapped",
        "ifWeightCappedEn",
        "publishDate",
        "ifProtect",
        "protectStartDate",
        "protectEndDate",
        "ifTopDing",
    ]

    values = ""
    count = 0
    for k, v in data.items():
        count += 1
        if k in fileds:
            values += f" '{get_str(v)}'"
        else:
            values += f" ''"
        if count != len(fileds):
            values += ","
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


def run(dt):
    resp = requset_index_zz()
    if resp is None:
        return
    print(f"-----------------------------------------------")

    data = parse_response(resp)
    print(f"-----------------------------------------------")

    client.client.execute(f"alter table {TABLE_NAME} drop partition '{dt}'")
    print(f"-----------------------------------------------")

    insert_data_list(data, dt)
    print(f"-----------------------------------------------")

    check_row_num(TABLE_NAME, dt)
    print(f"-----------------------------------------------")


if __name__ == '__main__':
    todate = datetime.now()
    dt = todate.strftime('%Y-%m-%d')
    run(dt)
