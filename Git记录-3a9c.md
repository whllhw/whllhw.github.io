---
title: Git记录
tags: 'git,linux'
abbrlink: 20125
date: 2017-11-25 20:02:36
---
# #Git 使用笔记
> 持续记录一下我抠脚的Git

克隆本分支，深度为1
```
    git clone -b deploy_online --depth=1 git@github.com:whllhw/whllhw.github.io 
    git push #提交代码直接push
```

当已经存在.git文件夹时可以使用

```
    git branch -r # 显示远程分支
    git branch -a # 显示所有分支
    git checkout -b dev origin/deploy_online # 建立本地分支dev并切换为远程的deploy_online？待验证
```
推送到远程其他分支时
```
    git remote add origin git@github.com:whllhw/whllhw.github.io #添加远程仓库
    git push --set-upstream origin master:passage #将本地的master分支提交到远程的passage
    # 以后每次提交都要使用 git push origin HEAD:passage 有点麻烦！
        # 或者使用上面切换分支的方法 git checkout -b ... 
    # 或者使用本地分支与远程分支相同(master 作为变量，为分支名)
    git push --set-upstream origin master #默认将本地master分支提交到远程的master

```