
container_name="proxy_redis"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -itd \
  --name $container_name \
  -v /home/prod/007/fin/redis-server/redis.conf:/etc/redis/redis.conf \
  redis