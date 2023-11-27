

FROM bitnami/kafka:2.2.0

WORKDIR /opt/bitnami/kafka

ADD server.properties ./config

RUN alias ll='ls -l'

CMD ["sh", "-c", "while true; do sleep 1; done"]
