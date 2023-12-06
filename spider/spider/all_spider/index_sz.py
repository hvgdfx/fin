import requests
from fake_useragent import UserAgent
from tqdm import tqdm
import time

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
        url = f"http://query.sse.com.cn/commonSoaQuery.do?jsonCallBack={jsonCallBack}&isPagination={isPagination}&sqlId={sqlId}&_={_}"

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
        resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=(1, 10))
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
            data = resp.text
        except Exception as e:
            print(e)
            print(f"parse response {data}")
    return data


def check_data(resp) -> bool:
    return False


def parse_data(resp):
    pass


# 3. insert data
def insert_data(data):
    pass


def run():
    resp = requset_index_sz()
    if resp is None:
        return
    print(f"-----------------------------------------------")

    data = parse_response(resp)
    print(type(data))
    print(f"-----------------------------------------------")
    print(list(data.keys()))


if __name__ == '__main__':
    run()
