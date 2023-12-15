



sql="use stock;
create table IF NOT EXISTS index_zz_element
(
  date String,
  indexCode String,
  indexName String,
  indexNameEn String,
  securityCode String,
  securityName String,
  securityNameEn String,
  marketSource String,
  marketSourceEn String,
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

