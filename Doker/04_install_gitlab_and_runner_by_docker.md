### install gitlab and gitlab-runner

+++

1.docker-compose.yml

```yaml
version: '3'
volumes:
  gitlab-config-volume:
  gitlab-log-volume:
  gitlab-data-volume:
  gitlab-runner-config:
services:
  gitlab-web:
    image: gitlab/gitlab-ce:latest
    container_name: gitlab-web
    hostname: gitlab-web
    volumes:
      - gitlab-config-volume:/etc/gitlab
      - gitlab-log-volume:/var/log/gitlab
      - gitlab-data-volume:/var/opt/gitlab
      - /etc/localtime:/etc/localtime:ro
    ports:
      - '2222:22'
      - '8000:80'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        gitlab_rails['gitlab_shell_ssh_port'] = 2222
        external_url 'http://192.168.1.10/gitlab'
    networks:
      - gitlab-network

  gitlab-runner1:
    image: gitlab/gitlab-runner:latest
    container_name: gitlab-runner1
    hostname: gitlab-runner1
    volumes:
      - gitlab-runner-config:/etc/gitlab-runner
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - gitlab-network

networks:
  gitlab-network:
    name: gitlab-network
```



2.register-runner.sh

```shell
#!/bin/bash

URL="http://192.168.1.10:8000/gitlab"
PROJECT_REGISTRATION_TOKEN="As5zR11CqNxG7ehmy-Zo"

docker-compose exec gitlab-runner1 gitlab-runner register \
--non-interactive \
--executor "docker" \
--docker-privileged=true \
--docker-image alpine:latest \
--url ${URL} \
--registration-token ${PROJECT_REGISTRATION_TOKEN} \
--description "demo-project-runner" \
--tag-list "demo-project-runner" \
--run-untagged="false" \
--locked="false" \
--access-level="not_protected" \
--docker-volumes "/reports"
```



3.注册runner

```shell
chmod +x register-runner.sh
./register-runner.sh
```



4.重启gitlab-runner

```shell
docker-compose restart gitlab-runner
```



5.配置文件/var/lib/docker/volumes/docker-compose_gitlab-runner-config/_data/config.toml

```shell
concurrent = 1
check_interval = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "demo-project-runner"
  url = "http://192.168.1.10:8000/gitlab"
  token = "zUstwqjCEozvMm8HZSqG"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/reports", "/cache"]
    shm_size = 0
```



