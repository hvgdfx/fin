
container_name="test_centos_env"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -itd \
  --name $container_name \
  centos:7