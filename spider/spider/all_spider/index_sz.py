import requests
from fake_useragent import UserAgent

ua = UserAgent()

# 1. request

def requset_index_sz():
    # 1. url
    url = "http://query.sse.com.cn/commonSoaQuery.do?jsonCallBack=jsonpCallback311835&isPagination=false&sqlId=DB_SZZSLB_ZSLB&_=1701760270888"
    # 2. headers

    proxy_json = requests.get("http://stock_proxy:5010/get").json()
    if proxy_json["https"]:
        print("没有http代理可用")
        return
    proxies = {
        "http": proxy_json["proxys"]
    }

    headers = {
        "user-agent": ua.random,
        "proxies": proxies
    }
    print(f"headers: {headers}")
    
    # 3. response
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        return resp


# 2. parse data

# 3. insert data

def run():
    resp = requset_index_sz()
    print(resp.json())


if __name__ == '__main__':
    run()
