


sql=""
sql="${sql}create database IF NOT EXISTS stock;"
sql="${sql}use stock;create table IF NOT EXISTS
          list_stock (
          code String,
          type String,
          market String,
          dt Date
          ) ENGINE = MergeTree()
          PARTITION BY dt order by dt;"

sql="${sql}use stock;
          create table IF NOT EXISTS trade_date
          (
            dt Date,
            is_open String
          ) ENGINE = MergeTree
          order by dt
          primary key dt
          ;
          "

clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#\
  --multiquery -q  "${sql}"
