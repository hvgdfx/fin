
FROM bitnami/prometheus:2.48.0

USER root

#CMD ["sh", "-c", "while true; do sleep 1; done"]

CMD ["sh", "-c", "trap 'exit' INT; while true; do sleep 1; done"]
