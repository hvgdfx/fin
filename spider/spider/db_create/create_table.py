import sys

sys.path.append("/work")
sys.path.append("/home/prod/007/fin/spider")

from spider.utils.ck_utils import client


def create_stock_db():
    try:
        client.execute("create database stock")
        return True
    except Exception as e:
        print(e)
        return False


def create_stock_list_table():
    try:
        client.client.execute("create table ")
        return True
    except Exception as e:
        print(e)
        return False


def create_index_list_gz_table():
    pass


if __name__ == '__main__':
    result = create_stock_db()
    print(result)
