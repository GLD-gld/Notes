### 17.1 什么是进程（process）

***

1.进程与程序（process&program）

+ 进程：一个程序被加载到内存当中运行，那么在内存内的那个数据就被称为进程（process）。
  + 程序（program）：通常为二进制程序放置在存储媒介中（如硬盘、光盘、软盘、磁带等），以物理文件的形式存在；
  + 进程（process）：程序被触发后，执行者的权限与属性、程序的程序代码与所需数据等都会被加载到内存中，操作系统并给予这个内存内的单元一个标识符（PID），可以说，进程就是一个正在运行中的程序。
+ 子进程与父进程
+ fork and exec：过程调用的流程
  + 系统先以fork的方式复制一个与父进程相同的暂存进程，这个进程与父进程的唯一的区别就是PID不同！
  + 但会多一个PPID参数，这个PPID就是父进程的进程标识符。
+ 系统或网络服务：常驻在内存的进程
  + crond启动后会在后台当中一直持续不断运行
  + 常驻进程就会被称为服务（daemon）
  + atd，syslog，Apache，named，postfix，vsftpd



2.Linux的多用户、多任务环境

+ 多用户环境
  + 多种不同的账号，每中账号都有其特殊的权限
+ 多任务行为
  + CPU可在多个工作间切换，CPU调度
+ 多重登录环境的七个基本终端窗口
  + 6个命令行界面的登录窗口，以及一个图形界面。可以是不同的人
+ 特殊的进程管理行为
  + 重开一个窗口，删除有问题的进程
+ bash环境下的工作管理（job control）
  + cp file1 file2 &
  + &：放在后台执行
+ 多用户、多任务的系统资源分配问题考虑



### 17.2 工作管理（job control）

***

1.什么是工作管理

+ 登录系统取得bash shell之后，在单一终端机下同时进行多个工作的行为管理。
+ 在进行工作管理的行为中，其实每个工作都是目前bash的子进程，即彼此之间是有相关性的。我们无法以job control的方式有tty1的环境去管理tty2的bash。
+ 这些工作所触发的进程必须来自于你shell的子进程（只管理自己的bash）
+ 前台：你可以控制与执行命令的这个环境称为前台（foreground）的工作；
+ 后台：可以自行运行的工作，可使用bg/fg调用该工作；
+ 后台中“执行”的进程不能等待terminal/shell的输入（input）



2.job control的管理

+ 直接将命令丢到后台中“执行”的&
  + `tar -zpcvf /tmp/etc.tar.gz /etc > /tmp/log.txt 2>&1 & `
+ 将目前的工作丢到后台中“暂停”：ctrl+z
+ 查看目前的后台工作状态：jobs
  + jobs [-lrs]
  + -l：除了列出job number与命令串之外，同时列出PID的号码；
  + -r：仅列出正在后台run的工作；
  + -s：仅列出正在后台当中暂停（stop）的工作。
+ 将后台工作拿到前台来处理：fg
  + fg %jobnumber
  + +：代表最近被放到后台的工作号码
  + -：代表最近最后第二个被放置到后台中的工作号码
+ 让工作在后台下的状态变成运行中：bg
  + bg %jobnumber
+ 管理后台当中的工作：kill
  + kill -signal %jobnumber
  + -l：这个是L的小写，列出目前kill能够使用的信号（signal）有哪些
  + signal：man 7 signal可知
  + -1：重新读取一次参数的配置文件（类似reload）
  + -2：代表与由键盘输入ctrl-c同样的操作
  + -9：立刻强制删除一个工作
  + -15：以正常的程序方式终止一项工作。默认值
  + -17：相当于用键盘输入ctrl-z来暂停一个进程的进行



3.脱机管理问题

+ 工作管理的后台依旧与终端机有关。工作状态下脱机了，工作是不会继续进行的。
+ at：是将工作放置到系统后台，而与终端机无关。
+ nohup：可以在脱机或注销系统后，还能够让工作继续进行。
  + nohup [命令与参数] ：在终端机前台中工作
  + nohup [命令与参数] & ：在终端机后台中工作
+ nohup并不支持bash内置的命令，因此你的命令必须要是外部命令才行。



### 17.3 进程管理

***

1.进程的查看

+ ps：将某个时间点的进程运行情况选取下来
  + `ps aux` `ps -lA`查看系统所有的进程数据
  + `ps axjf`连同部分进程树状态
  + -A：所有的进程均显示出来，与-e具有同样的作用；
  + -a：不与terminal有关的所有进程
  + -u：有效用户（effective user）相关的进程
  + x：通常与a这个参数一起使用，可列出较完整信息。
  + l：较长、较详细地将该PID的信息列出；
  + j：工作的格式（jobs format）
  + -f：做一个更为完整的输出。
+ 查看系统所有进程：psaux
  + ps aux | egrep '(cron|syslog)'
+ top：动态查看进程的变化
  + top [-d 数字] | top [-bnp]
  + -d：后面可以接秒数，就是整个进程界面更新的秒数。默认是5秒。
  + -b：以批次的方式执行top
  + -n：指定某些个PID来进行查看检测而已
  + 可使用的按键命令；
    + ？：显示top当中可以输入的按键命令
    + P：以CPU的使用资源排序显示
    + M：以内存的使用资源排序显示
    + N：以PID来排序
    + T：由该进程使用的CPU时间累积（TIME+）排序
    + k：给予某个PID一个信号（signal）
    + r：给予某个PID重新制定一个nice值
    + q：离开top软件的按键
    + zombie：显示的是有几个僵尸进程。<defunct>是僵尸进程
  + 以top的信息进行2次，然后将结果输出到/tmp/top.txt
    + top -b -n 2 > /tmp/top.txt
  + 自己bash的PID可由$$变量取得：echo $$
+ pstree：进程之间的相关性
  + `pstree [-A|U] [-up]`
  + -A：各进程树之间的连接以ASCII字符来连接；
  + -U：各进程树之间的连接以utf8码的字符来连接，在某些终端接口下可能会有错误
  + -p：同时列出每个进程的PID
+ **所有的进程都是依附在init这个进程下面的，这个进程的PID是1号。因为它是由Linux内核所主动调用的第一个进程！**



2.进程的管理

+ 如果想要将某个莫名其妙的登陆者的连接删除的话，就可以通过使用pstree -p找到相关进程



3.关于进程的执行顺序

+ PRI：（priority）PRI值越低越优先。
+ 这个PRI值是有内核动态调整的，用户无法直接调整PRI值的。
+ PRI（new）= PRI（old）+ nice
+ nice：新执行的命令即给予新的nice值
  + -n：后面接一个数值，范围为-20～19
+ renice：以存在进程的nice重新调整
  + renice [number] PID



4.系统资源的查看

+ free：查看内存使用情况
+ `free [-b|-k|-m|-g] [-t]`
  + -b，-k，-m，-g：显示单位
  + -t：在输出的最终结果中显示物理内存与swap的总量。



+ uname：查看系统与内核相关信息
+ `uname [-asrmpi]`
  + -a：所有系统相关的信息，
  + -s：系统内核名称
  + -r：内核版本
  + -m：本系统的硬件名称
  + -p：CPU的类型，与-m类似，只是显示的是CPU的类型
  + -i：硬件的平台
+ uptime：查看系统启动时间与工作负载，就是显示top界面的最上面一行
+ netstat：跟踪网络
+ `netstat -[atunlp]`
  + -a：将目前系统上所有的连接、监听、Socket数据都列出来；
  + -t：列出tcp网络数据包的数据；
  + -u：列出udp网络数据包的数据；
  + -n：不列出进程的服务名称，以端口号（port number）来显示；
  + -l：列出目前正在网络监听（listen）的服务；
  + -p：列出该网络服务的进程PID。
+ dmesg：分析内核产生的信息
  + `dmesg|more`  输出所有的内核开机时的信息
+ vmstat：检测系统资源变化
+ `vmstat [-a] [延迟 [总计检测次数]]`  cpu/内存等信息
+ `vmstat [-fs]`  内存相关
+ `vmstat [-S 单位]`  设置显示数据的单位
+ `vmstat [-d]`  与磁盘有关
+ `vmstat [-p 分区]`  与磁盘有关
  + -a：使用inactive/active（活跃与否）替代buffer/cache的内存输出信息；
  + -f：开机到目前为止系统复制（fork）的进程数；
  + -s：将一些事件（开机至目前为止）导致的内存变化情况列表说明；
  + -S：后面可以接单位，让显示的数据有单位。例如K/M取代bytes的容量；
  + -d：列出磁盘的读写总量统计表；
  + -p：后面列出分区，可显示该分区的读写总量统计表
+ 统计目前主机CPU状态，每秒一次，共计三次！
  + `vmstat 1 3`
+ 系统上面所有的磁盘的读写状态
  + `vmstat -d`



### 17.4 特殊文件与程序

***

1.具有SUID/SGID权限的命令执行状态

+ SUID的权限会生效是由于具有该权限的程序被触发，一个程序被触发会变成进程，所以执行者可以具有程序所有者的权限就是在该程序变成进程的那个时候。

+ 例：触发passwd之后，会取得一个新的进程与PID，该PID产生时通过SUID来给予该PID特殊的权限设置。

  

2./proc/* 代表的意义

+ 内存当中的数据都是写入到/proc/*这个目录xia
+ cmdline：这个进程被启动的命令串
+ environ：这个进程的环境变量内容
+ /proc/cmdline：加载kernel时所执行的相关参数！查阅此文件，可了解系统是如何启动的
+ /proc/cpuinfo：本机的CPU的相关信息，包含频率、类型与运算功能等
+ /proc/devices：这个文件记录了系统各个主要设备的主要设备代号，与mknod有关
+ /proc/filesystems：目前系统已经加载的文件系统
+ /proc/interrupts：目前系统上面的IRQ分配状态
+ /proc/ioports：目前系统上面各个设备所配置的I/O地址
+ /proc/kcore：这个就是内存的大小
+ /proc/loadavg：top及uptime的上面三个平均数值记录
+ /proc/meminfo：使用free列出的内存信息
+ /proc/modules：目前Linux已经加载的模块列表，也可以想成是驱动程序
+ /proc/swaps：使用的分区记录
+ /proc/partitions：使用fdisk -l会出现目前所有的分区，这里也有
+ /proc/pci：在PCI总线上面每个设备的详细情况！可用lspci来查阅
+ /proc/uptime：就是用uptime的时候会出现的信息
+ /proc/version：内核的版本，就是用uname -a显示的内容
+ /proc/bus/*：一些总线的设备，还有USB的设备也记录在此



3.查询已打开文件或已执行程序打开的文件

+ fuser：通过文件（或文件系统）找出正在使用该文件的程序
  + `fuser [-umv] [-k [i] [-signal]]` file /dir
  + -u：除了进程的PID之外，同时列出该进程的所有者；
  + -m：后面接的那个文件名会主动上提到该文件系统的所顶层，对umount不成功很有效！
  + -v：可以列出每个文件与程序还有命令的完整相关性！
  + -k：找出使用该文件/目录的PID，并试图以SIGKILL这个信号给予该PID
  + -i：必须与-k配合，在删除PID之前会先询问用户意愿
  + -signal：-1 -15等，默认-9



+ lsof：列出被进程所打开的文件名
  + `lsof [-aUu] [+d]`
  + -a：多项数据需要“同时成立”才显示结果时！
  + -U：仅列出Unix like系统的socket文件类型
  + -u：后面接username，列出该用户相关进程所打开的文件
  + +d：后面接目录，即找出某个目录下面已经被打开的文件



+ pidof：找出某个正在执行的进程的PID
  + `pidof [-sx] program_name`
  + -s：仅列出一个PID而不列出所有的PID
  + -x：同时列出该program name可能的PPID那个进程的PID



### 17.5 SELinux初探

***

1.什么是SELinux

+ Security Enhanced Linux：安全强化的Linux
+ SELinux是在进行程序、文件等权限设置依据的一个内核模块。
+ 由于启动网络服务的也是程序，因此刚好也是能够控制网络服务能否访问系统资源的一道关卡！



+ 传统的文件权限与账号关系，自主访问控制，DAC（Discretionary Access Control）
  + 基本上，就是依据进程的所有者与文件资源的rwx权限来决定有无访问的能力
  + root具有最高的权限
  + 用户可以取得进程来更改文件资源的访问权限



+ 以策略规则制定特定程序读取特定文件：委托访问控制，MAC（Mandatory AccessControl）
  + 可以针对特定的进程与特定的文件资源来进行权限的控制！
  + 也就是说，即使是root，在使用不同的进程时，所能取得的权限并不一定是root，而得看当时该进程的设置而定。



+ SELinux提供一些默认策略，并在该策略内提供多个规则（rule），让你可以选择是否启用该控制规则。



2.SELinux的运行模式

+ SELinux是通过MAC的方式来管控进程，它控制的主体是进程，而目标则是该进程能否读取的“文件资源”。
+ 主体（Object）
  + SELinux主要想要管理的就是进程。
+ 策略（Policy）
  + targeted：针对网络服务限制较多，针对本机限制较少，是默认的策略；
  + strict：完整的SELinux限制，限制方面较为严格。
  + 建议使用默认的targeted策略即可
+ 安全上下文（security context）
  + 主体与目标的安全上下文必须一致才能都顺利访问。
+ 顺序：
  + 主体程序必须要通过SELinux策略内的规则放行后，就可以与目标资源进行安全上下文的比较，
  + 若比较失败则无法访问目标，若比较成功则可以开始访问目标。
  + 最终能否访问目标还是与文件系统的rwx权限设置有关。
+ 查看安全上下文：ls -Z
  + Identify:role:type	身份识别:角色:类型
+ 身份标识：（Identify）
  + root：表示root账号身份
  + system_u：表示系统程序方面的标识，通常就是进程
  + user_u：代表的是一般用户账号相关的身份
+ 角色（role）
  + object_r：代表的是文件或目录等文件资源
  + system_r：代表的是进程，不过一般用户也会被指定成为system_r
+ 类型（Type，最重要）
  + type：在文件资源（Object）上面称为类型（Type）
  + domain：在主体程序（Subject）中则称为域（domain）
  + domain需要与type搭配，则该程序才能够顺利读取文件资源



3.SELinux的启动、关闭与查看

+ Enforcing：强制模式，代表SELinux正在运行中，且已经正确开始限制domain/type了
+ permissive：宽容模式，代表SELinux正在运行中，不过仅会有警告信息并不会实际限制访问，调试之用。
+ disabled：关闭，SELinux并没有实际运行。
+ 查看SELinux模式：getenforce



+ 查看SELinux的策略为何：sestatus
  + `sestatus [-vb]`
  + -v：检查列于/etc/sestatus.conf内的文件与程序的安全上下问内容；
  + -b：将目前策略的规则布尔值列出，即某些规则（rule）是否要启动（0/1）之意
+ 配置文件：/etc/selinux/config

+ SELinux的启动与关闭
  + 改变策略，改变模式都要重新启动。
  + SELinux运行下只能切换为enforcing或permissive模式，不能直接关闭SELinux。
  + SELinux关闭的状态到打开的状态也需要重新启动。
  + 启动SELinux，可调整配置文件为enforcing，并指定targeted。
  + 并且到/boot/grub/menu.lst这个文件去，看看内核有无关闭SELinux。
  + 确认kernel后面不可以接selinux=0这个选项。
  + 当selinux=0时，内核会自动忽略/etc/selinux/config的设置值，而直接忽略SELinux的加载。
+ 切换模式
  + `setenforce [0|1]`
  + 0：转成permissive宽容模式；
  + 1：专成Enforcing强制模式。
  + 无法在Disabled的模式下面进行模式的切换。



4.SELinux网络服务运行范例



5.SELinux所需的服务



6.SELinux的策略与规则管理