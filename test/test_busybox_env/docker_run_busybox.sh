
container_name="test_busybox_env"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker run -it \
  --name $container_name \
  --add-host host.docker.internal:172.17.0.1 \
  busybox
