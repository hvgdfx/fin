import sys

sys.path.append("../../")

import requests
import time
import json
from fake_useragent import UserAgent
from spider.utils.ck_utils import client
from datetime import datetime
import xlrd
import os


ua = UserAgent()

xls_dir_path = "/work/spider/all_spider/data/"

# 1. request
def requset_index_zz_element(index_code):
    try_count = 0
    while True:
        # 1. url
        url = f"https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/{index_code}cons.xls"

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
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate,br",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
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
def parse_response(resp, index_code):
    if resp is None:
        return False
    else:
        try:
            os.makedirs(xls_dir_path, exist_ok=True)
            with open(f"{xls_dir_path}index_zz_element_{index_code}.xls", "wb") as f:
                f.write(resp.content)
            return True
        except Exception as e:
            print(e)
            return False


# 3. insert data
def insert_data_list(index_code, dt):
    values_list = insert_data(index_code)
    for values in values_list:
        sql = f"insert into stock.index_zz_element VALUES ({values}, '{dt}')"
        print(sql)
        # client.client.execute(sql)


def insert_data(index_code):
    workbook = xlrd.open_workbook(f"{xls_dir_path}index_zz_element_{index_code}.xls")
    sheet = workbook.sheet_by_name(f"{index_code}cons.xls")

    values_list = []

    for row_index in range(sheet.nrows):
        row_data = sheet.row_values(row_index)
        if row_index == 0:
            pass
        else:
            count = 0
            values = ""
            for row_value in row_data:
                count += 1
                values += f" '{get_str(row_value)}'"
                if count != len(row_data):
                    values += ","
            values_list.append(values)
    return values_list


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

def get_index_list(dt):
    result = client.client.execute(f"select indexCode from stock.index_zz where indexCode != '' and dt='{dt}';")
    result = [t[0] for t in result]
    return result


def run(index_code, dt):
    resp = requset_index_zz_element(index_code)
    if resp is None:
        return
    #print(f"-----------------------------------------------")

    flag = parse_response(resp, index_code)
    #print(f"-----------------------------------------------")

    if flag:
        insert_data_list(index_code, dt)
    else:
        print(f"{index_code} 没有该指数的明细xls")
    #print(f"-----------------------------------------------")

def run_all():
    todate = datetime.now()
    dt = todate.strftime('%Y-%m-%d')

    index_list = get_index_list(dt)
    for index_code in index_list:
        try:
            run(index_code, dt)
            print(f"index_code: {index_code} success")
        except Exception as e:
            print(f"index_code: {index_code} fail {e}")


if __name__ == '__main__':
    # run("000300", "2023-12-15")
    run_all()
