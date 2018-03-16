from database import *
import os
from sys import platform
from models import *
from datetime import datetime
import subprocess,hashlib
import logging

def getPath():
    """

    :return: 返回存放文件的目录
    """
    filePath = 'E:/博客/whllhw.github.io/'
    return filePath


def getDelpoyPath():
    return 'E:/博客/blog'


def getFileName():
    """
    得到文件储存路径，文件名
    :return: filePath -> str,fileNames -> list
    """
    filePath = getPath()
    fileNames = [file for file in os.listdir(
        filePath) if not os.path.isdir(file) and file[-3:] == '.md']
    return filePath, fileNames


def importPassageTool():
    """
    导入磁盘文章到数据库
    :return:
    """
    """
    u = User('username','passwd')
    db_session.add(u)
    db_session.commit()
    User.query.filter(User.name == 'lhw').first()
    """
    filePath, fileNames = getFileName()
    for file in fileNames:
        with open(filePath + file, encoding='utf-8') as f:
            passage_md5 = hashlib.md5(open(filePath + file,'rb').read()).hexdigest()
            f.seek(0)  # 返回到文件头部
            _ = f.readline()
            info = {}
            for i in f:
                if '---' in i:
                    break
                i = i.split(':', 1)
                info[i[0]] = i[1].strip().replace('\n', '')
            try:
                info['tags'] = info['tags'].lower().replace('\'', '')
            except:
                print('----', info)
                exit()
            content = ''.join((i for i in f))
            for t in info['tags'].split(','):  # 处理标签，对不在数据库中的进行创建
                if not Category.query.filter(Category.name == t.strip()).first():
                    db_session.add(Category(t.strip()))
                    db_session.commit()
            # 提交文章
            if not Passage.query.filter(Passage.title == info['title']).first():
                try:
                    date = datetime.strptime(
                        info['date'].strip(), '%Y-%m-%d %H:%M:%S')
                except:
                    info['date'] = info['date'].replace('\'', '')
                    date = datetime.strptime(
                        info['date'].strip(), '%Y/%m/%d %H:%M:%S')

                db_session.add(
                    Passage(title=info['title'], context=content, date=date, author=1))
                db_session.commit()

            passage_id = Passage.query.filter(
                Passage.title == info['title']).first().id
            db_session.add(File(passage_id, passage_md5, file))
            db_session.commit()

            for t in info['tags'].split(','):
                category_id = Category.query.filter(
                    Category.name == t.strip()).first().id
                db_session.add(Tag(passage_id, category_id))
                db_session.commit()


def outPassageTool(passage):
    """
    从数据中写出单个文章到文件上
    :param passage_id:
    :return:
    """
    categories = Category.query.join(Tag).join(Passage).filter(Passage.id == passage.id).all()  # join连接查询出所有的tag
    fileName = passage.title.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?',
                                                                                                          '').replace(
        '<', '').replace('>', '').replace('|', '') + '.md'
    file = db_session.query(File).filter(File.passage_id == passage.id).first()
    # 不判断是否已经修改！
    # Python md5 校验打开方式有毒！！
    # md5.update() 为大数据读入时使用
    if file and os.path.exists(getPath()+file.fileName):
        if file.md5 != hashlib.md5(open(getPath()+file.fileName,'rb').read()).hexdigest(): # 文件md5不相同，已经被修改
            logging.warning(file.fileName + "已经被修改")
        else:
            os.remove(getPath() + file.fileName)

    # 无论是否被修改将会直接清空文件
    with open(getPath() + fileName, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: {passage.title}\n')
        f.write('tags: ')
        tag = (i.name for i in categories)
        f.write(', '.join(tag))
        date = passage.date.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'\ndate: {date}\n')
        f.write('---\n\n')
        f.write(passage.context)

    with open(getPath() + fileName, 'rb') as f:
        hexdigest = hashlib.md5(f.read()).hexdigest()
        if not file:
            db_session.add(File(passage.id, hexdigest, fileName))  # 提交文件属性到数据库
            db_session.commit()
        else:
            file.fileName = fileName
            file.md5 = hexdigest
            db_session.commit()


def syncPassage():
    """
    同步数据库与文件
    :return
    """
    # TODO:同步数据库与文件
    """
        直接全部把数据库中的文章输出
    """
    if platform == 'win32':
        os.system('del '+getPath().replace('/','\\') + '\\*.md')
    else:
        os.system('rm '+getPath() + '/*.md')
    for passage in Passage.query.all():
        outPassageTool(passage)


def deployPassage():
    """
    发布文章：
    :return:
    """
    # 删除 _post 下所有md文件
    # 移动文件到 _post
    if platform == 'win32':
        os.system('del ' + getDelpoyPath().replace('/', '\\') + '\\source\\_posts\\*.md')
        os.system('copy ' + getPath().replace('/', '\\') + '*.md ' + getDelpoyPath().replace('/',
                                                                                             '\\') + '\\source\\_posts\\')
    else:
        os.system('rm ' + getDelpoyPath() + '/source/_post/*.md')
        os.system(f'cp f{getPath()}/*.md {getDelpoyPath()}/source/_posts/')
    # 执行 hexo g & hexo d
    p = os.system(f'cd {getDelpoyPath()} & hexo g & hexo d')
    # retVal = p.wait()
    # 文章同步提交到git
    # q = subprocess.Popen(f'cd {getPath()} & git add . & git commit -m "bak up" & git push', shell=True,
    #                      stdout=subprocess.PIPE,
    #                      stderr=subprocess.STDOUT)
    # for line in q.stdout.readline():
    #     print(line)
    # retVal2 = q.wait()
    return 0

if __name__ == '__main__':
    # outPassageTool(Passage.query.filter(Passage.id == 30).first())
    syncPassage()
