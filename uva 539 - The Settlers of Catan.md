---
title: uva 539 - The Settlers of Catan
tags: 
date: 2018-01-26 17:37:19
---

题目求最大的路径长度，应该是记录边的visited情况，而不是节点的visited情况。最长的路径出现环的时候会少算一条边！对于图的操作以后要注意对节点还是边进行操作，不然在DFS时会出现意外情况。