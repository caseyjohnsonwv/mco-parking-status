FROM node:19

COPY package.json .
RUN npm i --verbose

ENV NODE_ENV=production

COPY *.ts *.js *.json ./
COPY src/ /src/
COPY /static /static/
RUN npm run build

ENV HOST="0.0.0.0"
ENV PORT="80"
EXPOSE 80

ENTRYPOINT [ "node", "build" ]
