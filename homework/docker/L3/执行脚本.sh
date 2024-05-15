##创建镜像
docker build -f ./Dockerfile -t mynginx ./
docker tag mynginx 192.168.75.128:5000/mynginx:hzytest

##搭建私有仓库
docker pull registry
docker run -d -p 5000:5000 -v /usr/local/registry:/var/lib/registry --restart=always  --name myregistry registry


##增加私有仓库信息到docker网络配置中
echo '{ "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"] ,"insecure-registries":["192.168.75.128:5000"]}' > /etc/docker/daemon.json

##重启docker
systemctl daemon-reload
systemctl restart docker


#验证
docker push 192.168.75.128:5000/mynginx:hzytest
curl http://192.168.75.128:5000/v2/_catalog
docker run -d -p 5004:80 --name mynginx 192.168.75.128:5000/mynginx:hzytest
