FROM centos:7.2.1511
MAINTAINER liuyueming
RUN yum install -y httpd php php-gd php-mysql
RUN echo "<?php phpinfo()?>" > /var/www/html/index.php
EXPOSE 80
EXPOSE 443
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
