
FROM ubuntu:20.04

WORKDIR /work

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y npm

RUN npm install -g cnpm --registry=https://registry.npmmirror.com
RUN cnpm install vue-cli -g
#RUN cnpm install vue -g
RUN cnpm install webpack -g


RUN vue init webpack my_project
RUN cd my_project
