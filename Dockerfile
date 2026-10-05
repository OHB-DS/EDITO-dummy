FROM nginx:alpine

RUN echo 'EDITO Generic works' > /usr/share/nginx/html/index.html

EXPOSE 80