FROM nginx:1.23.2
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY koneurakointi.conf /etc/nginx/conf.d/
