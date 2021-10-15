FROM centos:7.9.2009
MAINTAINER wzlu
RUN yum -y install java-1.8.0-openjdk vim telnet lsof
ADD logstash-6.1.0.tar.gz /usr/local/
RUN cd /usr/local/logstash-6.1.0
ADD run.sh /run.sh
RUN chmod 755 /*.sh
EXPOSE 5044
CMD ["/run.sh"]
