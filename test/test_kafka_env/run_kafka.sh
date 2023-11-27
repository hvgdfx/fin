
cd /opt/bitnami/kafka

./bin/zookeeper-server-start.sh ./config/zookeeper.properties &

sleep 10

./bin/kafka-server-start.sh ./server.properties
