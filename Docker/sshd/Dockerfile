FROM centos:7.2.1511
LABEL org.opencontainers.image.authors="tiankongsang@outlook.com"
RUN yum install -y net-tools openssh-server openssh-clients lsof telnet
RUN mkdir -p /var/run/sshd
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN /bin/echo 'root:000000' |chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
