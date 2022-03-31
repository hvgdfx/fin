


sql=""
sql="${sql}create database IF NOT EXISTS stock;"
sql="${sql}use stock;create table IF NOT EXISTS stock_list (code string, name string) ENGINE = MergeTree;"


clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123\
   --multiquery -q  "${sql}"
