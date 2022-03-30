
import requests
import sys

sys.path.append("/work")
sys.path.append("/home/prod/007/fin/spider")

r = requests.get("http://proxy_pool:5010/get")
print(r)