---
title: SSH密钥认证的坑
tags: ubuntu
abbrlink: 44822
date: 2017-01-10 22:43:38
---
> 对这种坑，无fuck说，在弄腾讯云的时候就会出现，没办法就直接用服务市场的镜像，就解决了
> 在jobsky的服务器(__Centos7__)上不想输密码，SSH配置的时候老出现问题
> __Server refused our key__

<!--more-->

# 解决过程
1. ssh 文件夹权限不对？
据网上说要求__700__甚至__400__的权限，改了，__无济于事__
2. 用puttykeygen生成的问题？
万恶的Mircosoft和Linux不相容，我又在服务端生成了一个新的密钥，__失败__
3. 终于想起我的腾讯爸爸，登上云服务器看看.ssh文件夹，只有一个文件__authorized_keys__。好像没什么毛病！
4. Selinux?失效！
4. 最后在一篇文章中找到["关于使用putty私钥连接linux出现失败的原因解决方案"](http://blog.csdn.net/magic_zj00/article/details/7470023)
竟然有和3相同的名字：__authorized_keys__
5. 最后key-comment 内容不重要
# Finally
```
mv id_rsa.pub authorzied_keys
```
![](http://www.intmain.me/images/20170110223815.png)
## 吐槽
辣鸡百度，尽搜出来水教程，弄了一个晚上
附：SSH的配置文件/etc/ssh/ssh_config

