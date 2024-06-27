FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y build-essential cmake git libssl-dev zlib1g-dev

WORKDIR /root

RUN git clone https://github.com/ton-blockchain/ton.git && \
    cd ton && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make

WORKDIR /root/ton/build

COPY config.json /root/ton/build/config.json

CMD ["./ton_node", "--config", "config.json"]
