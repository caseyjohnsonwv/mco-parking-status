FROM node:19 AS builder

COPY package.json .
RUN npm i --verbose

COPY . .
RUN npm run build


FROM nginx:stable

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /build /usr/share/nginx/html
