FROM node:21

RUN mkdir -p /home/nodejs/demoproject1

ADD ./ /home/nodejs/demoproject1

WORKDIR /home/nodejs/demoproject1

RUN npm install

ENV HOST 0.0.0.0
ENV PORT 8081

EXPOSE 80

CMD ["npm", "start"]