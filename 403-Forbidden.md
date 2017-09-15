---
title: Nginx上php部署 403-Forbidden 问题
tags: 'nginx, php'
abbrlink: 15782
date: 2017-06-01 13:37:00
---

php7.0-fpm + Nginx搭建php服务，遇到403 也是常见的情形。网络上有说进程数不够、缓存不够会出现403 ，可我这破网站也就我一人在上，显然不是这情况。先记录下如何安装。
	
	sudo apt-get install php nginx # 默认php7自带了fpm
修改Nginx默认站点的配置

<!--more-->

	
	sudo /etc/nginx/sites-enabled/default
	
修改location ~ \.php$ 下的内容：
去掉注释 #

	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		# With php7.0-cgi alone:
		#fastcgi_pass 127.0.0.1:9000;
		# With php7.0-fpm:
		fastcgi_pass unix:/run/php/php7.0-fpm.sock;
	}

fpm比cgi模式下快，注意不能同时启用两个，会报错。（智障了半天没有找出来）

重启一下服务：
	
	/etc/init.d/nginx reload

---

然后会出现访问网站 403 Forbidden 错误！！！
网上找了一下说是权限的锅，Nginx 与 php-fpm 运行的用户没有权限读取目录下文件所致。

	sudo chown www-data:www-data . -R
	sudo chmod 770 . -R

www-data 是运行Nginx的默认用户，php7.0-fpm写入系统服务，运行用户是root。不能简单的设置为 777 ，违反权限最小原则，安全性丢失。