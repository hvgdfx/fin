# import baostock as bs
import sys, os
import argparse

sys.path.append("/work")
sys.path.append("/data/wuchang/fin/spider")

from spider.utils.ck_utils import client


def get_all_trade_date():
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    #### 获取交易日信息 ####
    rs = bs.query_trade_dates(start_date="1990-01-01", end_date="2022-12-31")
    print('query_trade_dates respond error_code:' + rs.error_code)
    print('query_trade_dates respond  error_msg:' + rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

    #### 结果集输出到csv文件 ####
    file_path = "./all_trade_data.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            for pair in data_list:
                f.write(f"{pair[0]},{pair[1]}")
                f.write("\n")

    #### 登出系统 ####
    bs.logout()


def insert_all_trade_date(dt):
    # file_path = "./all_trade_data.txt"
    file_path = f"./tradeDate_{dt}.csv"
    if os.path.exists(file_path):
        pass
    else:
        print(f"file not exists. {file_path}")
        return
    with open(file_path) as f:
        for line in f.readlines():
            splits = line.replace("\n", "").split(",")
            dt = splits[0]
            isOpen = splits[1]
            client.client.execute(f"insert into stock.trade_date VALUES ('{dt}', '{isOpen}')")
            print(f"{dt},{isOpen}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="通过日期来上传交易日期")
    parser.add_argument("dt", type=str, help="交易日期的年份，比如2023")

    args = parser.parse_args()

    insert_all_trade_date(args.dt)
