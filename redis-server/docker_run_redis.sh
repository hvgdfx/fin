
container_name="proxy_redis"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -itd \
  --name $container_name \
  --network host \
  --network-alias $container_name \
  --requirepass 123456 \
  redis