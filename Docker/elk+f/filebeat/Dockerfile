FROM centos:7.9.2009
RUN yum -y install java-1.8.0-openjdk vim telnet lsof
ADD filebeat-6.1.0-linux-x86_64.tar.gz /usr/local/
RUN cd /usr/local/filebeat-6.1.0-linux-x86_64
COPY filebeat.yml /usr/local/filebeat-6.1.0-linux-x86_64
ADD run.sh /run.sh
RUN chmod 755 /*.sh
CMD ["/run.sh"]
