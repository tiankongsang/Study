# Docker

## 系统环境准备

创建文件夹

```shell
mkdir -p /var/log/elasticsearch
chmod -R 777 /var/log/elasticsearch
mkdir -p /opt/logstash/conf
cp ./logstash/conf/logstash-nginx-log.conf /opt/logstash/conf/logstash-nginx-log.conf
```

修改系统参数

```Shell
$ vi /etc/sysctl.conf
vm.max_map_count=655360
$ sysctl -p
$ vi /etc/security/limits.conf
*                soft    nofile          65535
*                hard    nofile          65535
*                hard    nproc           65535
*                soft    nproc           65535
*                hard    memlock         unlimited
*                hard    melock          unlimited
```

创建 Docker 网络

```shell
docker network create elk
```

## Docker 构建

```Shell
cd filebeat
docker build -t filebeat .
cd logstash
docker build -t logstash .
cd elasticsearch
docker build -t elasticsearch .
cd kibana
docker build -t kibana .
```

## 删除全部 Docker 容器

```Shell
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

## Docker 运行

```Shell
docker run -itd -p 80:80 -v /var/log/nginx:/var/log/nginx --name nginx nginx
docker run -itd --network elk -v /var/log/nginx:/var/log/nginx --name filebeat filebeat
docker run -itd -p 5044:5044 --network elk -v /opt/logstash/conf:/opt/logstash/conf --name logstash logstash
docker run -itd -p 9200:9200 -p 9300:9300 --network elk --name elasticsearch -v /var/log/elasticsearch:/var/log/elasticsearch elasticsearch
docker run -itd -p 5601:5601 --network elk --name kibana kibana
```

## 添加 Nginx 日志

```Shell
watch -n 2 curl -k localhost
```
