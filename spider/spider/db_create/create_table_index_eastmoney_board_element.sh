



sql="use stock;
      create table IF NOT EXISTS index_eastmoney_board_element
      (
        board_id String,
        board_name String,
        securityCode String,
        securityName String,

        dt String
      ) ENGINE = MergeTree
        PARTITION BY dt order by dt;
    "

clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123 \
  --multiquery -q  "${sql}"


