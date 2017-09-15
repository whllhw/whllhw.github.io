---
title: shell script
date: '2016/11/16 10:37:59'
tags: shell
abbrlink: 33145
---
> 简要记录下了三个sh脚本学习

<!--more-->

---
## 自动按时间建立脚本文件
```
#!/bin/bash //指定解释器
if [[ -z "$1" ]];then //如果参数1非空则
   newfile=~/newscript_`date +%m%d_%S`
//newfile=~/newscript_日期+月日秒 这里先执行“`date +%m%d_%S`”结果作为外部的输入信息
else
   newfile=$1 //文件名为参数
fi //if结束
if  ! grep "^#!" $newfile &>/dev/null; then
//如果非  newfile里一开始有#（屏幕不显示出来（送入黑洞））
cat >> $newfile << EOF//将标准输入（追加）给newfile，EOF为退出编辑状态
```
---
<!--more-->
```
#!/bin/bash//指定解释器

# Author: Inert Your Name here.

#Date & Time: `date +"%F %T"`

#Description: Please Edit here.

EOF//结束输入

fi//如果结束

vim +5 $newfile//向下移动5行，以便输入
```
---
## 指定用户是否在系统中注册
```
#!/bin/bash //指定解释器

read –p "please input a username:"  USER//使用提示符输入并保存在USER里

if cut –d：-f1  /etc/passwd | grep "^$USER$" &> /dev/null ;then//如果 取出/ect/passwd(:为分割字符) 有USER的内容 （不显示出来） 

MYBASH=`grep  "^$USER:"  /etc/passwd | cut –d :  -f7`//找出文件里第7个字段

echo "${USER}'s shell is $MYBASH"//显示USER的shell路径

else

  echo "$USER not exists."//USER不存在

  exit  4//退出

fi
```