import requests
import socks
import socket
import platform

TOKEN = "6955121712:AAHug7zbealQl4O1v4Milcrr6JQJKKTQ4rs"
# 设置 Clash Verge 代理服务器地址和端口号
proxy_host = "127.0.0.1"
proxy_port = 7897  # 假设 Clash Verge 使用的是 SOCKS5 代理，端口号为 7890

# 构建代理配置
# proxies = {
#     'http': f'socks5://{proxy_host}:{proxy_port}',
#     'https': f'socks5://{proxy_host}:{proxy_port}'
# }

proxies = {
    "http": f"http://{proxy_host}:{proxy_port}",
    "https": f"http://{proxy_host}:{proxy_port}",
}

proxies = {}

# # 配置 PySocks 库使用本地 SOCKS5 代理
# socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)

# # 安装 PySocks 代理
# socket.socket = socks.socksocket


def run():
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    url2 = "http://www.baidu.com"
    response = requests.get(url2, proxies=proxies)
    print(response.text)


def run2():
    url = "http://www.facebook.com"
    response = requests.get(url, proxies=proxies)
    print(response.text)


if "__main__" == "__main__":
    run()
