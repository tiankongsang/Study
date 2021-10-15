nohup consul agent -server -bootstrap -ui -data-dir=/var/lib/consul-data -bind=192.168.73.129 -client=0.0.0.0 -node=consul-server01 &>/var/log/consul.log &
nohup consul-template -consul-addr 192.168.3.129:8500 -template "/root/consul/nginx.ctmpl:/usr/local/nginx/conf/vhost/kgc.conf:/usr/local/nginx -s reload" --log-level=info &>/var/log/consul.log &
