### install docker

+++

```shell
1.安装docker
yum install -y docker

2.启动docker服务													RedHat8 可能需要安装firewalld，并关闭firewalld。
systemctl start docker.service

3.查看安装结果
docker version

4.设置docker开机启动
systemctl enable docker.servie

5.配置docker镜像下载加速
vim /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
or
{
  "registry-mirrors": ["https://registry.cn-hangzhou.aliyuncs.com"]
}

6.重新加载配置文件
systemctl daemon-reload

7.重启docker服务
systemctl restart docker.service

8.安装docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

9.给执行权限
chmod +x /usr/local/bin/docker-compose

```

