
---
title: Selenium 自动化测试框架
tags: Selenium,python
date: 2017-09-21 12:29:15
---

> 比较快速的爬取一些网站，最快就是用这个框架，记录遇到的坑。

查阅的[中文文档](https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html "中文文档")基本用法简单，但是高级的用法就是英文的，或者没有。这里记录一下。

---

<!--more-->

---

``webdriver.Chrome('/path/to/chromedriver')``
- 加载驱动时要指定路径，不然提示没有找到驱动
- 在弹出的网页进行查找元素时，要使用切换窗口，不然提示NoSuchElementException

``driver.switch_to_window(driver.window_handles[-1])``

- driver.page_source返回的是当前渲染后的网页的源码，可以进行保存
- 获取元素的内容 ```element.text```返回str类型，包含当前元素下所有的内容
- 最后一个是json模块的锅：输出json到文件时居然还是\u开头的unicode，python3 还有编码问题？后面终于找到还要附加参数，心态爆炸

``f.write(json.dumps(data,indent=4,ensure_ascii=False))``

- 隐式等待，可以自制一个装饰器，重复调用

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def wait(func):
	def wrapper(*args,**kw):
		return WebDriverWait(driver, 30).until(func(*args,**kw))
	return wrapper
@wait
def find_element_by_xpath(xpath):
	return  EC.presence_of_element_located((By.XPATH, xpath))
@wait
def find_elements_by_xpath(xpath):
	return EC.presence_of_elements_located((By.XPATH, xpath))
```
