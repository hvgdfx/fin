from spider.spider.utils.ck_utils import client


def create_stock_list_table():
    try:
        client.execute("create table ")
        return True
    except Exception as e:
        print(e)
        return False


def create_index_list_gz_table():
    pass
