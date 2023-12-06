
container_name="stock_proxy_redis"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -itd \
  --name $container_name \
  --net host \
  -v /home/prod/007/fin/redis-server/redis.conf:/etc/redis/redis.conf \
  -d redis redis-server /etc/redis/redis.conf