
container_name="test_nodejs_env"

# delete container
docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f

# build image
docker build -t ${container_name}:1.0 .

docker run -it \
  --name $container_name \
  --network host \
  ${container_name}:1.0