



sql="use stock;
      create table IF NOT EXISTS index_eastmoney_board
      (
        board_type String,
        board_type_cn String,
        board_type_href String,
        board_key String,
        board_id String,
        board_name String,
        board_href String,
        board_order String,

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


