FROM node:10-alpine

WORKDIR /usr/local/src/service

RUN npm install express
COPY server.js .

WORKDIR /
COPY flag.txt .

EXPOSE 5000
ENTRYPOINT ["node", "/usr/local/src/service/server.js"]
