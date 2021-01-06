### Install docker/docker-compose

+++

网易yum_repo：http://mirrors.163.com/.help/centos.html

阿里yum_repo：https://developer.aliyun.com/mirror/

scp /Users/gld/Downloads/CentOS7-Base-163.repo gld@192.168.1.10:/etc/yum.repos.d/

```shell
1.备份
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

2.下载yum.repo
curl -O http://mirrors.163.com/.help/CentOS7-Base-163.repo

3.生成yum缓存
yum clean all
yum mackcache
```

