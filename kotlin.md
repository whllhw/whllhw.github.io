---
title: kotlin
tags: 
date: 2018-02-07 12:59:37
---

# #语法特性
- 分号可省略

- 变量推导
```kotlin
	fun sum(a: Int, b: Int) = a   b
```

- 变量定义

```
	val a = 2  //局部常量。自动推导出Int 类型，不可再次修改
	var b = 2 //顶层变量。可以修改
```

- 字符串模板
```
	var a = 1
	val s1 = "a is $a"
	a = 2
	val s2 = "${s1.replace("is","was")},but now is $a"
```

- if 作为表达式

```
fun maxOf(a: Int, b:Int) = if (a>b) a else b
```

- 函数返回值可为 null

```
	fun parseInt(str: String): Int?{
		return str.toIntOrNull()
	}
```

- 分支中自动类型转化

```
	fun getStringLength(obj: Any):Int? {
		if(obj is String){ // 在此分支中自动转化为了String类型，不需要再手动进行显式转化
			return obj.length
		}
		// 出了分支则为 Any 类型
		return null
	}
```

- for 循环

```
	val items = listOf("apple","banana","kiwi")
	for (item in items){
		println(item)
	}
	for(index in items.indices){
		println("${items[index]}")
	}
```

- when 表达式

```
	fun describe(obj: Any): String =
	when (obj) { // 与switch case 相似
		1          -> "One"
		"Hello"    -> "Greeting"
		is Long    -> "Long"
		!is String -> "Not a string"
		else       -> "Unknown"
	}
```

- 区间( range )

```
	val x = 10
	val y = 9
	if (x in 1..y 1) {  // 使用 in 进行判断区间
		println("fits in range")
	}
	for( x in 1..5){  // 区间迭代
		print(x)
	}
	for ( x in 1..10 step 2){ // 指定步进
		print(x)
	}
```

- 集合

```
	in 运算符进行迭代
	for (item in items) {
		println(item)
	}
	判断包含的实例
	when {
		"orange" in items -> println("juicy")
		"apple" in items -> println("apple is fine too")
	}
```

- lambda表达式


- 创建类及实例

```
	var obj = Obj(1,2,3) // 不需要 new 关键字
```