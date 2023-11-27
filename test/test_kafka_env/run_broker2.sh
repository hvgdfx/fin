
cd /opt/bitnami/kafka

sleep 10

#nohup ./bin/kafka-server-start.sh ./server1.properties > ./logs/broker2/server.log 2>&1 &
./bin/kafka-server-start.sh ./server2.properties

while true;
  do sleep 3600;
  done