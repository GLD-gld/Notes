### docker0 bridge

+++

1.两个容器之间通过docker0 这个bridge通信

```shell
yum install bridge-utils
brctl show
```



2.创建容器时，将会创建一对接口（veth-pair），一个接口在容器内部，一个接口在docker0 这个bridge内部

<img src="/Users/gld/Library/Application Support/typora-user-images/image-20210116101823704.png" alt="image-20210116101823704" style="zoom:50%;" />



3.容器访问Internet

<img src="/Users/gld/Library/Application Support/typora-user-images/image-20210116102643742.png" alt="image-20210116102643742" style="zoom:50%;" />