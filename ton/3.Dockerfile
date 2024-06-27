FROM ubuntu:20.04

# RUN   sudo apt-get update && \
#   sudo apt-get install -y build-essential git cmake ninja-build zlib1g-dev libsecp256k1-dev libmicrohttpd-dev libsodium-dev && \
#   wget https://apt.llvm.org/llvm.sh && \
#   chmod +x llvm.sh && \
#   ./llvm.sh 16 all && \
#   cp assembly/native/build-ubuntu-shared.sh . && \
#   chmod +x build-ubuntu-shared.sh

# CMD  ["./build-ubuntu-shared.sh"]  
CMD ["sh", "-c", "while true; do sleep 1; done"]



