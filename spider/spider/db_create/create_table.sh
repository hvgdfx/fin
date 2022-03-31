



sql="create database stock;"


clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123\
   --multiquery -q  "${sql}"
