---
title: WordPress需要FTP连接问题
tags: WordPress
abbrlink: 16169
date: 2016-11-20 16:19:06
---

- 用于解决WordPress更新插件时要ftp的情况
- 网站文件的权限不对，WordPress无法写入文件（又是权限的锅）
- 只需要在wp-config配置文件中加入三行代码：
```
	define("FS_METHOD","direct");
	define("FS_CHMOD_DIR",0777);
	define("FS_CHMOD_FILE",0777);
```
便可解决权限问题。不需要FTP连接。

<!--more-->