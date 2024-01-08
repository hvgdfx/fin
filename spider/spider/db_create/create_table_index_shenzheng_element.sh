



sql="use stock;
      create table IF NOT EXISTS index_shenzheng_element
      (
        indexCode String,
        securityCode String,
        securityName String,
        totalShareCapital String,
        negotiableCapital String,
        industry String,
        computeTag String,

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


