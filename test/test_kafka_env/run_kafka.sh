
cd /opt/bitnami/kafka

./bin/zookeeper-server-start.sh ./config/zookeeper.properties &

sleep 10

nohup ./bin/kafka-server-start.sh ./server1.properties > ./logs/broker1/server.log 2>&1 &
nohup ./bin/kafka-server-start.sh ./server2.properties > ./logs/broker2/server.log 2>&1 &
nohup ./bin/kafka-server-start.sh ./server3.properties > ./logs/broker3/server.log 2>&1 &

while true;
  do sleep 3600;
  done