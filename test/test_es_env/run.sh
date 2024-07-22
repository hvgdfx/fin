
# 认证可以去github官网看下，有详细步骤

docker network create es

docker images | grep my-es | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep my-es | awk '{print $1}' | xargs docker rm -f
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.0
docker run -d --name my-es --net es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t elasticsearch:8.11.0


docker images | grep my-kibana | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep my-kibana | awk '{print $1}' | xargs docker rm -f
docker pull docker.elastic.co/kibana/kibana:8.11.0
docker run -d --name my-kibana --net es -p 5601:5601 docker.elastic.co/kibana/kibana:8.11.0



