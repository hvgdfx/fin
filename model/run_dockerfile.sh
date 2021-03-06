
container_name="tf2"

docker ps -a  | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker build -t ${container_name}:1.0 .
docker run -it --name ${container_name} --network fin-network --network-alias ${container_name} ${container_name}:1.0
