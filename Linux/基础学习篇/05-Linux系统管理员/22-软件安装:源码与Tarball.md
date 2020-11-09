### 22.1 开放源码的软件安装与升级简介

***

1.什么是开放源码、编译程序与可执行文件

+ Linux系统上真正识别的可执行文件其实是二进制文件
+ 可执行文件类：ELF 32-bit LSB executable
+ 一般的script：text executables
+ 程序代码文件其实就是一般的纯文本文件



2.什么是函数库

+ 函数库：类似子程序的角色，可以被调用来执行的一段功能函数
+ 动态和静态函数库
+ 内核相关信息大多放置在 /usr/include，/lib，/usr/lib里面



3.什么是make与configure

+ 可使用make这个命令的相关功能来进行编译过程的命令简化。

+ 执行configure来新建Makefile，再以make来调用所需要的数据来编译即可。



4.什么是Tarball的软件

+ Tarball文件，就是将软件的所有源码文件先以tar打包，然后再以压缩技术来压缩，通常最常见的就是以gzip来压缩了。
+ tarball文件一般的扩展名就会写成*.tar.gz或者是简写为 *.tgz 或 *.tar.bz2之类的
+ 解压缩后：
  + 源代码文件；
  + 检测程序文件（可能是configure或config等文件名）
  + 本软件的简易说明与安装说明（INSTALL或README）



5.如何安装与升级软件

+ 直接以源码通过编译来安装与升级；
+ 直接以编译好的二进制程序来安装与升级。
+ 安装：
  + 将Tarball由厂商的网页下载下来；
  + 将Tarball解压缩，生成很多的源码文件；
  + 开始以gcc来进行源码的编译（会生成目标文件）；
  + 然后以gcc进行函数库、主程序、子程序的链接，以形成主要的二进制文件；
  + 将上述的二进制文件以及相关的配置文件安装至自己的主机上面。



### 22.2 使用传统语言进行编译的简单范例

****

1.单一程序：打印Hello World

+ 安装所需所有软件
  + `yum groupinstall "Development Tools"`
+ vim hello.c
+ 没有加任何参数，则执行文件的文件名会被自动设置为a.out这个可执行文件
  + gcc hello.c  
+ 添加-c参数，则会生成hello.o这个目标文件,再以-o参数生成可执行文件
  + gcc -c hello.c
  + gcc -o hello hello.o



2.主程序、子程序链接：子程序的编译

+ 编写所需要的主程序、子程序
+ 进行程序的编译与链接（Link）
  + `gcc -c thanks.c thanks2.c`
  + `gcc -o thanks.o thanks2.o`
  + `./tanks.o`
+ **由于我们的源码文件有时并非仅只有一个文件，所以我们无法直接进行编译。这个时候就需要先生成目标文件，然后再以链接制作成为二进制可执行文件。 **
+ **如果有一天，你更新了thanks2.c这个文件的内容，则你只要重新编译thanks2.c来产生新的thanks2.o，然后再以链接制作出新的二进制可执行文件即可，而不必重新编译其他没有改动过的源码文件**



+ gcc -O -c thanks.c thanks2.c      -O：为生成优化的参数
+ gcc -Wall -c thanks.c thanks2.c     -Wall：为产生更详细的编译过程信息。



3.调用外部函数库：加入链接的函数库

+ gcc sin.c -lm -L/lib -L/usr/lib

  + -l：是加入某个函数库（library）的意思；
  + -m：则是libm.so这个函数库，其中lib与扩展名（.a或.so）不需要写
  + -L：函数库的Path，默认是将函数库放置在/lib与/usr/lib当中

  

+ #include <stdio.h>

  + 将一些定义数据由stdio.h这个文件读入，包括printf的相关配置
  + 默认放置在/usr/include/stdio.h
  + `gcc sinc -lm -I/usr/include`
  + -I/path后面接的路径就是设置去搜索相关的include文件的目录

  

4.gcc的简易用法（编译、参数与链接）

+ 仅将源码编译成为目标文件，并不制作链接等功能
  + `gcc -c hello.c`
+ 在编译的时候，依据操作环境给予优化执行速度
  + `gcc -O hello.c -c`
+ 在进行二进制文件制作时，将链接的函数库与相关的路径填入
  + `gcc sin.c -lm -L/usr/lib -I/usr/include`
  + -lm指的是libm.so或libm.a这个函数库文件
  + -L后面接的路径是刚才上面那个函数库的搜索目录
  + -I后面接的是源码内的include文件的所在目录
+ 将编译的结果输出成某个特定文件名
  + `gcc -o hello hello.c`
+ 在编译的时候，输出较多的信息说明
  + `gcc -o hello hello.c -Wall`



### 22.3 用make进行宏编译

***

1.为什么要用make

+ 新编辑makefile这个规则文件，内容只哟啊制作出main这个可执行文件

+ vim makefile

  ```makefile
  main: main.o haha.o sinvalue.o cosvalue.o
  	gcc -o main main.o haha.o sinvalue.o cosvalue.o -lm
  ```

+ 尝试使用makefile制定的规则进行编译的行为

  + `make`

+ 在不删除任何文件的情况下，重新执行一次编译的操作

  + `make`
  + 只会进行更新的操作而已

+ **make会主动去判断每个目标相关的源码文件，并直接予以编译，最后再直接进行链接的操作**



+ 好处：
  + 简化编译时所需要执行的命令；
  + 若在编译完成之后，修改了某个源码文件，则make仅会针对被修改了的文件进行编译，其他的目标文件不会被更改；
  + 最后可以依照相依性来更新（update）执行文件。



2.makefile的基本语法与变量

+ 基本规则

  ```makefile
  目标（target）：目标文件1 目标文件2
  	gcc -o 欲新建的可执行文件 目标文件1 目标文件2
  ```

+ 在makefile当中的#代表批注

+ <tab> 需要在命令行（例如gcc这个编译程序命令）的第一个字符；

+ 目标（target）与相关文件（就是目标文件）之间需以“:"隔开



+ 通过shell script来简化makefile

  ```makefile
  LIBS = -lm
  OBJS = main.o haha.o sin_value.o cos_value.o
  CFLAGES = -Wall
  main: ${OBJS}
  	gcc -o main ${OBJS} ${LIBS}
  clean:
  	rm -f main ${OBJS}
  ```



+ make命令行后面加上的环境变量为第一优先；
+ makefile里面指定的环境变量为第二优先；
+ shell原本具有的环境变量第三优先。
+ 特殊变量
  + $@：代表目前的目标（target）
  + 这里$@代表main



### 22.4 Tarball的管理与建议

***

1.使用源码管理软件所需要的基础软件

+ Tarball的安装是可以跨平台的，因为C语言的程序代码在各个平台上面是可以共通的，只是需要的编译程序可能并不相同而已。
+ gcc或cc等C语言编译程序（compiler）
+ make及autoconfig等软件
+ 需要Kernel提供的Library以及相关的Include文件



2.Tarball安装的基本步骤

+ 取得源文件：将tarball文件在/usr/local/src目录下解压缩；
+ 取得步骤流程：进入新建立的目录下面，去查阅INSTALL与README等相关文件内容（很重要的步骤）；
+ 相关属性软件安装：根据INSTALL/README的内容查看并安装好一些相关的软件（非必要）；
+ 建立makefile：以自动检测程序（configure或config）检测操作环境，并建立Makefile这个文件；
+ 编译：以make这个程序并使用该目录下的Makefile作为它的参数配置文件，来进行make（编译或其他）的操作；
+ 安装：以make这个程序，并以Makefile这个参数配置文件，依据install这个目标（target）的指定来安装到正确的路径。



+ 执行方式：
  + ./configure
  + makeclean
  + make
  + make install



3.一般Tarball软件安装的建议事项（如何删除、升级）

+ 单一软件的文件都在一个目录之下，移除软件方便。只要将该目录一出即可视为该软件已经被删除。
  + 例删除apache
  + `rm -rf /usr/local/apache`
+ 最好将tarball的原始数据解压缩到/usr/local/src当中；
+ 安装时，最好安装到/usr/local这个默认路径下；
+ 考虑将来的反安装步骤，最好可以将每个软件单独安装在/usr/local下面；
+ 为安装到单独目录的软件的man page 加入 man path搜索。
+ 如果安装的软件放置在/usr/local/software/中，那么在man page搜索的设置中可能就得要在/etc/man.config内的40～50行左右处添加：MANPATH/usr/local/software/man



4.一个简单的范例（利用ntp来示范）

+ 解压缩下载的tarball，并参阅README/INSTALL文件
  + `cd /usr/local/src`
  + `tar -zxvf /root/ntp-4.2.4p7.tar.gz`
  + `cd ntp-4.2.4p7`
+ 检查configure支持参数，并实际生成makefile规则文件
  + `./configure --help | more`
  + --prefix=PREFIX     install architecture-independent files in PREFIX（这个软件将来要安装到哪个目录去，默认是/usr/local）
  + --enable-all-clocks    + include all suitable non-PARSE clocks:
  + --enable-parse-clocks  - include all suitable PARSE clocks:
  + `./configure --perfix=/usr/local/ntp --enable-all-clocks --enable-parse-clocks`
+ 最后开始编译与安装
  + `make clean;make`
  + `make check`
  + `make install`



5.利用patch更新源码



### 22.5 函数库管理

***

1.动态与静态函数库



2.ldconfig与/etc/ld.so.conf



3.程序的动态函数库解析：ldd



### 22.6 检验软件的正确性

***

1.每个文件独特的指纹验证数据

+ md5sum/sha1sum

  + `md5sum/sha1sum [-bct] filename`

    `md5sum/sha1sum [--status|--warn] --check filename`

  + -b：使用二进制的读取方式，默认为Windows/DOS文件类型的读取方式；

  + -c：检验文件指纹；

  + -t：以文本类型来读取文件指纹。

+ 通常为以下重要文件进行指纹数据库的创建，将下面这些文件新建数据库：

  + /etc/passwd
  + /etc/shadwon(假如你不让用户改密码了)
  + /etc/group
  + /usr/bin/passwd
  + /sbin/portmap
  + /bin/login
  + /bin/ls
  + /bin/ps
  + /usr/bin/top