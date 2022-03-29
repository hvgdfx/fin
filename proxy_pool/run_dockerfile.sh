

docker build -t proxy_pool:1.0 .

docker run -it --name proxy_pool --network fin-network proxy_pool:1.0