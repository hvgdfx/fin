

name='test-kafka-env'

docker images | grep ${name} | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep ${name} | awk '{print $1}' | xargs docker rm -f


docker build -t ${name}:1.0 --no-cache -f ./Dockerfile .
docker run -d --name ${name} --user root --network host ${name}:1.0
