---
title: Ubuntu下的网络配置
date: '2016/11/16 10:37:59'
tags: Ubuntu
abbrlink: 54469
---
记录下了Ubuntu下网络初始化

<!--more-->

# 1.配置网络
## 命令版：
### 1.设置IP
    sudo ifconfig ens3 202.197.75.58 
### 2.设置网关
    sudo route add default gw 202.197.75.55
### 3.设置DNS
    sudo nano /etc/resolv.conf 
添加`nameserver 114.114.114.114`
### 4.重启网络
    sudo /ect/init.d/networking restart
或者`sudo ifconfig ens3 down`
+`sudo ifconfig ens3 up`
### 5.测试网络
    ping 114.114.114.114
***
> 好吧，这是我查以前的博客来的，现在谁还用这些命令，直接改配置文件啊！！！
## 配置版：
<!--more-->
### 1.打开配置文件

`sudo nano /etc/network/interfaces`

使用下面的配置：

``` shell
auto ens3 ;自动挂载网卡
iface ens3 inet static ;静态IP地址
address 202.197.75.58 ;要设置的IP
gateway 202.197.75.55 ;网关
netmask 255.255.255.0 ;子网掩码
dns-nameservers 114.114.114.114

```
### 2.重启网卡
    sudo /etc/init.d/networking restart
***
#安装ssh
    sudo apt-get update
    sudo apt-get install openssh-server
    sshd
##设置开机自动启动ssh
    sudo nano /etc/rc.local 
    文件中添加：sshd
   
