#项目骨架
pip3.6 install virtualenv
whereis virtualenv

1.mkdir ~/.venvs
#执行virtualenv，让它包含系统站点包，然后让它在~/.venvs/lpthw中创建一个虚拟环境
2.virtualenv --system-site-packages ~/.venvs/lpthw
#激活lpthw虚拟环境
3.source ~/.venvs/lpthw/bin/activate

#创建骨架项目目录
mkdir projects                  #用来存储自己的各个项目
cd projects
mkdir skeleton                  #项目名
cd skeleton
mkdir bin NAME tests docs       #NAME为项目主模块名，bin用来存放在命令行上运行的脚本，但不存放模块
touch NAME/__init__.py
touch tests/__init__.py
touch setup.py                  #安装项目时用到
touch tests/NAME_tests.py       #测试专用的骨架文件

#应用程序的测试
nosetests                       #测试配置