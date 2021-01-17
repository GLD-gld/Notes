### swarm_wordpress

+++

1.Swarm

```shell
#创建overlay网络
docker network create -d overlay demo

#mysql
docker service create --name mysql --env MYSQL_ROOT_PASSWORD=root --env MYSQL_DATABASE=wordpress --network demo --mount type=volume,source=mysql-data,destination=/var/lib/mysql mysql

#wordpress
docker service create --name wordpress -p 80:80 --env WORDPRESS_DB_PASSWORD=root --env WORDPRESS_DB_HOST=mysql --network demo wordpress
```



2.Stack

```shell
#创建stack
docker stack deploy wordpress --compose-file=docker-compose.yml

#列出stack
docker stack ls

#查看具体的stack
docker stack ps wordpress

#查看stack里的services
docker stack serices wordpress
```



```yaml
#docker-compose.yml

version: '3'

services:

  web:
    image: wordpress
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_PASSWORD: root
    networks:
      - my-network
    depends_on:
      - mysql
    deploy:
      mode: replicated
      replicas: 3
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      update_config:
        parallelism: 1
        delay: 10s

  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - my-network
    deploy:
      mode: global
      placement:
        constraints:
          - node.role == manager

volumes:
  mysql-data:

networks:
  my-network:
    driver: overlay
```



3.Secret Management

+ 存在Swarm Manager节点Raft database里
+ Secret可以assign给一个service，这个service就能看到这个secret
+ 在container内部Secret看起来像文件，但是实际是在内存中

```
#在Swarm Manager节点中创建secret
docker secret creat ${secret_name} ${filename}
echo "admin123" | docker secret create ${secret_name} -

#查看secret
docker secret ls

#删除secret
docker secret rm ${secret_name}

#将secret传入Mysql中
echo "admin123" | docker secret create my-pw -
docker service create --name db --secret my-pw -e MYSQL_ROOT_PASSWORD_FILE=/var/run/secrets/my-pw mysql
```



4.Stack Secret

```yaml
version: '3'

services:

  web:
    image: wordpress
    ports:
      - 8080:80
    secrets:
      - my-pw
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_PASSWORD_FILE: /run/secrets/my-pw
    networks:
      - my-network
    depends_on:
      - mysql
    deploy:
      mode: replicated
      replicas: 3
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      update_config:
        parallelism: 1
        delay: 10s

  mysql:
    image: mysql
    secrets:
      - my-pw
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/my-pw
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - my-network
    deploy:
      mode: global
      placement:
        constraints:
          - node.role == manager

volumes:
  mysql-data:

networks:
  my-network:
    driver: overlay

#不推荐，因为需要创建一个password文件
# secrets:
#   my-pw:
#    file: ./password
```



5. Update Service

```shell
#版本更新
docker service update --image ${image} web

#端口更新
docker service update --publish-rm 8080:5000 --publish-add 8088:5000 web

sh -c "while true; do curl 127.0.0.1:8088&&sleep 1; done"

```



```yaml
version: '3'

services:

  web:
    image: wordpress
    ports:
      - 8080:80
    secrets:
      - my-pw
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_PASSWORD_FILE: /run/secrets/my-pw
    networks:
      - my-network
    depends_on:
      - mysql
    deploy:
      mode: replicated
      replicas: 3
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      update_config:
        parallelism: 1
        delay: 10s

  mysql:
    image: mysql
    secrets:
      - my-pw
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/my-pw
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - my-network
    deploy:
      mode: global
      placement:
        constraints:
          - node.role == manager

volumes:
  mysql-data:

networks:
  my-network:
    driver: overlay
```

