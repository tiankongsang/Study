FROM centos:7.9.2009
RUN yum -y install java-1.8.0-openjdk vim telnet lsof
ADD kibana-6.1.0-linux-x86_64.tar.gz /usr/local/
RUN cd /usr/local/kibana-6.1.0-linux-x86_64
COPY kibana.yml /usr/local/kibana-6.1.0-linux-x86_64/config/
EXPOSE 5601
CMD ["/usr/local/kibana-6.1.0-linux-x86_64/bin/kibana"]
