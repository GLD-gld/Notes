### 9.1 认识防火墙

***

​	防火墙就是通过定义一些有顺序的规则，并管理进入到网络内的主机数据数据包的一种机制

​	只要能够分析与过滤进出进出我们管理的网络的数据包的数据，就可以称为防火墙。

1.关于本章的一些提醒事项

2.为何需要防火墙

+ 防火墙最大的功能就是帮助你限制某些服务的访问来源
+ 防火墙最重要的任务就是规划出：
  + 切割被信任（如子域）与不被信任（如Internet）的网段
  + 划分出可提供Internet的服务与必须受保护的服务
  + 分析出可接受与不可接受的数据包状态

3.Linux系统上防火墙的主要类别

+ Netfilter（数据包过滤机制）
  + 硬件地址MAC、软件地址IP、TCP、UDP、ICMP等数据包的信息都可以进行过滤分析
  + 主要分析的是OSI七层协议的2，3，4层
+ TCP Wrappers（程序管理）
  + 主要是通过分析服务器程序来管理，因此与启动的端口无关，只与程序的名称有关。
+ Proxy（代理服务器）



4.防火墙的一般网络布线示意

+ 单一网络，仅有一个路由器
  + 因为内外网络已经分开，所以安全维护在内部可以开放的权限较大。
  + 安全机制的设置可以针对Linux防火墙主机来维护即可。
  + 对外只看到Linux防火墙主机，所以对于内部可以达到有效的安全防护
+ 内部网络包含安全性更高的子网，需内部防火墙切开子网
  + 更多时候是由于某些外来访客利用移动设备（笔记本电脑）连接到公司内部的无限网络来加以窃取企业内部的重要信息。
+ 在防火墙的后面架设网络服务器主机



5.防火墙的使用限制

+ 拒绝让Internet的数据包进入主机的某些端口
+ 拒绝让某些来源IP的数据包进入
+ 拒绝让带有某些特殊标志（flag）的数据包进行
+ 分析硬件地址MAC来决定连接与否
+ 防火墙并不能有效阻挡病毒或木马程序
+ 防火墙对于来自内部LAN的攻击无能为力

```shell
firewall-cmd --state                          ##查看防火墙状态，是否是running
firewall-cmd --reload                          ##重新载入配置，比如添加规则之后，需要执行此命令
firewall-cmd --get-zones                      ##列出支持的zone
firewall-cmd --get-services                    ##列出支持的服务，在列表中的服务是放行的
firewall-cmd --query-service ftp              ##查看ftp服务是否支持，返回yes或者no
firewall-cmd --add-service=ftp                ##临时开放ftp服务
firewall-cmd --add-service=ftp --permanent    ##永久开放ftp服务
firewall-cmd --remove-service=ftp --permanent  ##永久移除ftp服务
firewall-cmd --add-port=80/tcp --permanent    ##永久添加80端口 
firewall-cmd --remove-port=80/tcp --permanent    ##永久移除80端口 
firewall-cmd --zone=public --list-ports       ##查看已开放的端口

iptables -L -n                                ##查看规则，这个命令是和iptables的相同的
man firewall-cmd
```



### 9.2 TCP Wrappers

***

1.哪些服务有支持

+ 由super daemon（xinetd）所管理的服务

  + 配置文件在/etc/xinetd.d/里面的服务就是xinetd所管理的

+ 支持libwrap.so模块的服务

  + ```shell
    for name in rsyslogd sshd xinetd httpd; do echo $name; ldd $(which $name) | grep libwrap; done
    ```

+ 满足上面条件才可以使用/etc/hosts.{allow|deny}来进行防火墙机制的控制

+ TCP Wrappers是通过启动服务的文件名来管理的



+ /etc/hosts.{allow|deny}的设置方式

  + 两个文件的语法

  + ```shell
    service(program_name):ip或domain或hostname
    #服务 : IP或域或主机名
    #不支持192.168.1.0/24这种bit数值的显示方式
    #只支持Netmask的地址显示方式
    ```

  + 先以/etc/hosts.allow进行优先比对，该规则符合就予以放行。

  + 再以/etc/hosts.deny比对，规则符合就予以抵挡。

  + 若不在这两个文件内，亦即规则都不符合，最终则予以放行。

+ 例：开放本机的127.0.0.1可以进行任何本机的服务，然后，让局域网（192.168.1.0/24）可以使用rsync，同时10.0.0.100也能够使用rsync，但其他来源则不允许使用rsync。

  + ```shell
    cat /etc/xinetd./rsync
    
    vim /etc/hosts.allow
    ALL: 127.0.0.1				#这就是本机全部的服务都接受
    rsync: 192.168.1.0/255.255.255.0 10.0.0.100
    
    vim /etc/hosts.deny
    rsync: ALL
    ```



### 9.3 Linux的数据包过滤软件：iptables

***

1.不同Linux内核版本的防火墙软件

2.数据包进入流程：规则顺序的重要性

