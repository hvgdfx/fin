
cd /opt/bitnami/kafka

sleep 10

#nohup ./bin/kafka-server-start.sh ./server0.properties > ./logs/broker0/server.log 2>&1 &
./bin/kafka-server-start.sh ./server0.properties

while true;
  do sleep 3600;
  done