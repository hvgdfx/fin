from spider.utils.alter import send_message
from spider.utils.ck_utils import client


def check_row_num(table, dt):
    sql = f"select count(*) from stock.{table} where dt = '{dt}' "
    print(sql)
    result = client.client.execute(sql)
    print(f"result: {result}")
    # send_message()


if __name__ == '__main__':
    check_row_num("index_eastmoney_board_element", "2024-04-16")
