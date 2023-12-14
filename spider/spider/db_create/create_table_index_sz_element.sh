



sql="use stock;
create table IF NOT EXISTS index_sz_element
(
  indexCode String,
  securityAbbrEn String,
  securityAbbr String,
  inDate String,
  securityCode String,
  marketSource String,
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

