FROM zookeeper:3.4

USER root

WORKDIR /zookeeper-3.4.14

ADD . ./

#RUN mv zoo.cfg ./conf/ \
#    && ./bin/zkServer.sh start

CMD ["sh", "-c", "while true; do sleep 1; done"]