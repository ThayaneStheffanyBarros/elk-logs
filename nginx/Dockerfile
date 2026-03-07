FROM nginx:latest

RUN rm /var/log/nginx/access.log
RUN rm /var/log/nginx/error.log

CMD ["nginx", "-g", "daemon off;"]