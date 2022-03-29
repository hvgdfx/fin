


container_name="anaconda3"

docker ps -a  | grep $container_name | awk '{print $1}' | xargs docker rm -f

docker run -it --name ${container_name} --network fin-network --network-alias ${container_name} continuumio/anaconda3
