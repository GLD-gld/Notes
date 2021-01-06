### install gitlab

+++

1.安装依赖软件

```shell
sudo yum install -y git vim gcc glibc-static telnet
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd

sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix
```



2.设置gitlab安装源

```shell
vim /etc/yum.repos.d/gitlab-ce.repo
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1

国外：curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
```



3.安装gitlab

+ 设置域名，然后安装

```shell
sudo EXTERNAL_URL="http://gitlab.example.com" yum install -y gitlab-ce
```

+ 直接安装

```shell
sudo yum install -y gitlab-ce
```



4.安装完成后配置

```shell
sudo gitlab-ctl reconfigure
```



5.gitlab配置文件

```shell
/etc/gitlab/gitlab.rb
```



6.修改hosts

+ 宿主机

```shell
ip    EXTERNAL_URL
```

+ gitlab_server

```shell
127.0.0.1    EXTERNAL_URL
```



7.登陆和修改密码

​	打开http://gitlab.example.com/ 修改root用户密码，然后使用root和新密码登陆。



8.命令

```shell
gitlab-ctl start
gitlab-ctl status
gitlab-ctl stop
```





+++

### install runner

+++

1.安装docker

```shell
curl -sSL https://get.docker.com/ | sh
```



2.安装gitlab ci runner（Using binary file）

```shell
1.Simply download one of the binaries for your system:
# Linux x86-64
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64"

# Linux x86
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-386"

# Linux arm
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-arm"

# Linux arm64
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-arm64"

# Linux s390x
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-s390x"

2.Give it permissions to execute:
sudo chmod +x /usr/local/bin/gitlab-runner

3.Create a GitLab CI user:
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash

4.Install and run as service:
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
```



3.查看是否正常运行

```shell
sudo gitlab-runner status
```



4.注册runner

```shell
sudo gitlab-runner register
```



5.设置Docker权限

```shell
sudo usermod -aG docker gitlab-runner
sudo systemctl restart docker.service
sudo gitlab-runner restart
```



6.命令

```shell
gitlab-runner start
gitlab-runner status
gitlab-runner stop
```



7.配置文件/etc/gitlab-runner/config.toml

```shell
concurrent = 1
check_interval = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "demo-project"
  url = "http://gitlab.example.com/"
  token = "zHcmHQyQ-XXUFXUwG9o_"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    extra_hosts = ["gitlab.example.com:192.168.1.10"]
    shm_size = 0
```

