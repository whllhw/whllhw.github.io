#!/usr/bin/env python
# coding=utf-8
import os
import time
from multiprocessing import Process
import hashlib
def deploy(data,title,tags):
    if not os.path.exists('_posts'):
        os.makedirs('_posts')
    #filename = data.split('title: ',1)[1].split('\n',1)[0].replace('-','').replace('/','').replace('\\','').replace(' ','')
    filename = title.replace('/','').replace('\\','').replace(' ','')+hashlib.md5(data).hexdigest()[:4]
    with open('_posts/'+filename+'.md','wb') as f:
        f.write('''
        ---
        title: {}
        tags: {}
        date: {}
        ---
        <!--more-->
        '''.format(title,tags,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).encode('utf-8'))
        f.writelines(data.encode('utf-8'))
    return filename
def post(filename):
    Process(target=main,args=(filename,)).start()
def main(filename):
    os.system('cp _posts/{}.md ../whllhw.github.io/source/_posts'.format(filename.encode('utf-8')))
    os.chdir('../whllhw.github.io')
    os.system('hexo g')
    os.chdir('public/')
    os.system('git add .;git commit -m "Site update:{}";git push'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    os.chair('cd ../source/_posts')
    os.system('git add .;git commit -m "Site update:{}";git push'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))    

if __name__ == '__main__':
    deploy('''---
title: 中文
tags: 
date: 
---''')
