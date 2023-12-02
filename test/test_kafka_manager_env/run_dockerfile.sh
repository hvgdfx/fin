
name="my-kafka-manager"

docker run -it --rm  -p 59000:9000 -e ZK_HOSTS="127.0.0.1:2181" \
               -e APPLICATION_SECRET=letmein sheepkiller/kafka-manager:stable
