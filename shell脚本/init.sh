#!/bin/bash
## -bash: ./lzj.sh: /bin/bash^M: bad interpreter: No such file or directory
## vim或者vi的命令模式下，输入命令  set fileformat=unix 即可解决换行问题
echo -e "\e[1;31m【----------------------------------------在opt和var创建lzj文件夹】\e[0m"
sleep 2
mkdir -p /opt/lzj
mkdir -p /var/lzj
mkdir -p /usr/local/scripts

echo -e "\e[1;31m【----------------------------------------禁用防火墙】\e[0m"
sleep 2
systemctl stop firewalld
systemctl disable firewalld
systemctl status firewalld

echo -e "\e[1;32m【----------------------------------------修改selinux】\e[0m"
sleep 2
sed -i '/^SELINUX=/c SELINUX=disabled' /etc/selinux/config

echo -e "\e[1;32m【----------------------------------------安装wget】\e[0m"
sleep 2
yum install wget -y

echo -e "\e[1;33m【----------------------------------------修改yum源】\e[0m"
sleep 2
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache

echo -e "\e[1;33m【----------------------------------------安装常用软件】\e[0m"
yum install man man-pages ntp vim lrzsz zip unzip telnet perl net-tools -y

echo -e "\e[1;34m【----------------------------------------同步系统时间】\e[0m"
yum info ntp &&  ntpdate cn.ntp.org.cn

echo -e "\e[1;34m【----------------------------------------DNS域名配置】\e[0m"
sleep 2
echo "192.168.58.100 basenode" >> /etc/hosts
echo "192.168.58.101 node01" >> /etc/hosts
echo "192.168.58.102 node02" >> /etc/hosts
echo "192.168.58.103 node03" >> /etc/hosts
echo -e "\e[1;34m【----------------------------------------安装JDK】\e[0m"
sleep 2
rpm -ivh jdk-8u231-linux-x64.rpm
echo 'export JAVA_HOME=/usr/java/jdk1.8.0_231-amd64' >> /etc/profile
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
source /etc/profile
echo -e "\e[1;35m【----------------------------------------安装Tomcat】\e[0m"
sleep 2
tar -zxf apache-tomcat-8.5.47.tar.gz
mv apache-tomcat-8.5.47 /opt/lzj/
echo -e "\e[1;35m【----------------------------------------安装Mysql】\e[0m"
sleep 2
rpm -e --nodeps `rpm -qa | grep mariadb`

tar -xvf mysql-5.7.28-1.el7.x86_64.rpm-bundle.tar
rpm -ivh mysql-community-common-5.7.28-1.el7.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.28-1.el7.x86_64.rpm
rpm -ivh mysql-community-client-5.7.28-1.el7.x86_64.rpm
rpm -ivh mysql-community-server-5.7.28-1.el7.x86_64.rpm

systemctl start mysqld
systemctl enable mysqld

temppasswd=`grep "A temporary password" /var/log/mysqld.log | awk '{ print $NF}'`

mysql -uroot -p$temppasswd --connect-expired-password << EOF
set global validate_password_policy=low;
set global validate_password_length=6;
alter user root@localhost identified by '123456';

use mysql;
update user set  host='%' where user = 'root';
commit;
quit
EOF

systemctl restart mysqld

echo -e "\e[1;36m【----------------------------------------设置开机启动项】\e[0m"
sleep 2
touch /usr/local/scripts/auto_ntpdate.sh
echo '#!/bin/bash' >> /usr/local/scripts/auto_ntpdate.sh
echo 'yum info ntp &&  ntpdate cn.ntp.org.cn' >> /usr/local/scripts/auto_ntpdate.sh
chmod u+x /usr/local/scripts/auto_ntpdate.sh

echo '/usr/local/scripts/auto_ntpdate.sh' >> /etc/rc.local
chmod u+x /etc/rc.local

echo -e "\e[1;36m【----------------------------------------删除文件】\e[0m"
sleep 2
rm -rf apache-tomcat-8.5.47.tar.gz
rm -rf jdk-8u231-linux-x64.rpm
rm -rf mysql*
rm -rf *.sh

echo -e "\e[1;36m【----------------------------------------关闭计算器，拍快照】\e[0m"
sleep 2
shutdown -h now