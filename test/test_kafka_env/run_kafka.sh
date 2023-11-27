
cd /opt/bitnami/kafka

./bin/zookeeper-server-start.sh ./config/zookeeper.properties &

sleep 10

./bin/kafka-server-start.sh ./server1.properties &
./bin/kafka-server-start.sh ./server2.properties &
./bin/kafka-server-start.sh ./server3.properties &
