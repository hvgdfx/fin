from spider.utils.alter import send_message
from spider.utils.ck_utils import client


def check_row_num(table, dt):
    sql = f"select count(*) from stock.{table} where dt = '{dt}' "
    print(sql)
    result = client.client.execute(sql)
    print(f"result: {result}") # result: [(0,)]
    count = result[0][0]
    send_message(f"[SPIDER] {table} {dt} {count}")


if __name__ == '__main__':
    check_row_num("index_eastmoney_board_element", "2024-04-16")
