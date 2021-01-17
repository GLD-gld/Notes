### Network Namespace

+++

1.查看linux的network namespace

```
ip netns list
```



2.删除network namespace

```shell
ip netns delete ${var}
```



3.创建network namespace

```shell
ip netns add ${var}
```



4.在network namespace中执行命令

```shell
ip netns exec ${var} ip a
ip netns exec ${var} ip link

#lo端口up起来
ip netns exec ${var} ip link set dev lo up

#单个端口无法up起来，必须是一对
```



+ test

```shell
#添加两个namespcace
ip netns add test1
ip netns add test2

#添加veth-pair（一对虚拟接口）
ip link add veth-test1 type veth peer name veth-test2

#将test1接口添加到namespace test1中
ip link set veth-test1 netns test1

#将test2接口添加到namespace test2中
ip link set veth-test2 netns test2

#给两个端口分配ip
ip netns exec test1 ip addr add 192.168.1.1/24 dev veth-test1
ip netns exec test2 ip addr add 192.168.1.2/24 dev veth-test2

#将两个端口up起来
ip netns exec test1 ip link set dev veth-test1 up
ip netns exec test2 ip link set dev veth-test2 up

#可ping(ICMP),IP可达性。telnet，服务可用性
ip netns exec test1 ping 192.168.1.2
ip netns exec test2 ping 192.168.1.1
```

