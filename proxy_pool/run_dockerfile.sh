

docker images | grep proxy_pool | awk '{print $3}' | xargs docker rmi

docker build -t proxy_pool:1.0 .

docker run -it --name proxy_pool --network fin-network proxy_pool:1.0