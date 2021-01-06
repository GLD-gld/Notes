### 7.1 网络数据包连接进入主机的流程

***

1.数据包进入主机的流程

+ 经过防火墙的分析

  + Linux系统有内建的防火墙机制，默认有两个机制，两个机制独立存在，因此默认有两层防火墙。
  + 第一层是数据包过滤式的Net Filter防火墙
  + 第二层则是通过软件管理的TCP Wrappers防火墙

  

+ 数据包过滤防火墙：IP Filtering 或 Net Filter

  + 要进入Linux本机的数据包都会先通过Linux内核的预置防火墙，即NetFilter。就是iptables这个软件所提供的防火墙功能
  + 主要针对TCP/IP的数据包头部来进行过滤的机制，主要分析的是OSI的第二、三、四层
  + 主要控制的就是MAC、IP、ICMP、TCP与UDP的端口与状态（SYN，ACK）等

+ 第二层防火墙：TCP Wrappers

  + 就是/etc/hosts.allow与/etc/hosts.deny的配置文件功能。



+ 服务的基本功能
  + 防火墙主要管理的是MAC、IP、Port等数据包头部方面的信息
  + 如果想要允许某些目录可以进入，某些目录无法进入，就需要通过权限以及服务器软件提供的相关功能实现了
  + 例：可以在httpd.conf这个配置文件之内规范某些IP来源不能使用httpd这个服务来取得主机的数据，那么即使该IP通过前面两层的过滤，依旧无法取得主机的资源。
  + **如果httpd这个程序本来就有问题的话，那么Client端将可直接利用httpd软件的漏洞来入侵主机，而不需要取得主机内root的密码**



+ SELinux对网络服务的详细权限控制
  + SELinux可以针对网络服务的权限来设置一些规则（Policy），让程序能够拥有的功能有限
  + 因此当用户的文件权限设置错误，以及程序有问题时，即使使用的是root权限，该程序能够执行的操作也是被限制的。



+ 使用主机的文件系统资源
  + 网页数据的权限当然就是要让httpd这个程序可以读取
  + 分析日志文件：/var/log/messages与/var/log/secure
  + http://linux.vbird.org/download/index.php?action=detail&fileid=60



2.常见的攻击手法与相关保护

+ 取得账户信息猜密码
+ 利用系统的程序漏洞主动攻击
+ 利用社会工程学欺骗
+ 利用程序功能的“被动”攻击
+ 蠕虫或木马的Rootkit
+ DDoS攻击法（Distributed Denial of Service）
+ 其他



3.主机能执行的保护操作：软件更新、减少网络服务、启动SELinux

+ 软件更新的重要性
+ 认识系统服务的重要性
+ 权限与SELinux的辅助





### 7.2 网络自动升级软件

1.如何进行软件升级

2.CentOS的yum软件更新、镜像站点使用的原理

+ 原理：CentOS可在yum服务器上下载官方网站给出的rpm表头列表数据，该数据除了记载每个rpm软件的相依性之外，也说明了rpm文件所放置的容器（Repository）所在。
+ 流程：
  + 先由配置文件判断yum Server所在的IP地址
  + 连接到yum Server后，先下载新的rpm文件的表头数据
  + 分析比较用户所欲安装/升级的文件，并提供用户确认。
  + 下载用户选择的文件到系统中的/var/cache/yum，并进行实际安装
+ CentOS官网列出的亚洲地区镜像站点一览表
  + `htt://www.centos.org/modules/tinycontent/index.php?id=32`



3.yum的功能：安装软件组、全系统更新

Yum不仅能够提供在线自动升级，它还可以用于查询、软件组的安装、整体版本的升级等。

+ yum [option] [查询的工作项目] [相关参数]
  + option：主要的参数，包括有：
    + -y：主动回答yes而不需要由键盘输入
  + 查询的工作项目：由于不同的使用条件，而有一些选择的项目，包括：
    + install：指定安装的软件名称，所以后面需接软件名称
    + update：进行整体升级的行为：当然也可以接某个软件，仅升级一个软件
    + remove：删除某个软件
    + search：搜寻某个软件或者是重要关键字
    + list：列出目前yum所管理的所有的软件名称与版本，有点类似rpm -qa
    + info：同上，不过有点类似rpm -qai
    + clean：下载的文件被放到/var/cache/yum，可使用clean将它移除，例如packages｜headers｜metadata｜cache等
    + grouplist：列出所有可使用的软件组，例如Development Tools之类
    + groupinfo：后面接group_name，则可了解该group内含的所有软件名
    + groupinstall：可以安装一整套的软件组，常与--installroot=/some/path 共享来安装新系统
    + groupremove；删除某个软件组
+ 所有下载的rpm文件都会在安装完毕之后予以删除
+ 如果想要下载的rpm文件继续保留在/var/cache/yum当中，就需要修改/etc/yum.conf配置文件
  + `keepcache=1`
  + 可以给内网的所有机器升级：`rpm -Fvh *.rpm`



+ yum安装软件组
  + 软件群组又分为“Desktop Platform”与开发者“Desktop Platform Development”两部分
+ 全系统更新



4.挑选特定的镜像站点：修改yum配置文件与清除yum缓存

+ 镜像站点中最重要的特色就是repodata的目录。该目录就是分析rpm软件后所产生的软件属性相依数据放置处。

+ ```shell
  vim /etc/yum.repos.d/test.repo
  baseurl=http://...				#最重要
  
  yum clean all			#改过配置文件，最好清除已有清单
  yum repolist all  #列出目前yum server所使用的容器有哪些 enabled才是启动的
  ```

+ yum clean [packages|headers|all]

  + packages：将已下载的软件文件删除
  + headers：将下载的软件文件头删除
  + all：将所有容器数据都删除



### 7.3 限制连接端口（Port）

***

1.什么是Port

当你启动一个网络服务是，这个服务会依据TCP/IP的相关通信协议启动一个端口进行监听，那就是TCP/UDP数据包的Port（端口）了。

+ 服务器端启动的监听端口所对应的服务是固定的
  + www：Port 80
  + FTP：Port 21
  + E-mail：Port 25
+ 客户端启动程序时，随机启动一个大于1024以上的端口
  + 浏览器、Filezilla
+ 一台服务器可以同时提供多种服务
  + 所谓的“监听”是某个服务程序会一直常驻在内存当中，所以该程序启动的Port就会一直存在。端口不同，所以可以同时启动不同服务
+ 共65536个Port
  + Port 占用 16个位，以Port 1024分开
  + 只有root才能启动保留的Port：小于1024端口。这些Port主要是用于一些常见的通信服务，常见的协议于Port的对应是记录在/etc/services里面
  + 大于1024用于Client端的Port：主要是作为Client端的软件激活端口
+ 是否需要三次握手
  + 建立可靠的连接服务需要用到TCP协议，需要三次握手
  + 非面向连接，例如DNS和视频系统，只要使用UDP协议即可
+ 通信协议可以启用在非正规的Port
  + 常用在一些地下网站
+ 所谓的Port安全性
  + 没有所谓的Port安全性，因为Port的启用是有服务软件所造成的。
  + 真正影响网络安全的并不是Port，而是启动Port的那个软件。
  + 对安全真正有危害的是某些不安全的服务而不是开了哪些Port。



2.端口的查看：netstat、nmap

​	服务跟Port对应的文件：/etc/services

+ netstat：在本机上面以自己的程序监测自己的Port

  + 列出正在监听的网络服务

    + `netstat -tunl`

  + 列出已连接的网络连接状态

    + `netstat -tun`

  + 删除已建立或在监听当中的连接

    + ```shell
      netstat -tunp
      kill -9 PID
      ```



+ nmap：通过网络的监测软件辅助，可监测非本机上的其他网络主机，但有非法之虞。
  + Network exploration tool and security/port scanner：被系统管理员用来管理系统安全性检查的工具。
  + nmap [扫描类型] [扫描参数] [hosts 地址与范围]
  + [扫描类型]：主要的扫描类型有下面几种：
    + -sT：扫描TCP数据包已建立的连接connect（）
    + -sS：扫描TCP数据包带有SYN卷标的数据
    + -sP：以ping的方式进行扫描
    + -sO：以IP的协议进行主机的扫描
  + [扫描参数]：主要的扫描参数有几种：
    + -PT：使用TCP里头的ping的方式来进行扫描，可以获知目前有几台计算机存在（较常用）
    + -PI：使用实际的ping（带有ICMP数据包的）来进行扫描
    + -P：这个是port range，例如1024-，80-1023，30000-60000等的使用方式
  + [Hosts 地址与范围]：有几种类似的类型
    + 192.168.1.100：直接写入HOST IP而已，仅检查一台
    + 192.168.1.0/24：为C Class的形态
    + 192.168.* .*：B Class的形态
    + 192.168.1.0-50,60-100,103,200：变形的主机范围
  + 使用默认参数扫描本机所启用的port（只会扫描 TCP）
    + `nmap localhost`
  + 同时扫描本机的TCP/UDP端口
    + `nmap -sTU localhost`
  + 通过ICMP数据包的监测，分析局域网内有几台主机是启动的
    + `nmap -sP 192.168.1.0/24`
  + 检测端口
    + `nmap 192.168.1.0/24`



3.端口与服务的启动/关闭及开机时状态设定

​	其实Port是在执行某些软件之后被软件激活的，所以要关闭某些port时，可直接将某个程序关闭就好了。

​	可以用kill，但不是正统的解决之道。可利用系统给我们的script即可

+ stand alone 与 super daemon
  + stand alone就是直接执行该服务的可执行文件，让该执行文件直接加载到内存当中运行。服务具有较快速的响应。
  + 启动的script一般放置在/etc/init.d/这个目录下面
  + /etc/init.d/ssh restart
+ super daemon
  + 响应慢，不过有额外管理：何时启动，何时可以进行连接，哪个IP可以连进来，是否允许同时连接等
  + /etc/xinetd.d/
  + /etc/init.d/xinetd restart



+ 关闭Port

  + ```shell
    找到那个Port
    netstat -tnlp ｜ grep 111
    找到文件后，再以rpm处理
    which rpcbind
    找到这个软件
    rpm -qf /sbin/rpcbind
    
    rpm -qc rpcbind | grep init
    
    /etc/init.d/rpcbind stop
    
    ```

+ 启动Telnet

  + ```shell
    rpm -qa | grep telnet-server
    yum install telnet-server
    
    /etc/xinetd.d/telnet
    disable=yes --> disable=no
    
    /etc/init.d/xinetd restart
    
    netstat -tnlp
    ```

  + ```shell
    chkconfig --list |  grep rpcbind 与 runlevel 来确认一下rpcbind是否启动
    chkconfig --level 35 rpcbind off  来设置开机时不要启动
    可以通过“/etc/init.d/rpcbind stop”来立即关闭它
    ```



+ 很多的系统服务是必须存在的，否则系统将会出问题
  + acpid：电源模块
  + atd：管理单一计划命令时执行的服务，应该要启动的
  + crond：计划任务
  + haldaemon：系统硬件变更检测的服务
  + iptables：防火墙
  + network：网络
  + postfix：邮件
  + rsyslog：登录文件记录
  + sshd：在远程以文字界面的终端机登录
  + xinetd：就是super daemon



4.安全性考虑——关闭网络服务端口

+ ```shell
  netstat -tlunp
  
  找到启动脚本
  rpm -qc $(rpm -qf $(which rpc.statd)) | grep init
  ```

+ ```shell
  vim closedaemon.sh
  for daemon in nfs nfslock rpcgssd rpcidmapd rpcsvcgssd xinetd rpcbind
  do
  	chkconfig $daemon off
  	/etc/init.d/$daemon stop
  done
  ```



### 7.4 SELinux 管理原则

***

1.SELinux的工作模式

​	SELinux是通过MAC的方式来管理程序，它控制的主体是程序，而目标则是该程序能否读取的文件资源。

+ 主体（Subject）
  + SELinux主要管理的就是程序，可以将“主体”跟Process划上等号。
+ 目标（Object）
  + 主体程序访问的目标资源一般就是文件系统。
+ 策略（Policy）
  + targeted：针对网络服务限制较多，针对本机限制较少，是 默认的策略。
  + mls：完整的SELinux限制，限制方面较为严格。
+ 安全性环境（Security Context）
  + 主体与目标的安全性环境必须一致才能够顺利访问目标。



+ 重点：
  + 主体程序必须要通过SELinux策略内的规则放行后，才可以与目标资源进行安全性环境的比对，若比对失效则无法访问目标
  + 若比对成功则可以开始访问目标



+ 安全性环境（Security Context）
  + 可以将安全性环境看成SELinux内必备的rwx
  + 安全性环境是放置到文件的inode内的
  + 查看安全性环境：ls -Z
+ Identify:role:type    身份识别:角色:类型
+ 身份识别：
  + root：表示root的账号身份
  + system_u：表示系统程序方面的识别，通常就是程序
  + user_u：代表的是一般用户账号相关的身份
+ 角色：
  + object_r：代表的是文件或目录等文件资源
  + system_r：代表的就是程序了。或一般用户
+ 类型：
  + Type：在文件资源（Object）中称为类型（Type）
  + Domain：在主体程序（Subject）中则称为域（Domain）
  + Domain需要与Type搭配，该程序才能够顺利地读取文件资源



+ 程序与文件SELinux Type字段的相关性
  + 策略内需要制定详细的domain/type相关性
  + 若文件的Type设置错误，即使权限设置为rwx全开的777，该主体程序也无法读取目标文件资源。



2.SELinux的启动、关闭与查看

+ 三种模式：

  + enforcing：强制模式，代表SELinux运行中，且已经正确的开始限制domain/type了
  + permissive：宽容模式，代表SELinux运作中，不过仅会有警告信息并不会实际限制domain/type的访问。Debug用
  + disabled：关闭，SELinux并没有实际运行。

  ```shell
  getenforce
  vim /etc/selinux/config
  SELINUX=enforcing          #调整模式
  SELINUXTYPE=targeted       #目前仅有targeted与mls
  ```



+ 由enforcing或permissive改成disabled，或相反。必须要重新启动服务。
  + setenforce [0|1]
  + 0：转成permissive 宽容模式
  + 1：转成Enforcing 强制模式
  + setenforce无法在Disabled的模式下面进行模式的切换
+ Disabled转成Enforcing后，如果出现一堆服务无法顺利启动
  + 在Permissive的状态下，使用`restorecon -Rv /`重新还原所有SELinux的类型



3.SELinux Type的修改

​	文件复制时，SELinux的Type字段会继承自目标目录

​	默认的SELinux Type类型记录在/etc/selinux/targeted/contexts

+ chcon：修改
+ chcon [-R] [-t type] [-u user] [-r role] 文件
+ chcon [-R] --reference=范例文件 文件
  + -R：连同该目录下的子目录也同时修改
  + -t：后面接安全性环境的类型字段，例如：httpd_sys_content_t
  + -u：后面接身份识别，例如 system_u
  + -r：后面接角色，例如 system_r
  + --reference=范例文件：拿某个文件当范例来修改后续接的文件类型
+ restorecon：恢复成原有的SELinux Type
+ restorecon [-Rv] 文件或目录
  + -R：连同子目录一起修改
  + -v：将过程显示到屏幕上
+ semanage：查询类型与修改
+ semanage {login|user|port|interface|fcontext|translation} -l
+ semanage fcontext -{a|d|m} [-frst] file_spec
  + fcontext：主要用在安全性环境方面，-l为查询的意思
  + -a：增加的意思，你可以增加一些目录的默认安全性环境类型设置
  + -m：修改的意思
  + -d：删除的意思



+ 查询一下/var/www/的默认安全性环境设置为何

  + `semanage fcontext -l | grep '/var/www'`

+ 利用semanage设置/srv/vbird目录的默认安全性环境为 public_content_t

  + ```shell
    mkdir /srv/vbird
    ll -Zd /srv/vbird
    
    semanage fcontext -l | grep '/srv'
    
    semanage fcontext -a -t public_content_t "/srv/vbird(/.*)?"
    semanage fcontext -l | grep '/srv/vbird'
    
    cat /etc/selinux/targeted/contexts/files/file_contexts.local
    
    restorecon -Rv /srv/vbird*    尝试恢复默认值
    ll -Zd /srv/vbird
    ```



4.SELinux策略内的规则布尔值修订

+ 策略查阅
+ yum install setools-console
+ seinfo [-Atrub]
  + -A：列出SELinux的状态、规则布尔值、身份识别、角色、类别等所有信息
  + -t：列出SELinux的所有类别（type）种类
  + -r：列出SELinux的所有角色（role）种类
  + -u：列出SELinux的所有身份识别（user）种类
  + -b：列出所有规则的种类（布尔值）
+ 列出与httpd有关的规则（booleans）有哪些
  + `seinfo -b ｜ grep httpd`
+ sesearch [--all] [-s 主体类别] [-t 目标类别] [-b 布尔值]
  + --all：列出该类别或布尔值的所有相关信息
  + -t：后面还要接类别，例如-t httpd_t
  + -b：后面还要接布尔值的规则，例如-b httpd_enable_ftp_server
+ 找出目标文件资源类别为httpd_sys_content_t的有关信息
  + `sesearch -all -t httpd_sys_content_t`



+ 布尔值的查询与修改

+ getsebool [-a] [布尔值条款]

  + -a：列出目前系统上面的所有布尔值条款设置为开启或关闭值

+ 查询本系统内所有的布尔值设置状况

  + `getsebool -a`

+ setsebool [-P] 布尔值=[0|1]

  + -P：直接将设置值写入配置文件，该设置数据未来会生效的

+ 查询httpd_enable_homedirs是否为 on，若不为 on，请启动它

  ```shell
  getsebool httpd_enable_homedirs
  setsebool -P httpd_enable_homedirs=1
  getsebool httpd_enable_homedirs
  ```



5.SELinux日志文件记录所需的服务

+ 检测SELinux产生错误的服务：auditd与setroubleshoot，不过都整合到auditd中了
+ setroubleshoot：将错误信息写入/var/log/messages
  + 这个服务会将错误信息与克服方法记录到/var/log/messages与/var/log/setroubleshoot/*中
  + 两个软件：setroubleshoot与setroubleshoot-server
  + `yum install setroubleshoot setroubleshoot-server`
  + `/etc/init.d/auditd restart`



+ 用E-mail或在命令列上面直接提供setroubleshoot错误信息

+ ```shell
  vim /etc/setroubleshoot/setroubleshoot.cfg
  18行
  recipients_filepath = /var/lib/setroubleshoot/email_alter_recipients
  147行
  console=True
  
  vim /var/lib/setroubleshoot/email_alert_recipients
  root@localhost
  your@email.address
  
  /etc/init.d/auditd restart
  ```



+ SELinux错误克服的总结
  + 网络连接要通过SELinux的权限判定后才能够继续rwx的权限比对，而SELinux的比对需要通过策略的各项规则比对后才能够进行SELinux Type安全性环境的比对，这两项工作都需要正确才行。
  + 而后续的SELinux修改主要是通过chcon、restorecon、setsebool等命令来处理的。
  + 通过分析/var/log/messages内提供的setroubleshoot的信息，就可以很轻松地管理SELinux了。



### 7.5 被攻击后的主机修复工作

***

1.网管人员应具备的技能

​	其实一台主机最常发生问题的状况，都是由内部的网络误用所产生的。

+ 了解什么是需要保护的内容
+ 预防黑客（Black Hats）的入侵
+ 主机环境安全化
+ 防火墙规则的制定
+ 实时维护主机
+ 良好的教育训练课程
+ 完善的备份计划



2.主机受攻击后恢复的工作流程

+ 1.立即拔出网线
+ 2.分析日志文件信息，查找可能的入侵途径
  + 分析日志文件：低级的Cracker通常仅是利用工具软件来入侵系统。
  + 可以分析：/var/log/messages、/var/log/secure
  + 利用last命令来找出上次登录用户的信息
  + 检查主机开放的服务
  + 查询Internet上面的安全通报
+ 3.重要数据备份：非Linux系统上面原有的数据
+ 4.重新安装
+ 5.软件的漏洞修补
+ 6.关闭或删除不需要的服务
+ 7.数据恢复与恢复服务设置
+ 8.连上Internet