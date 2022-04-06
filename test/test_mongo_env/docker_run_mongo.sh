
container_name="test_mongo_env"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -it \
  --name $container_name \
  mongo 