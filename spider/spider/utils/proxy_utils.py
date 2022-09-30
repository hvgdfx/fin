import requests


def get_proxy():
    proxy = ""
    try:
        response = requests.get("http://localhost:5010/get")
        if response:
            if response.status_code == 200:
                proxy = response.json()["proxy"]
            else:
                print("proxy status code is not 200")
        else:
            print("proxy response is None")
    except Exception as e:
        print(e)
    return proxy


if __name__ == '__main__':
    r = get_proxy()
    print(r)
