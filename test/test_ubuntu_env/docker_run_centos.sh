
container_name="test_ubuntu_env"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -it \
  --name $container_name \
  ubuntu:20.04