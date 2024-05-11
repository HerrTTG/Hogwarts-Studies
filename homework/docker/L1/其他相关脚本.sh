docker run --name(设置启动的容器名称) -d 后台运行  -e环境信息传递

常用参数：
-p端口映射（宿主机端口:容器端口）
端口映射非常重要，如果没有，是无法被外部访问的。
端口映射的概念相当于是用启动容器的服务器作为跳板机，外部访问先访问服务器，在通过端口映射访问到对应容器

tip:容器本身是无法永久存东西了，在容器中的东西如果容器被删除会一起丢失
解决办法就是挂载将某一个文件 或者路径 挂载到容器中去，容器哪怕被删除。文件也不会丢失，路径也不会丢失

-v （宿主机的路径:想要放在容器中的路径 ） 挂载宿主机中的XX路径到容器中作用是可以使容器对文件的操作永久性，另外就是配合权限设置可以让容器调用宿主机中的一些命令，如docker



部署nginx服务
      docker run -d -p 5004:80 --name mynginx nginx
      docker run -d -p 5004:80 -v "$PWD/html":/usr/share/nginx/html --name mynginx nginx(映射文件)

搭建mysql
-v 将mysql路径挂载为宿主机 保存
      docker run --name some-mysql -v /home/test/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=Kuoka314+ -p 33066:3306 -d mysql
      docker run --name hzy-mysql -e MYSQL_ROOT_PASSWORD=Kuoka314+ -p 33066:3306 -d mysql


搭建jinkins
-p可以多个
-it可以不用写
--restart always 如果容器发生异常 是否自动重启
--privileged 特权模式 docker 为了安全 容器在启动的时候默认关闭了很多权限。privileged是Docker容器的一个选项，用于授予容器内的进程对主机系统的更高权限。当您使用--privileged标志来运行容器时，容器内的进程将具有对主机系统的完全访问权限，包括访问设备、挂载文件系统等。这在一些特定的使用情况下可能是必要的，但同时也带来了一些安全风险。

--user root 指明启动容器使用root用户进行启动 jinkins经常需要再容器里调用docker 所以需要设置特殊权限和root用户
-v 并且配合-v将docker相关的路径和文件挂载到jinkins容器中

docker pull jenkins/jenkins:lts

docker run --name myjenkins -itd -p 5003:8080 -p 50000:50000 --restart always --privileged=true  --user root  --env JAVA_OPTS="-Xmx8192m" -v $(pwd)/jenkins_data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v /bin/docker:/bin/docker  jenkins/jenkins:lts


搭建jira

jira要申请license
部署简单设置难
docker run -v "$PWD"/jira:/var/atlassian/application-data/jira --name="jira" -d -p 5005:8080 atlassian/jira-software


搭建testlink
https://blog.51cto.com/u_14664141/6315715
部署testlink需要两个容器，需要数据库保存数据
解决两个容器之间如何通讯问题
--link {指定容器} docker将指定容器的网络信息 以环境变量的形式 注入到启动的容器中去

docker network create
在Docker中， docker network create命令是用于创建新的网络的主要命令之一。
Docker网络是用来连接Docker容器的虚拟网络。docker network create命令就是用来创建这些虚拟网络的。

基本用法
docker network create命令的基本语法如下：

docker network create [OPTIONS] NETWORK_NAME

其中，NETWORK_NAME参数指定要创建的网络的名称。

创建一个名为my_network的桥接网络

docker network create my_network


通过上述命令，可以创建一个名为my_network的桥接网络。桥接网络是默认的Docker网络类型，适用于连接同一主机上的多个容器。

创建一个自定义子网和网关的桥接网络
docker network create --subnet=192.168.0.0/16 --gateway=192.168.0.1 my_network
        通过上述命令，可以创建一个名为my_network的桥接网络，并指定了自定义的子网和网关。





--net docker run创建Docker容器时，可以用 --net 选项指定容器的网络模式  --net testlink表示设置在在 testlink这个桥接网络上。
--privileged




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


登录
user/bitnami

