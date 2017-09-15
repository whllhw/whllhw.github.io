---
title: 腾讯云主机相关的iptables使用端口转发
tag: 'linux,iptables'
abbrlink: 13040
date: 2017-06-23 11:27:00
---

# 腾讯云主机相关的iptables使用端口转发
> 阿里云、腾讯云的主机都是只有内网IP网卡，用户不能使用公网IP网卡，因此直接在iptables上进行开放端口是不行的。

<!--more-->

在使用ngrok进行内穿透时，笔者发现无法连接到指定端口，于是去iptables放通该端口，使用```nc -v -w 10 -z intmain.me 6060``` 出现超时错误， ```time out :Operation now in progress``` 但我用其来试探80端口时显示连接成功。



1. **腾讯安全组，放通该端口** 。（默认安全组放通全部端口不安全，这个坑一直没发现，郁闷了好久）



```shell
	$ iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 6060 -j ACCEPT
	$ service iptables save
	$service iptables restart
```

这样就放通了6060端口，在外部可以进行访问了。
端口转发可以实现
- 一台机到另一台机端口
- 转发本机端口的转发（相当于端口引用）

``` shell
	# 首先启用端口转发
	$ echo 1 > /proc/sys/net/ipv4/ip_forward
	# 或者修改 /etc/sysctl.conf ,使net.ipv4.ip_forward = 1 ,sysctl -p
```


参考链接： 
<a href="http://blog.csdn.net/zzhongcy/article/details/42738285" target="_blank" rel="external">linux下用iptables转发本地端口</a>