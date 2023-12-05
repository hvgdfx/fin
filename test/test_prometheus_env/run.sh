

docker run --name test-prometheus-env \
  -v prometheus.yml:/opt/bitnami/prometheus/conf/prometheus.yml \
  bitnami/prometheus:2.48.0