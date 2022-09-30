
container_name="spider"

docker ps -a  | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker build -t ${container_name}:1.0 -f Dockerfile .
docker run -it \
  --name ${container_name} \
  --network host \
  ${container_name}:1.0 \


  #--network-alias ${container_name} \
