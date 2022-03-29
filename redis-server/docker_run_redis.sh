
docker ps -a | grep redis-proxy | awk '{print $1}' | xargs docker rm -f
docker run -itd --name redis-proxy -p 6379:6379 redis --requirepass 123456