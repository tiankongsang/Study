FROM centos:7.2.1511
LABEL org.opencontainers.image.authors="tiankongsang@outlook.com"
RUN yum install -y wget proc-devel net-tools gcc zlib zlib-devel make openssl-devel
RUN wget http://nginx.org/download/nginx-1.9.7.tar.gz
RUN tar zxf nginx-1.9.7.tar.gz
WORKDIR nginx-1.9.7
RUN ./configure --prefix=/usr/local/nginx && make && make install
RUN echo "daemon off;" >> /usr/local/nginx/conf/nginx.conf
WORKDIR /root/nginx
ADD run.sh /run.sh
RUN chmod 776 /run.sh
EXPOSE 80
EXPOSE 443
CMD ["/run.sh"]