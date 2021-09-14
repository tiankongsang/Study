FROM centos:7.2.1511
LABEL org.opencontainers.image.authors="tiankongsang@outlook.com"
RUN yum install -y proc-devel net-tools gcc zlib zlib-devel make openssl-devel
RUN cd /tmp && curl -o nginx-1.12.1.tar.gz http://nginx.org/download/nginx-1.12.1.tar.gz && \
    tar -zxvf nginx-1.12.1.tar.gz && cd nginx-1.12.1 && \
    ./configure --prefix=/usr/local/nginx && make -j 2 && make install
RUN echo "daemon off;" >> /usr/local/nginx/conf/nginx.conf
WORKDIR /root/nginx
ADD run.sh /run.sh
RUN chmod 776 /run.sh
EXPOSE 80
EXPOSE 443
CMD ["/run.sh"]