




docker network create es

docker run -d --name elasticsearch --network es -e "discovery.type=single-node" -p 9200:9200 elasticsearch:8.14.3

docker run -d --name kibana --network es -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://localhost:9200 kibana



docker network create es

docker run -d --name elasticsearch --network es \
    -e "discovery.type=single-node" \
	-p 9200:9200 \
	-e xpack.security.enabled=false \
	-e xpack.security.enrollment.enabled=true \
	-e xpack.security.http.ssl.enabled=false \
	elasticsearch:8.14.3

docker run -d --name kibana --network es \
    -p 5601:5601 \
	-e ELASTICSEARCH_HOSTS=http://localhost:9200 \
	-e ELASTICSEARCH_USERNAME=admin \
	-e ELASTICSEARCH_PASSWORD=admin \
	kibana:8.14.3


curl -X PUT "http://localhost:9200/test123"
curl -X GET "http://10.96.17.132:9200/test123/_mapping"




