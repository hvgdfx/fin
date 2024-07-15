

name='my-es'

docker network create es


docker images | grep ${name} | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep ${name} | awk '{print $1}' | xargs docker rm -f
docker run -d --name ${name} --network es \
    -e "discovery.type=single-node" \
	-p 9200:9200 \
	-e xpack.security.enabled=false \
	-e xpack.security.enrollment.enabled=false \
	elasticsearch:8.14.3