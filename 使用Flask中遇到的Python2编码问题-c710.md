---
title: 使用Flask 中遇到的Python2 编码问题
tags: 'flask,python'
abbrlink: 22006
date: 2017-09-17 16:47:49
---
# 使用Flask 中遇到的Python2 编码问题

>  python2 的编码问题一直被开发者诟病，进行一些字符工作是确实会有点麻烦，而且新手不熟悉编码，更会踩坑里。

开始前建议阅读 [Python2.x 字符编码终极指南](http://selfboot.cn/2016/12/28/py_encode_decode/)，或者搜索一下就有很多文章。

Python2 中的 str 类型可以看做是 byte 类型的数组，即是字节流。早期设计中并没有这么多的编码，后来版本提供一个 unicode类型来修复了这一类型。有如下关系

```python
unicode.encode('utf-8') = str
str.decode('utf-8') = unicode
```

Flask 中提交的表单 + MySQLdb + Mysql

1. 源文件中指明编码 #coding=utf-8
2. Mysql设置编码为utf8 
3. MySQLdb 连接指定charset='utf8'，插入的代码如下

```python
g.db.execute('insert into entries (title, text) values ({}, {})'.format(request.form['title'].encode('utf-8'), request.form['text'].encode('utf-8')))
```

​	request.form['title'] 的类型是Unicode，encode后应该就可以变成str了，可是

提示``OperationalError: (1054, "Unknown column 'abc' in 'field list'")``英文都插入不了，然后经Stack Overflow启发，改动 { } => "{ }"，然后就可以运行了。。坑死了。

还有一个坑：``OperationalError: (2002, "Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)")``

默认MySQLdb会在/var/lib/mysql 寻找sock，由于服务器的安装位置不是这里，查找mysql.sock发现在/tmp 目录下，创建MySQLdb连接时，指定unix_sock = /tmp/mysql.sock就可以连接了
