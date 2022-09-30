import sys
import requests
import abc
from typing import List

sys.path.append("/work")
sys.path.append("/home/prod/007/fin/spider")

from spider.utils.ck_utils import client
from spider.utils.proxy_utils import get_proxy


class BaseSpider(object):
    def __init__(self, tb_name):
        self.multiprocess = False
        self.tb_name = tb_name
        self.insert_values = ""
        self.request_params = []
        self.url = ""
        self.header = {}
        self.response_result = None

    def schedule(self):
        if self.multiprocess:
            pass
        else:
            for request_param in self.request_params:
                self.schedule_per_request(request_param)

    @abc.abstractmethod
    def get_urls(self) -> List[str]:
        raise NotImplementedError

    def schedule_per_request(self, request_param):
        # 1. parse request_param
        self.parse_request_param(request_param)

    def parse_request_param(self, request_param):
        self.url = request_param
        # self.header = {} # todo

    def spidering(self):
        # 1. 先获取代理地址
        proxy = get_proxy()

        # 2. 获取请求
        try:

            response = requests.get(url=self.url,
                                    headers=self.header,
                                    proxy=proxy) # todo user-agent
            if response:
                if response.status_code == 200:
                    self.response_result = response.json()
                else:
                    print("status code")
            else:
                print("response is None")
        except Exception as e:
            print("")

    @abc.abstractmethod
    def parse_spidered_result(self):
        raise NotImplementedError

    def write_to_db(self):
        values_str = self.insert_values  # todo parse values and 判断values的个数

        # sql = f"insert into {self.tb_name} VALUES ({})"
        # print(sql)
        # client.execute(sql)

