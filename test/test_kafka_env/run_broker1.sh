
cd /opt/bitnami/kafka

alias ll='ls -l'

sleep 10

#nohup ./bin/kafka-server-start.sh ./server1.properties > ./logs/broker1/server.log 2>&1 &
./bin/kafka-server-start.sh ./server1.properties

while true;
  do sleep 3600;
  done