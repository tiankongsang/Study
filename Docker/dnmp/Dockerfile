FROM centos:7.2.1511
MAINTAINER liuyueming
RUN yum install -y httpd php php-gd php-mysql
RUN echo "<?php phpinfo()?>" > /var/www/html/index.php
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
