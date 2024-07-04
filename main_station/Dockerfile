FROM ccr.ccs.tencentyun.com/library/node:14 as vue-build

WORKDIR /tmp

ADD . /tmp

RUN npm build serve 

# FROM nginx:stable
# FROM ccr.ccs.tencentyun.com/library/nginx:latest

# add nginx.conf /etc/nginx/conf.d/https.conf
# add big.html /usr/share/nginx/html/big.html
# add ./dist/* /usr/share/nginx/html

# CMD ["/usr/sbin/nginx", "-c", "/nginx.conf", "-g", "daemon off;"]
# CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

#CMD ["nginx", "-s", "reload"]

CMD ["sh", "-c", "while true; do sleep 1; done"]