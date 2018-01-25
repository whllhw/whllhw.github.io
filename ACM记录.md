---
title: ACM记录
tags: cocos
date: 2018-01-24 15:26:19
---

汉诺塔问题：
```
void f(int n,int from, int to, int on) {
	if (n == 1) {
		ans  ;
		return;
	}
	f(n - 1, from, to, on);// 1 -> 2
	f(n - 1, to, on, from);// 2 -> 3
	//移动n -> 2
	ans  ;
	f(n - 1, on, from, to);//3 - > 1
	//移动n -> 3
	ans  ;
	f(n - 1, from, on, to);//1 -> 3
}
```