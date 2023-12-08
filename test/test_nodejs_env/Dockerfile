FROM node:21

WORKDIR /home/nodejs/project/demo  

ADD . /home/nodejs/project/demo/

RUN npm init -y \
    && npm install express

CMD ["npm", "server.js"]