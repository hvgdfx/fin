



sql="use stock;
      create table IF NOT EXISTS index_eastmoney_board
      (
        indexCode String,
        indexName String,
        baseDate String,
        baseIndex String,
        publishDate String,

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


