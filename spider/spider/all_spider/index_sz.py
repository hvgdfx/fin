import requests
from fake_useragent import UserAgent

ua = UserAgent()


# 1. request

def requset_index_sz():
    # 1. url
    url = "http://query.sse.com.cn/commonSoaQuery.do?jsonCallBack=jsonpCallback311835&isPagination=false&sqlId=DB_SZZSLB_ZSLB&_=1701760270888"
    # 2. headers

    proxy_json = requests.get("http://stock_proxy:5010/get").json()
    print(f"proxy_json: {proxy_json}")
    if proxy_json["https"]:
        print("没有http代理可用")
        return

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

    # 3. response
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    try_count = 0
    while True:
        try_count += 1
        if try_count > 3:
            break
        if resp.status_code == 200:
            return resp
    return None



# 2. parse data
def parse_response(resp):
    result = {}
    try:
        resp = resp.json()
        result = resp
    except Exception as e:
        print(e)
        return result

    # 正常

    return result


# 3. insert data

def run():
    resp = requset_index_sz()

    if resp is None:
        return
    
    data = parse_response(resp)
    print(list(data.keys()))


if __name__ == '__main__':
    run()
