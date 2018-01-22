from database import *
import os
from models import *
from datetime import datetime


def getPath():
    """

    :return: 返回存放文件的目录
    """
    filePath = 'E:/博客/whllhw.github.io/'
    return filePath


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
    import hashlib
    filePath, fileNames = getFileName()
    md5 = hashlib.md5()
    for file in fileNames:
        with open(filePath + file, encoding='utf-8') as f:
            md5.update(f.read().encode('utf-8'))
            passage_md5 = md5.hexdigest()
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


def outPassageTool(passage_id):
    """
    从数据中写出单个文章到文件上
    :param passage_id:
    :return:
    """
    passage = Passage.query.filter(Passage.id == passage_id).first()
    categories = Category.query.join(Tag).join(Passage).filter(Passage.id == 2).all()  # join连接查询出所有的tag
    title = passage.title.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace(
        '<', '').replace('>', '').replace('|', '') + '.md'
    with open(getPath() + title, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: {passage.title}\n')
        f.write('tags: ')
        tag = (i.name for i in categories)
        f.write(', '.join(tag))
        date = passage.date.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'\ndate: {date}\n')
        f.write('---\n\n')
        f.write(passage.context)

    with open(getPath() + title, 'r', encoding='utf-8') as f:
        import hashlib
        md5 = hashlib.md5(f.read().encode('utf-8'))
        db_session.add(File(passage_id, md5.hexdigest(), title))  # 提交文件属性到数据库
        db_session.commit()


def syncPassage():
    """
    同步数据库与文件
    :return:
    """
    import hashlib
    filePath, fileNames = getFileName()
    md5 = hashlib.md5()
    for passage in Passage.query.all():
        if os.path.isdir(filePath + passage.title + '.md'):
            pass


if __name__ == '__main__':
    outPassageTool(30)
