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
    && apt-get install -y --no-install-recommends --allow-unauthenticated procps \
    && mv zoo.cfg ./conf/

    #&& /zookeeper-3.4.14/bin/zkServer.sh start /zookeeper-3.4.14/conf/zoo.cfg

#CMD ["./bin/zkServer.sh", "start", "./conf/zoo.cfg"]
#CMD ["sh", "-c", "while true; do sleep 1; done"]
CMD ["sh", "./run_zk.sh"]
