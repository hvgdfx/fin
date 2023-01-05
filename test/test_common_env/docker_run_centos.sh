
container_name="test_centos_env"

docker images | grep $container_name | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f


docker build -t $container_name:1.0 --no-cache -f ./Dockerfile .
docker run --name $container_name --user root --network host $container_name:1.0

