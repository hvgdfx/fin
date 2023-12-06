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
        url = f"https://query.sse.com.cn/commonSoaQuery.do?&sqlId=DB_SZZSLB_CFGLB&indexCode=000001&isPagination=true&pageHelp.pageSize=60&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.pageNo=1&pageHelp.endPage=1&_=1701861121120"

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
            data = resp.json()["pageHelp"]
        except Exception as e:
            print(e)
            print(f"parse response {data}")
    return data


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
