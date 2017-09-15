---
title: wxPython的坑，textctrl回车事件处理
tags: python
abbrlink: 27751
date: 2017-03-30 15:14:42
---

> _学习Python的GUI界面绘制，对比PyQt，wxPython的区别，选择了wxPython的路径。_ 为一个小程序，实现网络聊天室的效果，简要写写其界面，毕竟只用终端界面容易出现冲突。

> 我参考的是这个
[快速入门教程](http://zetcode.com/wxpython/firststeps/)

# 到正题了————\>
实现功能为：按下回车，发送信息到服务器，并广播到各个客户端。

__BUG__：wxPython消息处理机制会先处理按下ENTER键的事件，而不是先执行回车。

<!--more-->
![](https://intmain.me/images/sp170330_152238.png)

```python
def OnEnter(self,e):
	self.out.WriteText('\n<localhost>' + \
		self.text.GetValue())
	self.text.Clear()
```
处理后会多出空格。就像这样：
![](https://intmain.me/images/sp170330_152834.png)
在网上查解决方法，找不到。小型库使用者少（还是我弱鸡）

突然看到还可以绑定事件 wx.EVT_TEXT 来检测输入的内容。于是再绑定一个清除回车的消息不就可以了。
![](https://intmain.me/images/sp170330_152523.png)
```python
self.Bind(wx.EVT_TEXT,self.replaceEnter,self.text)
def replaceEnter(self,e):
	if '\\n' in self.text.GetValue():
		self.text.Clear()
```

最后，完美解决~