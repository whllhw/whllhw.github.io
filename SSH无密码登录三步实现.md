---
title: SSH无密码登录三步实现
tags: 'ubuntu,ssh'
abbrlink: 20103
date: 2017-03-11 23:37:45
---
> _SSH免密码登录百度上有很多教程，大多是重复的，效果不一定好，Linux字符终端调试起来不一定好受，原来的Ubuntu上没有试过登录，后面就弄不好了。_
借助必应的威力，有了新的发现，借助__ssh-copy-id__，三步实现！！

## 第一步：
生成密钥：
```shell
ssh-kengen 
```
保存在_~/.ssh/_目录下。
## 第二步：
```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub username@remote-host
```
该命令将公钥文件写到远程机器的 *~/.ssh/authorized_key*

## 第三步：
```shell
ssh username@remote-host
```
登录！！

> 原文：

[使用ssh-keygen和ssh-copy-id三步实现SSH无密码登录](http://blog.chinaunix.netdd/uid-26284395-id-2949145.html)


<!--more-->
