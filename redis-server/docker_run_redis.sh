
docker ps -a | grep redis-proxy | awk '{print $1}' | xargs docker rm -f
docker run -itd --name redis-proxy redis --requirepass 123456