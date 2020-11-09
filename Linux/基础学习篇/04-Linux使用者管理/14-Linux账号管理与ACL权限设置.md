### 14.1 Linux的账号与用户组

***

1.用户标识符：UID与GID

+ Linux仅认识ID
+ UID（UserID），/etc/passwd
+ GID（GroupID），/etc/group

+ 密码：/etc/shadow

  

2.用户账号

+ /etc/passwd文件结构，共7个字段

  + 每一行都代表一个账号，有几行就代表有几个账号在你的系统中！

  + 里面有很多账号本来就是系统正常运行所必须要的，我们可以简称它为系统账号，例如bin，daemon，adm，nobody，不可随意删

  + > 账号名称：用来对应UID。
    >
    > 密码：早期就是放在这个字段上，但会被所有的程序读取，后来将密码放在/etc/shadow。所以这里是一个x
    >
    > UID：这个就是用户标识符。
    >
    > >0：系统管理员。想让其他账号也有root权限，就将该账号的UID改为0即可。一个系统上面的系统管理员不见得只有root。
    > >
    > >1～499：系统账号。除0之外，其他的UID权限与特性并没有不一样。通常不可登录；
    > >
    > >> 1～99:由distributions自行创建的系统账号；
    > >>
    > >> 100～499:若用户有系统账号需求时，可以使用的账号UID。
    > >
    > >500～65535:（可登录账号）：给一般用户用的。目前内核（2.6x版）已经可以支持到2^32-1这么大的UID号码
    >
    > GID：与/etc/group有关！只是用来规定组名与GID的对应而已。
    >
    > 用户信息说明列：解释账号意义。
    >
    > 主文件夹：用户主文件夹
    >
    > Shell：默认bash。注意/sbin/nologin这个shell可以用来替代成让账号无法取得shell环境的登录操作。



+ /etc/shadow文件结构，共9个字段 

3.有效与初始用户组：groups，newgrp



### 14.2 账号管理

***

1.新增与删除用户：useradd，相关配置文件，passwd，usermod，userdel



2.用户功能



3.新增与删除用户组



4.账号管理实例



### 14.3 主机的具体权限规划：ACL的使用

***

1.什么是ACL



2.如何启动ACL



3.ACL的设置技巧：getfacl，setfacl



### 14.4 用户身份切换

***

1.su



2.sudo



### 14.5 用户的特殊shell与PAM模块

***

1.特殊的shell，/sbin/nologin



2.PAM模块简介



3.PAM模块设置语法



4.常用模块简介



5.其他相关文件



### 14.6 Linux主机上的用户信息传递

***

1.查询用户：w，who，last，lastlog

+ 目前已登录在系统上面的用户。

  + 通过w；who来查询
  + 通过last；lastlog检查用户登录的状况

+ w;who

  + 第一行显示目前的时间、开机（up）多久，几个用户在系统上的平均负载等；
  + 第二行只是各个项目的说明；
  + 第三行以后，每行代表一个用户。

  

2.用户对谈：write，mesg，wall（需用户在线才能收到信息）

+ write 用户账号 [用户所在终端接口]
  + write gld pts/2
  + ctrl+d来结束
+ mesg
  + mesg：可查看状态
  + mesg n：不接收消息
  + mesg y：接收消息
  + 不可拒接root消息
+ wall 广播
  + wall “I will shutdown my linux server...”



3.用户邮件信箱：mail（不在线也可）

+ mailbox：/var/spool/mail
+ mail username@localhost -s"邮件标题"
  + 寄信给本机，@localhost可不写
  + mail gld -s "nice to meet you"
  + 传输文件内容：`mail gld -s "nice to meet you" < filename`
+ 收信：mail
  + ？：显示mail内部命令



### 14.7 手动新增用户

***

1.一些检查工具

+ pwck：用户检查
  + 检查/etc/passwd这个账号配置文件内的信息，与实际的主文件夹是否存在等信息，
  + 比较/etc/passwd /etc/shadow的信息是否一致
+ grpck：用户组检查
+ pwconv
  + 将/etc/passwd内的账号与密码移动到/etc/shadow当中
  + 比较/etc/passwd及/etc/shadow，若/etc/passwd内存在的账号并没有对应的/etc/shadow密码时，则pwconv会去/etc/login.defs取用相关的密码数据，并新建改账号的/etc/shadow数据；
  + 若/etc/passwd内存在加密后的密码数据时，则pwconv会将该密码列移动到/etc/shadow内，并将原本的/etc/passwd内相对应的密码列变成x！
+ pwunconv
  + 将/etc/shadow内的密码列数据写回/etc/passwd中，并且删除/etc/shadow文件。
+ chpasswd
  + 可以读入没加密前的密码，并且经过加密后，将加密后的密码写入/etc/shadow当中。
  + 默认使用DES加密方法来加密
  + chpasswd -m来使用CentOs 5.x默认的MD5加密方法
  + passwd --stdin类似
  + echo "user:password" | chpasswd -m



2.特殊账号（如纯数字账号）的手工新建



4.批量新建账号模版（适用于passwd--stdin参数）



5.批量新键账号的范例（适用于连续数字，如学号）



