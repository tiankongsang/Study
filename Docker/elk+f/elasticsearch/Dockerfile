FROM centos:7.9.2009
MAINTAINER wzlu
RUN yum -y install java-1.8.0-openjdk vim telnet lsof
ADD elasticsearch-6.1.0.tar.gz /usr/local/
RUN cd /usr/local/elasticsearch-6.1.0/config
RUN mkdir -p /data/behavior/log-node1
RUN mkdir /var/log/elasticsearch
COPY elasticsearch.yml /usr/local/elasticsearch-6.1.0/config/
RUN useradd es && chown -R es:es /usr/local/elasticsearch-6.1.0
RUN chmod +x /usr/local/elasticsearch-6.1.0/bin/*
RUN chown -R es:es /var/log/elasticsearch/
RUN chown -R es:es /data/behavior/log-node1
EXPOSE 9200
EXPOSE 9300
CMD su es /usr/local/elasticsearch-6.1.0/bin/elasticsearch

