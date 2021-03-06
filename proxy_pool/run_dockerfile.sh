
container_name="proxy_pool"

docker images | grep $container_name | awk '{print $3}' | xargs docker rmi
docker ps -a  | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker build -t ${container_name}:1.0 .

docker run -itd \
  --name ${container_name} \
  --network host \
  --hostname $container_name \
  ${container_name}:1.0



