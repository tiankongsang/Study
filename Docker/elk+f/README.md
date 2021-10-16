# Docker

## Docker 构建

docker build -t filebeat .  
docker build -t logstash .  
docker build -t elasticsearch .  
docker build -t kibana .

## Docker 运行

docker run -itd -p 80:80 -v /var/log/nginx:/var/log/nginx --name nginx nginx  
docker run -itd --network elk -v /var/log/nginx:/var/log/nginx --name filebeat filebeat  
docker run -itd -p 5044:5044 --network elk -v /opt/logstash/conf:/opt/logstash/conf --name logstash logstash  
docker run -itd -p 9200:9200 -p 9300:9300 --network elk --name elasticsearch -v /var/log/elasticsearch:/var/log/elasticsearch elasticsearch  
docker run -itd -p 5601:5601 --network elk --name kibana kibana

## 添加 Nginx 日志

watch -n 2 curl -k 192.168.168.91
