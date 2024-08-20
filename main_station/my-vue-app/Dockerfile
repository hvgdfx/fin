FROM node:18 AS build 

WORKDIR /app

COPY package*.json ./
RUN npm install --registry=https://registry.npmmirror.com

COPY . . /app/
RUN npm run build 

FROM nginx:stable 

COPY --from=build /app/dist /usr/share/nginx/html 

EXPOSE 80 

CMD ["nginx", "-g", "daemon off;"]

