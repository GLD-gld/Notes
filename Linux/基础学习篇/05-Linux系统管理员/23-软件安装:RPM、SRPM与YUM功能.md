### 23.1 软件管理器简介

***

1.Linux界的两大主流：RPM与DPKG

+ dpkg

  + 最早由Debian Linux社区所开发出来的。
  + B2D，Ubuntu

+ RPM

  + 最早是由Red Hat这家公司开发出来的。
  + Fedora，CentOS，SuSE

+ 在线升级

  ```tex
  distribution代表				软件管理机制				使用命令								在线升级机制（命令）
  Red Hat/Fedora					RPM								rpm，rpmbuild					YUM（yum）
  Debian/Ubuntu						DPKG							dpkg									 APT（apt-get）
  ```

  

2.什么是RPM与SRPM

+ RPM：RedHat Package Manager
+ 通常不同的distribution所发布的RPM文件并不能用在其他的distributions上



+ SRPM：Source RPM
  + 也就是这个RPM文件里面含有源代码，这个SRPM所提供的软件内容并没有经过编译。
  + SRPM的扩展名是以***.src.rpm这种格式来命名的。
+ SRPM安装
  + 先将该软件以RPM管理的方式编译，此时SRPM会被编译成为RPM文件；
  + 然后将编译完成的RPM文件安装到Linux系统当中。
+ 因为RPM文件需要在相同的Linux环境下才能够安装，而SRPM既然是源代码的格式，自然我们就可以通过修改SRPM内的参数设置文件，然后重新编译生成能适合我们Linux环境的RPM文件。



3.什么是i386、i586、i686、noarch、x86_64



4.RPM的优点



5.RPM属性依赖的解决方式：YUM在线升级

+ 当客户端有升级、安装的需求时，yum会向容器要求清单的更新，等到清单更新到本机的/var/cache/yum里面后，等一下更新时就会用这个本机清单与本机的RPM数据库进行比较，这样就知道该下载什么软件。接下来yum会跑到容器服务器（yum server）下载所需要的软件，然后再通过RPM的机制开始安装软件。



### 23.2 RPM软件管理程序：rpm

***

1.RPM默认安装的路径

+ /var/lib/rpm

```tex
/etc							一些设置文件放置的目录，例如/etc/crontab
/usr/bin					一些可执行文件
/usr/lib					一些程序使用的动态函数库
/usr/share/doc		一些基本的软件使用手册与帮助文档
/usr/share/man		一些man page文件
```





2.RPM安装（install）

+ `rpm -ivh package_name`
  + -i：install的意思
  + -v：查看更详细的安装信息画面
  + -h：以安装信息栏显示安装进度



3.RPM升级与更新（upgrade/freshen）

+ -Uvh：没有的软件安装，有的软件更新
+ -Fvh：没有的软件不安装，有的软件更新



4.RPM查询（query）

+ `rpm -qa` `rpm -q[licdR] 已安装的软件名称` `rpm -qf 存在于系统上面的某个文件名` `rpm -qp [licdR] 未安装的某个文件名称`
  + -q：仅查询，后面接的软件名称是否有安装；
  + -qa：列出所有的已经安装在本机Linux系统上面的所有软件名称；
  + -qi：列出该软件的详细信息（information），包含开发商、版本于说明等；
  + -ql：列出该软件所有的文件与目录所在完整文件名（list）；
  + -qc：列出该软件的所有设置文件（找出在/etc/下面的文件名而已）；
  + -qd：列出该软件的所有帮助文件（找出与man有关的文件而已）；
  + -qR：列出与该软件有关的依赖软件所含的文件（Required的意思）；
  + -qf：由后面接的文件名称找出该文件属于哪一个已安装的软件。
  + -qp：找出某个RPM文件内的信息，而非已安装的软件信息



5.RPM验证与数字证书（Verify/Signature）

+ 使用/var/lib/rpm下面的数据库内容来比较目前Linux系统的环境下的所有软件文件。
+ `rpm -Va`  `rpm -V 已安装的软件名称` `rpm -Vp 某个RPM文件的文件名` `rpm -Vf 在系统上面的某个文件`
  + -V：后面加的是软件名称，若该软件所含的文件被改动过，才会列出来；
  + -Va：列出目前系统上面所有可能被改动过的文件；
  + -Vp：后面加的是文件名称，列出该软件内可能被改动过的文件；
  + -Vf：列出某个文件是否被改动过。



+ S（file Size differs）：文件的容量大小是否被改变；
+ M（Modedeffers）：文件的类型或文件的属性（rwx）是否被改变，如是否可执行等参数已被改变；
+ 5（MD5 sum differs）：MD5这一种指纹码的内容已经不同；
+ D（Device major/minor number mis-match）：设备的主/次代码已经改变
+ L（readLink（2）path mis-match）：Link路径已被改变；
+ U（User ownership differs）：文件的所有者已被改变；
+ G（Group ownership differs）：文件的所属用户组已被改变；
+ T（m Time differs）：文件的创建时间已被改变。



+ c：设置文件（config file）
+ d：文档（documentation）
+ g：“鬼”文件（ghost file），通常是该文件不被某个软件所包含，较少发生；
+ l：授权文件（license file）；
+ r：自述文件（read me）



+ 数字证书（digital signature）

+ 安装一个RPM文件时：

  + 首先你必须要先安装原厂发布的公钥文件；
  + 实际安装原厂的RPM软件时，rpm命令回去读取RPM文件的证书信息，与本机系统内的证书信息比较；
  + 若证书相同则予以安装，若找不到相关的证书信息时，则给予警告并且停止安装。

+ ```shell
  locate GPG-KEY
  find /etc -name '*GPG-KEY'
  
  rpm --import /etc/pki/rpm-gpg/....
  rpm -qa | grep pubkey
  ```

  



6.卸载RPM与重建数据库（erase/rebuilddb）

+ 删除
  + `rpm -e package_name`
+ RPM数据库/var/lib/rpm/内的文件损坏：需重建数据库
  + `rpm --rebuilddb`



### 23.3 SRPM的使用：rpmbuild

***

1.利用默认值安装SRPM文件（--rebuild/--recompile）



2.SRPM使用的路径与需要的软件



3.设置文件的主要内容：（*.spec）



4.SRPM的编译命令（-ba/-bb）



5.一个打包自已软件的范例



### 23.4 YUM在线升级机制

***

1.利用yum进行查询、安装、升级与删除功能

+ 查询功能：yum [list|info|search|provides|whatprovides]参数
+ yum [option] [查询工作项目] [相关参数]
+ [option]
  + -y：当yum要等待用户输入时，这个选项可以自动提供yes的响应；
  + --installroot=/some/path：将该软件安装在/some/path中而不使用默认路径
+ [查询工作项目] [相关参数]：
  + search：搜索某个软件名称或者是描述（description）的重要关键字；
  + list：列出目前yum所管理的所有的软件名称与版本，有点类似于rpm -qa；
  + info：同上，不过有点类似于rpm -qai的运行结果；
  + provides：从文件去搜索软件！类似于rpm -qf的功能！



+ 搜索磁盘阵列（raid）相关的软件有哪些
  + `yum search raid`
+ 找出mdadm这个软件的功能为何
  + `yum info mdadm`
+ 列出yum服务器上面提供的所有软件名称
  + `yum list`
+ 列出目前服务器上可供本机进行升级的软件有哪些
  + `yum list updates`
+ 列出提供passwd这个文件的软件有哪些
  + `yum provides passwd`
+ 找出pam为开头的软件名称有哪些
  + `yum list pam*`



+ 安装/升级功能：yum[install|update] 软件
+ yum [option] [查询工作项目] [相关参数]
  + install：后面接要安装的软件
  + update：后面接要升级的软件，若要整个系统都升级，就直接update即可。



+ 删除功能：yum [remove] 软件



2.yum的设置文件

+ 如果你连接到CentOS的镜像站点（如ftp.twaren.net/Linux/CentOS）后，就会发现里面有一堆链接，那些链接就是这个yum服务器所提供的容器里，包括addons、centosplus、extras、fasttrack、os、updates等容器。
+ http:ftp.twaren.net/Linux/CentOS
+ 最重要的特色就是那个“repodata”的目录。该目录就是分析RPM软件后所产生的软件属性依赖数据放置处。



+ 配置文件解析：CentOS-Base.repo

+ ```shell
  [base]
  name=CentOS-$releasever - Base
  mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
  baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
  gpgcheck=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
  ```

+ [base]：代表容器的名字。中括号一定要存在，里面的名称则可以随意取，但是不能有两个相同的容器名称，否则yum会不知道该到哪里去找容器相关软件列表文件。

+ name：只是说明一下这个容器的意义而已，重要性不高！

+ mirrorlist=：列出这个容器可以使用的镜像站点，如果不想使用，可以批注掉这行。

+ baseurl：这个最重要，因为后面接的就是容器的实际网址。mirrorlist是由yum程序自行去找镜像站点，baseurl则是指定固定的一个容器网址。我们刚才找到的网址放到这里来。

+ enable=1：就是让这个容器被启动。如果不想启动可是使用enable=0

+ gpgcheck=1：还记得RPM的数字证书吗？这就是指定是否需要查阅RPM文件内的数字证书。

+ gpgkey=：就是数字证书的公钥文件所在位置。使用默认值即可。



+ 列出目前yum server所使用的容器有哪些
  + `yum repolist all`



+ 修改容器产生的问题与解决之道
+ yum clean [packages|headers|all]
  + packages：将已下载的软件文件删除；
  + headers：将下载的软件文件头删除；
  + all：将所有容器数据都删除。
+ 删除已下载过的所有容器的相关数据（含软件本身与列表）
  + `yum clean all`



3.yum的软件组功能

+ yum [组功能] [软件组]
  + grouplist：列出所有可使用的组列表，例如Development Tools之类的；
  + groupinfo：后面接group name，则可了解该group内含的所有组名称；
  + groupinstall：这个好用！可以安装一整组的软件，相当不错！
  + groupremove：删除某个组。



4.全系统自动升级

+ yum -y update



### 23.5 管理的抉择：RPM还是Tarball

***

+ 优先选择原厂的RPM功能
+ 选择软件官方网站发布的RPM或者是提供的容器网址
+ 利用Tarball安装特殊软件
+ 用Tarball测试新版软件