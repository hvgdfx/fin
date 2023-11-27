FROM zookeeper:3.4

USER root

WORKDIR /zookeeper-3.4.14

ADD . ./

RUN alias ll='ls -l' \
    && mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && cp sources.list /etc/apt/sources.list \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
    && apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated vim \
    && mv zoo.cfg ./conf/ \
    && ./bin/zkServer.sh start ./conf/zoo.cfg

CMD ["sh", "-c", "while true; do sleep 1; done"]