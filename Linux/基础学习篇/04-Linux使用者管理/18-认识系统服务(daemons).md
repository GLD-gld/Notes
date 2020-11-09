### 18.1 什么是daemon与服务（service）

***

1.daimon的主要分类

+ stand_alnoe：此daemon可以自行单独启动服务
  + www的httpd，FTP的vsftpd
+ super_daemon：一个特殊的daemon来统一管理
  + telnet
+ 窗口类型
  + 个别窗口负责单一服务的stand alone
  + 统一窗口负责各种业务的super daemon
  + multi-threaded（多线程）
  + single-threaded（单线程）



2.服务与端口的对应

+ 服务与端口号的对应
  + /etc/services
  + 第一列为daemon的名称
  + 第二列为该daemon所使用的端口号与网络数据包协议



3.daemon的启动脚本与启动方式

+ /etc/init.d/*：启动脚本放置处
+ /etc/sysconfig/*：各服务的初始化环境配置文件
+ /etc/xinted.conf，/etc/xinted.d/*：super daemon配置文件
+ /etc/*：各服务各自的配置文件
+ /var/lib/*：各服务产生的数据库
+ /var/run/*：各服务的程序的PID记录处



### 18.2 解析super daemon的配置 文件

***

1.默认值配置文件：xinetd.conf



2.一个简单的rsync范例设置

+ rsync可以进行远程镜射（mirror）



### 18.3 服务的防火墙管理xinetd，TCP Wrappers

***

1./etc/hosts.allow，/etc/hosts.deny管理

+ 任何以xinetd管理的服务都可以通过/etc/hosts.allow，/etc/hosts.deny来设置防火墙。



2.TCP Wrappers特殊功能



### 18.4 系统开启的服务

***

1.查看系统启动的服务

+ 找出目前系统开启的网络服务有哪些
  + `netstat -tulp`
+ 找出所有的有监听网络的服务
  + `netstat -lnp`
+ 查看所有的服务状态
  + service --status -all



2.设置开机后立即启动服务的方法

+ chkconfig：管理系统服务默认开机启动与否
+ `chkconfig [--level [0123456]] [服务名称] [on|off]`
  + list：仅将目前的各项服务状态栏显示出来
  + level：设置某个服务在该 level 下启动（on）或关闭（off）

