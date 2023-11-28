
name='mykafka'

#docker images | grep ${name} | awk '{print $3}' | xargs docker rmi -f
#docker ps -a | grep ${name} | awk '{print $1}' | xargs docker rm -f
#
#broker1_name="${name}_broker0"
#docker images | grep ${broker1_name} | awk '{print $3}' | xargs docker rmi -f
#docker ps -a | grep ${broker1_name} | awk '{print $1}' | xargs docker rm -f
#broker2_name="${name}_broker1"
#docker images | grep ${broker2_name} | awk '{print $3}' | xargs docker rmi -f
#docker ps -a | grep ${broker2_name} | awk '{print $1}' | xargs docker rm -f
#broker3_name="${name}_broker2"
#docker images | grep ${broker3_name} | awk '{print $3}' | xargs docker rmi -f
#docker ps -a | grep ${broker3_name} | awk '{print $1}' | xargs docker rm -f
#
#
#docker build -t ${broker1_name}:1.0 --no-cache -f ./broker0.Dockerfile .
#docker run -d --name ${broker1_name} --user root --network host ${broker1_name}:1.0
#
#docker build -t ${broker2_name}:1.0 --no-cache -f ./broker1.Dockerfile .
#docker run -d --name ${broker2_name} --user root --network host ${broker2_name}:1.0
#
#docker build -t ${broker3_name}:1.0 --no-cache -f ./broker2.Dockerfile .
#docker run -d --name ${broker3_name} --user root --network host ${broker3_name}:1.0

brokers=("broker0" "broker1" "broker2")

for broker in "${brokers[@]}";
do
  broker_name="${name}_${broker}"
  docker images | grep ${broker_name} | awk '{print $3}' | xargs docker rmi -f
  docker ps -a | grep ${broker_name} | awk '{print $1}' | xargs docker rm -f
  docker build -t ${broker_name}:1.0 --no-cache -f ./${broker}.Dockerfile .
  docker run -d --name ${broker_name} \
                --user root \
                --network host \
                -v /data1/kafka_data/${broker}:/opt/bitnami/kafka/logs/${broker}
                ${broker_name}:1.0
done
