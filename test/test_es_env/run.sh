

name='elasticsearch'

docker ps -a | grep ${name} | awk '{print $1}' | xargs docker rm -f


docker build -t ${name}:1.0 --no-cache -f ./Dockerfile .
docker run --name ${name} --user root --network host ${name}:1.0
