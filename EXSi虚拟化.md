---
title: VMware vSphere Hypervisor (ESXi)虚拟化使用笔记
tags: VMware
abbrlink: 59144
date: 2017-02-17 15:32:47
---

# VMware vSphere Hypervisor (ESXi)虚拟化使用

<!--more-->

----------

## 一、获取VMware vSphere Hypervisor (ESXi)
[官网下载地址](https://my.vmware.com/cn/web/vmware/downloads )下载ESXi以及管理工具*VMware vSphere*


----------

## 二、安装ESXi
注意：会清除数据并重新分区，注意资料备份

----------


## 三、配置网络
设置静态IP、DNS

----------

## 四、登录管理ESXi
可选**VMware Host Client**登录，或者**vSphere Client for Windows**

1. https://主机IP，即可进入VMware Host Client
2. 添加虚拟机，或者 部署OVF快速生成虚拟机
3. 添加系统光碟（Linux，Windows）
4. 启动安装程序

----------

## 五、添加用户并登录虚拟机
登录客户机需要在VMware Player，VMware workstation 里连接服务器，使用账户登录，添加权限不同的用户方便管理。

**对密码长度有严格的要求**

----------

## 六、获得官方的授权密钥

----------
# 存在问题
## ntf41client load faided
安装过程中提示No network adapters，无法继续安装。网卡驱动缺失造成的。
> [ "解决方案"](http://blog.bossma.cn/server/pc-install-esxi-5-5-two-problem-solution/)

1. 下载网卡驱动
2. 驱动打包工具ESXi-Customizer制作新的iso文件
## 调用对象 “ha-datastoresystem”的“HostDatastoreSystem.QueryVmfsDatastoreCreateOptions”。添加datastore出错
安装完成后没有数据储存，无法建立虚拟机，添加datastore提示**"HostDatastoreSystem.QueryVmfsDatastoreCreateOptions" for object “ha-datastoresystem” on ESXi “xxx.xxx.xxx.xx″ failed**
> [参考博客](http://blog.sina.com.cn/s/blog_666e9239010149ju.html)
> [参考2](http://www.ithao123.cn/content-10321943.html)
> [官方解答](https://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&externalId=1008886)

原因分析：

1. LUN空间大小超过2TB。
2. 这个LUN之前作为RDM裸设备映射。
3. LUN包含一个GPT分区，不能被清除。

未在实体机上解决。

----------
> 参考链接：[家用PC机打造VSphere5.1 测试环境](http://dngood.blog.51cto.com/446195/1123097)
> 