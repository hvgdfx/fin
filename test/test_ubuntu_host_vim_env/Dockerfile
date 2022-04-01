
FROM ubuntu:20.04

WORKDIR /work

RUN apt-get update
RUN apt-get install vim
RUN apt-get install npm

RUN npm install -g cnpm --registry=https://registry.npmmirror.com
RUN cnpm install vue-cli
RUN cnpm install vue -g
RUN cnpm install webpack -g