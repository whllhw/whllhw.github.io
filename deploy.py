#!/usr/bin/env python
# coding=utf-8
import os
import time
from multiprocessing import Process
import hashlib


def deploy(data, title, tags):
    if not os.path.exists('_posts'):
        os.makedirs('_posts')
    #filename = data.split('title: ',1)[1].split('\n',1)[0].replace('-','').replace('/','').replace('\\','').replace(' ','')
    filename = title.replace('/', '').replace('\\', '').replace(' ', '') + '-'
    filename += hashlib.md5(data.encode('utf-8')
                            ).hexdigest()[:4].decode('utf-8')
    # data为 unicode类型
    with open('_posts/' + filename + '.md', 'wb') as f:
        f.write('''
---
title: {}
tags: {}
date: {}
---
'''.format(title.encode('utf-8'), tags.encode('utf-8'), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        f.writelines(data.encode('utf-8'))
    return filename


def post(filename):
    Process(target=main, args=(filename,)).start()


def main(filename):
    # 复制指定的文件名到 whllhw.github.io/source/_posts
    # 并提交，同步到 github 的 passage 分支
    # 使用 hexo 自动提交到master分支
    os.system(
        'cp _posts/{}.md ../whllhw.github.io/source/_posts -f'.format(filename.encode('utf-8')))
    os.chdir('../whllhw.github.io/source/_posts')
    os.system('git add .;git commit -m "Site update:{}";git push'.format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    os.chdir('../../')
    os.system('hexo g')
    os.system('hexo d')
#    os.chdir('public/')
#    os.system('git add .;git commit -m "Site update:{}";git push'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
