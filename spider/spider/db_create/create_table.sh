


sql=""
sql="${sql}create database IF NOT EXISTS stock;"
#sql="${sql}use stock;create table IF NOT EXISTS
#          stock_list (
#          code String,
#          name String,
#          dt String
#          ) ENGINE = MergeTree
#          PARTITION BY dt;"

sql="${sql}use stock;create table IF NOT EXISTS
          trade_date (
          dt String,
          isOpen String,
          dt String
          ) ENGINE = MergeTree
          PARTITION BY dt;"

clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123\
  --multiquery -q  "${sql}"
