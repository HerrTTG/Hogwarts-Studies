# 拉取mariadb镜像
docker pull bitnami/mariadb

# 拉取testlink镜像
docker pull bitnami/testlink-archived


##创建数据库目录
mkdir -p /home/test/mysql


##设置网络
docker network create testlink

##启动数据库
docker run -d --name mariadb --net testlink --restart=always --privileged=true -e MARIADB_ROOT_PASSWORD=testlink -e MARIADB_USER=testlink -e MARIADB_PASSWORD=testlink -e MARIADB_DATABASE=testlink bitnami/mariadb

##启动testlink
docker run -d -p 5005:8080 -p 8445:8443 --name testlink --net testlink --restart=always --privileged=true -e TESTLINK_DATABASE_USER=testlink -e TESTLINK_DATABASE_PASSWORD=testlink -e TESTLINK_DATABASE_NAME=testlink bitnami/testlink-archived