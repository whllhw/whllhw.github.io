使用 Flask Web 框架生成 Markdown 文件后使用 Hexo 渲染，Git推送到服务器

Git 使用笔记

克隆本分支，深度为1
```
    git clone -b deploy_online git@github.com:whllhw/whllhw.github.io -depth=1
    git push #提交代码直接push
```
或者使用

```
    git branch -r # 显示远程分支
    git branch -a # 显示所有分支
    git checkout -b dev origin/deploy_online # 建立本地分支dev并切换为远程的deploy_online？待验证
```