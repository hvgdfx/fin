FROM ubuntu:20.04

# 设置非交互模式
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的软件包
RUN apt-get update && \
    apt-get install -y build-essential git cmake ninja-build zlib1g-dev libsecp256k1-dev libmicrohttpd-dev libsodium-dev

# 安装 tzdata 并配置时区
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apt-get install -y tzdata && \
    dpkg-reconfigure --frontend noninteractive tzdata

WORKDIR /root/ton
RUN git clone https://github.com/ton-blockchain/ton.git

# 下载和放置第三方库
WORKDIR /root/ton/third-party
RUN git clone https://github.com/abseil/abseil-cpp.git && \
    git clone https://github.com/google/crc32c.git && \
    git clone https://github.com/facebook/rocksdb.git

# 下载和构建 blst
WORKDIR /root/ton/third-party
RUN git clone https://github.com/supranational/blst.git && \
    cd blst && \
    ./build.sh

# 构建项目
RUN mkdir build && \
    cd build && \
    cmake .. && \
    make

WORKDIR /root/ton/build

COPY config.json /root/ton/build/config.json

# CMD ["./ton_node", "--config", "config.json"]
CMD ["sh", "-c", "while true; do sleep 1; done"]
