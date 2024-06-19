

docker pull ccr.ccs.tencentyun.com/library/nginx:latest
name='dalinghua-nginx'

docker images | grep ${name} | awk '{print $3}' | xargs docker rmi -f
docker ps -a | grep ${name} | awk '{print $1}' | xargs docker rm -f


docker build -t ${name}:1.0 --no-cache -f ./Dockerfile .
docker run -d --name ${name} \
    -p 443:443 \
    -v /data/wuchang/dalinghua.cn.key:/etc/nginx/certs/dalinghua.cn.key \
    -v /data/wuchang/dalinghua.cn.pem:/etc/nginx/certs/dalinghua.cn.pem \
    --user root \
    --network host ${name}:1.0
