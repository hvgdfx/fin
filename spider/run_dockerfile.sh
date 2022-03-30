
container_name="spider"

docker ps -a  | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker build -t ${container_name}:1.0 .
docker run -it \
  --name ${container_name} \
  --net host \
  --network host \
  ${container_name}:1.0 \


  #--network-alias ${container_name} \
