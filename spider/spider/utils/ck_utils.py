from clickhouse_driver import Client
import sys

sys.path.append("/work")
sys.path.append("/home/prod/007/fin/spider")

from spider.utils.test_utils import is_test_enviroment


class CKClient:
    def __init__(self):
        self.username = "default"
        self.passwd = "click!@#123"

        host_ip = "127.0.0.1" if is_test_enviroment else "localhost"
        self.client = Client(host=host_ip, port=9000, user=self.username, password=self.passwd)


client = CKClient()

if __name__ == '__main__':
    client = CKClient()
