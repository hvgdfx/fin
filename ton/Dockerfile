FROM ubuntu:20.04

# 设置非交互模式
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的软件包并配置时区
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
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
