### 16.1 什么是例行性工作

***

1.Linux工作调度的种类：at，cron

+ 两种工作调度的方式：
  + 一种是例行性的，就是每隔一定的周期要来办的事项；
  + 一种是突发性的，就是这次做完以后就没有的那一种



+ at
  + 仅执行一次就结束调度的命令
  + 要有atd这个服务的支持
+ crontab
  + 所设置的工作将会循环一直进行下去。
  + 分钟，小时，每周，每月或每年等
  + 可编辑/etc/crontab来支持
  + 需要crond服务支持



2.Linux上常见的例行性工作

+ 进行日志文件的轮替（log rotate）
  + 日志文件回越来越大，造成读写性能的困扰，让旧的数据与新的数据分别存放，系统必要的例行任务
+ 日志文件分析logwatch的任务
  + logwatch分析日志信息
+ 新建locate的数据库
  + 系统会主动进行updatedb，文件名数据库放置到/var/lib/mlocate
+ whatis数据库的建立
  + 与locate数据库类似的，whatis也是个数据库
+ RPM软件日志文件的新建
  + 是一种软件管理的机制。
+ 删除临时文件
  + 通过例行性工作调度执行名为tmpwatch的命令来删除这些临时文件
+ 与网络服务有关的分析行为



### 16.2 仅执行一次的工作调度

***

1.atd的启动与at运行的方式

+ 启用atd服务
  + `systemctl start atd`
+ 开机启动
  + `systemctl enable atds`
+ at的运行方式
  + 使用at这个命令来生成所要运行的工作，并将这个工作以文本文件的方式写入/var/spool/at/目录内
  + 利用/etc/at.allow与/etc/at.deny这两个文件来进行at的使用限制
    + 先寻找/etc/at.allow这个文件，写在这个文件中的用户才能使用at，没有在这个文件中的用户则不能使用at（即使没有写在at.deny当中）
    + 如果/etc/at.allow不存在，就寻找/etc/at.deny这个文件，若写在这个at.deny的用户则不能使用at，而没有在这个at.deny文件中的用户就可以使用at了
  + /etc/at.allow是管理较为严格的方式，而/etc/at.dent则较为松散



2.实际运行单一动作调度

+ at [-mldv] TIME
+ at -c 工作号码
  + -m：当at的工作完成后，即使没有输出信息，以email通知用户该工作以完成。
  + -l：at -l 相当于atq，列出目前系统上面的所有该用户的at调度；
  + -d：at -d 相当于atrm，可以取消一个在at调度中的工作；
  + -v：可以使用较明显的时间格式列出at调度中的任务列表；
  + -c：可以列出后面接的该项工作的实际命令内容。
  + TIME：时间格式
  + HH:MM
  + HH:MM YYYY-MM-DD
  + HH:MM[am|pm] [Month] [Date]
  + HH:MM[am|pm] + number [minutes|hours|days|weeks]
+ 例：at now + 5 minutes ¥ at /bin/mail root -s "testing at job" < /root/.bashrc <EOT>(ctrl+d 结束)
+ atq
  + 查询主机上面有多少的at工作调度
+ atrm 5
  + 删除工作调度
+ batch
  + 系统有空时才进行后台任务
  + batch 23:00 2009-3-17 ¥ sync ¥ sync ¥shutdown -h now <EOT> (ctrl+d)结束



### 16.3 循环执行的例行性工作调度

***

1.用户的设置

+ /etc/cron.allow
  + 将可以使用crontab的账号写入其中，若不在这个文件内的用户则不可使用crontab。
+ /etc/cron.deny
  + 将不可以使用crontab的账号写入其中，若未记录到这个文件当中的用户，就可以使用crontab。
+ crontab [-u username] [-l] [-e] [-r]
  + -u：只有root才能进行这个任务，也即帮其他用户新建/删除 crontab工作调度；
  + -e：编辑crontab的工作内容；
  + -l：查阅crontab的工作内容；
  + -r：删除所有的crontab的工作内容，若仅要删除一项，请用-e去编辑。



2.系统的配置文件：/etc/crontab

+ cat /etc/crontab
  + MAILTO=root：信息接收者。root并无法在客户端中以POP3之类的软件收信
  + PATH=...：执行文件的查找路径



3.一些注意事项

+ 资源分配不均的问题
+ 取消不要的输出选项
+ 安全的检验
+ 周与日、月不可同时并存



### 16.4 可唤醒停机期间的工作任务

***

1.什么是anacron

+ 并不能指定何时执行某项任务，而是以天为单位或者是在开机后立刻进行anacron的操作
+ 检测停机期间应该进行但是并没有进行的crontab任务，并将该任务执行一遍，然后就自动停止。
+ anacron其实也是通过crontab来运行的
+ anacron运行的时间通常有两个，一个是系统开机期间运行，一个是写入crontab的调度中。



2.anacron与/etc/anacrontab

+ anacron其实是一个程序并非一个服务
+ anacron [-sfn] [job] ..
+ anacron -u [job]..
  + -s：开始连续执行各项工作（job），会依据时间记录文件的数据判断是否运行
  + -f：强制执行，而不去判断时间记录文件的时间戳；
  + -n：立刻进行未进行的任务，而不延迟（delay）等待时间；
  + -u：仅更新时间记录文件的时间戳，不进行任何工作。
  + job：由/etc/anacrontab定义的各项工作名称。



