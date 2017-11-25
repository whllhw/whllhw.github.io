---
title: 我的云上CentOS记录
tags: 'centos,linux'
abbrlink: 8687
date: 2017-11-25 19:55:27
---
# #使用CentOS笔记
> 在云上使用Centos，很多常用的命令不能直接用。软件仓库轻量化，也有导致使用不便。安装nginx 要添加源，才能直接安装，不然就是自己编译源代码。
将持续更新。。。

# ##使用常用命令

Centos 安装编译工具包，很多在其他系统上直接安装的程序，都被包含进去，保证软件包仓库的纯净。

```shell
yum groupinstall "Development Tools"
```
nginx 配置重载
``nginx -s reload``
nginx 配置测试
``nginx -t``

查看本地端口使用情况

``netstat -ntlp``

结束进程

``pkill {pidname} ``