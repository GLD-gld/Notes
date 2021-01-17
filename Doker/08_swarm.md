### swarm

+++

1.architecture

<img src="/Users/gld/Library/Application Support/typora-user-images/image-20210117191531943.png" alt="image-20210117191531943" style="zoom:50%;" />



2.cluster

```shell
#manager
docker swarm init --advertise-addr=192.168.1.10

#worker1
docker swarm join --token SWMTKN-1-1zsekatfzlz7ucp08ttrkf4n95f065qnq288bqtdt8uaij1xpm-3qj8i3x9azjmll2plidb3goap 192.168.1.10:2377

#worker2
docker swarm join --token SWMTKN-1-1zsekatfzlz7ucp08ttrkf4n95f065qnq288bqtdt8uaij1xpm-3qj8i3x9azjmll2plidb3goap 192.168.1.10:2377

#在manager上查看node
docker node ls 
```



3.create a service

```shell
docker service create --name demo busybox sh -c "while true; do sleep 3600; done"

docker service ls

docker service ps demo

docker service scale demo=5

docker service rm demo
```