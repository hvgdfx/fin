

docker run \
  --web.listen-address=:59080 \
  -v prometheus.yml:/opt/bitnami/prometheus/conf/prometheus.yml \
  bitnami/prometheus:2.48.0