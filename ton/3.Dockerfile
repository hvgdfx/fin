FROM ubuntu:20.04

RUN   sudo apt-get update && \
  sudo apt-get install -y build-essential git cmake ninja-build zlib1g-dev libsecp256k1-dev libmicrohttpd-dev libsodium-dev wget lsb-release software-properties-common pkg-config && \
  wget https://apt.llvm.org/llvm.sh && \
  chmod +x llvm.sh && \
  ./llvm.sh 16 all

WORKDIR /root/ton
RUN git clone https://github.com/ton-blockchain/ton.git

WORKDIR /root/ton/third-party
RUN git clone https://github.com/abseil/abseil-cpp.git && \
    git clone https://github.com/google/crc32c.git && \
    git clone https://github.com/facebook/rocksdb.git

WORKDIR /root/ton
RUN cp assembly/native/build-ubuntu-shared.sh . && \
  chmod +x build-ubuntu-shared.sh

# CMD  ["./build-ubuntu-shared.sh"]  
CMD ["sh", "-c", "while true; do sleep 1; done"]



