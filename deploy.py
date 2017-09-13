#!/usr/bin/env python
# coding=utf-8
import os
import time
def deploy(data):
    filename = data.split('title: ',1)[1].split('\n',1)[0]
    with open('_posts/'+filename+'.md','wb') as f:
        f.writelines(data.encode('utf-8'))
    main(filename)
    return filename
    
def main(filename):
    os.system('cp _posts/{}.md ../whllhw.github.io/source/_posts'.format(filename.encode('utf-8')))
    os.chdir('../whllhw.github.io')
    os.system('hexo g')
    os.chdir('public/')
    os.system('git add .;git commit -m "Site update:{}";git push'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

if __name__ == '__main__':
    deploy('''---
title: 中文
tags: 
date: 
---''')
