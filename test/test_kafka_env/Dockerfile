

FROM bitnami/kafka:2.2.0

USER root

WORKDIR /opt/bitnami/kafka

ADD server.properties ./config
ADD sources.list ./

RUN alias ll='ls -l' \
    && mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && cp sources.list /etc/apt/sources.list
#    && DEBIAN_FRONTEND=noninteractive apt-get update


CMD ["sh", "-c", "while true; do sleep 1; done"]
