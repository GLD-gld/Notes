# 文稿
This is a practice

+ Docker Cloud

  + CaaS - Container-as-a-Service
  + 提供容器的管理，编排，部署的托管服务。
  + 主要模块：
    + 关联云服务商AWS，Azure
    + 添加节点作为Docker Host
    + 创建服务Service
    + 创建Stack
    + Image管理
  + 两种模式：
    + Standard模式。一个Node就是一个Docker Host
    + Swarm模式（beta）。多个Node组成的Swarm Cluster

+ Docker EE

  + UCP：universal control plane。app & cluster management（图形化操作界面swarm）

  + DTR：docker trusted registry。image  management（image管理）

  + 组建

    <img src="/Users/gld/Library/Application Support/typora-user-images/image-20210117182647296.png" alt="image-20210117182647296" style="zoom:50%;" />



<img src="/Users/gld/Library/Application Support/typora-user-images/image-20210117173508815.png" alt="image-20210117173508815" style="zoom:50%;" />