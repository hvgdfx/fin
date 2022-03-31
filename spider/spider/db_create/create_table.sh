


sql=""
sql="${sql}create database stock;"
sql="${sql}use stock;create table stock_list (code string, name string);"


clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123\
   --multiquery -q  "${sql}"
