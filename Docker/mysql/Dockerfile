FROM centos:6
LABEL org.opencontainers.image.authors="tiankongsang@outlook.com"
# 配置 CentOS Yum 源
RUN sed -i "s|enabled=1|enabled=0|g" /etc/yum/pluginconf.d/fastestmirror.conf && \
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak && \
curl -o /etc/yum.repos.d/CentOS-Base.repo https://www.xmpan.com/Centos-6-Vault-Aliyun.repo && \
yum clean all && yum makecache
# 安装 MySQL && 初始化 MySQL
RUN yum install -y mysql mysql-devel mysql-server
RUN /etc/init.d/mysqld start && \
mysql -e "grant all privileges on *.* to 'root'@'%' identified by '123456';" && \
mysql -e "grant all privileges on *.* to 'root'@'localhost' identified by '123456';"
EXPOSE 3306
CMD ["mysqld_safe"]