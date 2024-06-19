
# FROM nginx:stable
FROM ccr.ccs.tencentyun.com/library/nginx:latest

add nginx.conf ./

CMD ["/usr/sbin/nginx", "-c", "/nginx.conf", "-g", "daemon off;"]

#CMD ["nginx", "-s", "reload"]

#CMD ["sh", "-c", "while true; do sleep 1; done"]