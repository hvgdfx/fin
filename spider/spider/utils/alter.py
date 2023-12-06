import requests
import json


def send_message(text):
    try:
        data1 = {}
        data1["msgtype"] = "text"
        data1["at"]: {"isAtAll": True}
        data1["text"] = {"content": text}
        url = "https://oapi.dingtalk.com/robot/send?access_token=767e3d391fd9a07641f0c2d2f93dad0f3f90a8a1c0c77d4aef3ed92adb6953a8"

        resp = requests.post(url,
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(data1).encode('utf-8'))

        if resp.status_code == 200:
            print(f"alter success " + resp.text)
        else:
            print(f"alter failed {resp.status_code}")
    except Exception as e:
        print(f"send_massage went wrong! {e}")


def send_message2(text):
    try:
        data1 = {}
        data1["msgtype"] = "text"
        data1["at"]: {"isAtAll": True}
        data1["text"] = {"content": "warning " + text}
        url = "https://oapi.dingtalk.com/robot/send?access_token=767e3d391fd9a07641f0c2d2f93dad0f3f90a8a1c0c77d4aef3ed92adb6953a8"

        import urllib
        request = urllib.request.Request(url, headers={'Content-Type': 'application/json'},
                                         data=json.dumps(data1).encode('utf-8'))

        with urllib.request.urlopen(request, timeout=1) as response:
            response_data = json.loads(response.read())
        return response_data
    except Exception as e:
        print(f"send_massage went wrong! {e}")
        return


if __name__ == '__main__':
    text = "爬虫来了"
    send_message(text)
