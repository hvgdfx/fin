

FROM bitnami/kafka:2.2.0

USER root

WORKDIR /opt/bitnami/kafka

ADD server.properties ./config
ADD sources.list ./

RUN alias ll='ls -l' \
    && mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && cp sources.list /etc/apt/sources.list \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends vim


CMD ["sh", "-c", "while true; do sleep 1; done"]
