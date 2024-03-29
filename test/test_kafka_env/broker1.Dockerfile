

FROM bitnami/kafka:2.2.0

USER root

WORKDIR /opt/bitnami/kafka

ADD . ./

RUN alias ll='ls -l' \
    && mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && cp sources.list /etc/apt/sources.list \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
    && apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated vim

CMD ["sh", "./run_broker1.sh"]
