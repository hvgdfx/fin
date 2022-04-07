# 用来调度所有任务
import os
from spider.spider.db_create.trade_date import get_all_trade_date


def run():
    # 创建各种表
    create_all_table()

    # 插入交易日


def create_all_table():
    os.system("/bin/bash /work/spider/db_create/create_table.sh")


if __name__ == '__main__':
    run()
