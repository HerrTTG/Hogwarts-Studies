##Linux 系统:
##下载docker-compose文件
curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

##增加权限
chmod +x docker-compose

##软连接到/usr/bin/
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

#测试
docker-compose --version


mkdir /home/test

vi /docker-compose.yml

##-f可以指定yml文件
docker-compose -f /home/test/docker-compose.yml up -d

##Docker-compose 常用命令
##查看配置：
# docker-compose config
##创建容器：
#docker-compose up -d
##停止并删除容器：
# docker-compose down

##构建镜像：
# docker-compose build
##下载镜像：
# docker-compose pull

##运行的：
# docker-compose ps
##进程：
# docker-compose top
##启动：
# docker-compose start
##停止：
# docker-compose stop

#docker-compose ls
#docker-compose rm
#docker-compose logs -f