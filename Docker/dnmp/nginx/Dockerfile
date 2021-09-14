FROM centos:6
LABEL org.opencontainers.image.authors="tiankongsang@outlook.com"
# 配置 CentOS Yum 源
RUN sed -i "s|enabled=1|enabled=0|g" /etc/yum/pluginconf.d/fastestmirror.conf && \
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak && \
    curl -o /etc/yum.repos.d/CentOS-Base.repo https://www.xmpan.com/Centos-6-Vault-Aliyun.repo && \
    yum clean all && yum makecache
RUN yum install -y gcc gcc-c++ make openssl-devel pcre-devel
RUN cd /tmp && curl -o nginx-1.12.1.tar.gz http://nginx.org/download/nginx-1.12.1.tar.gz && \
    tar -zxvf nginx-1.12.1.tar.gz && cd nginx-1.12.1 && \
    ./configure --prefix=/usr/local/nginx && make -j 2 && make install
RUN rm -f /usr/local/nginx/conf/nginx.conf
COPY nginx.conf /usr/local/nginx/conf
EXPOSE 80
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
