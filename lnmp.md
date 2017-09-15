---
title: 'LNMP,SAMBA'
date: '2016/11/16 10:37:59'
tags: 'ubuntu,lnmp,samba'
abbrlink: 65501
---
> 简要记录下了ubuntu下LNMP服务器的安装，samba文件共享的配置

<!--more-->

# 配置LNMP

---

# 安装Nginx
- 1.执行源更新：`sudo apt-get update`
- 2.获取Nginx：`sudo apt-get install nginx`
- 3.浏览器打开：`202.197.75.58`
- 出现如图即为安装成功！
- ![](http://i.imgur.com/v4Vb7b4.png)

---

# 配置Nginx
- 1.执行`sudo nano /etc/nginx/sites-available/default`
- 2.获取对php的支持更改如下：
- ![](http://i.imgur.com/lGrrDVu.png)

---

- ![](http://i.imgur.com/PvPYrbF.png)

---
<!--more-->

#安装MySQL
- 1.获取Mysql：`sudo apt-get install mysql-server`
- 2.安全配置：`sudo mysql_secure_installation`

---

# 安装php
- 1.获取php-fastproessmanage：`sudo apt-get insatll php7.0-fpm`
- 2.获取php对mysql的支持：`sudo apt-get install php7.0-sql`
- 3.获得php其他软件：`sudo apt-get install php-curl php-gd php-mbstring php-mcrypt php-xml php-xmlrpc`

---

- ![](http://i.imgur.com/5kpBLSQ.png)

---

# 配置php安全
- 1.执行`sudo nano /etc/php/7.0/fpm/php.ini`
- 2.修改`cgi.fix_pathinfo=0`避免安全漏洞

---

# MySQL配置
- 1.执行进入后台：`mysql -u root -p`
- ![](http://i.imgur.com/qzyAhqg.png)

---

- 2.创建数据库：`CREATE DATABASE wordpress;`
- ![](http://i.imgur.com/0yyOe41.png)

---

- 3.进入wordpress后台安装
- ![](http://i.imgur.com/EO5DzIy.png)
- 4.安装完成后即可登录网站后台写博客

---

# samba文件共享
- 1.安装samba：`sudo apt-get install samba`
- 2.配置samba：`sudo nano /etc/samba/smb.conf`
- ![](http://i.imgur.com/xHwolcN.png)
- ![](http://i.imgur.com/BCnueuW.png)

---

- 3.重启服务：`service smbd restart`
- `service nmbd restart`
- 4.添加用户，并键入密码：`smbpasswd -a lhw`
- ![](http://i.imgur.com/6glZMQa.png)

---

- 5.在win下可以访问：
- ![](http://i.imgur.com/gYAZwQQ.png)

---

- ![](http://i.imgur.com/Lqhuu7F.png)

---

- 6.新建一个netgroup用户组`groupadd netgroup`
- 7.添加用户`useradd a(b,c) -g netgroup`
- ![](http://i.imgur.com/rCMN1uN.png)
- 8.分别创建密码：`passwd a`
- ![](http://i.imgur.com/l830zTJ.png)

---

- 9.将smb文件夹归属改变：`sudo chown c:netgroup smb`
- ![](http://i.imgur.com/rdn2miL.png)
- 10.分别设置smbpasswd：`smbpasswd -a a`
- ![](http://i.imgur.com/eGIDa0h.png)

---

- 11.配置smb，添加字段：
- ![](http://i.imgur.com/tKfYGgO.png)

---

- 12.使用a登录，发现无法上传文件，删除文件。
- ![](http://i.imgur.com/fa1PWeD.png)

---

- 13.使用c登录则可以上传文件：
- ![](http://i.imgur.com/Mn4KEPd.png)

---

- ![](http://i.imgur.com/J4rh8oF.png)

---

# shell script
- 1.打印登录用户，工作目录：
- ![](http://i.imgur.com/ZSoIzKz.png)

---

- 2.计算从1+2+3+....+100，结果显示在屏幕上且重定向到result.log
- ![](http://i.imgur.com/Ew9ae0F.png)

---

- 3.程序的文件名,共有几个参数,若参数的个数小于3个，则输出“the parameter is less than 3“”并退出,显示第二个参数。
- ![](http://i.imgur.com/ChObg5t.png)

---