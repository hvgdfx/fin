import platform

os_name = platform.system()

proxies = {}

if "Windows" == os_name:
    proxy_host = "127.0.0.1"
    proxy_port = 7897

    proxies = {
        "http": f"http://{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_host}:{proxy_port}",
    }
