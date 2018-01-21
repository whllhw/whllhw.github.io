from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite3.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    import models
    Base.metadata.create_all(bind=engine)


def importPassageTool():
    """
    导磁盘文章到数据库
    :return:
    """
    """
    u = User('username','passwd')
    db_session.add(u)
    db_session.commit()
    User.query.filter(User.name == 'lhw').first()
    """
    import os
    from models import Passage, Category, Tag
    from datetime import datetime
    filePath = 'E:/博客/whllhw.github.io/'
    fileNames = [file for file in os.listdir(
        filePath) if not os.path.isdir(file) and file[-3:] == '.md']
    for file in fileNames:
        with open(filePath + file, encoding='utf-8') as f:
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
            for t in info['tags'].split(','):
                category_id = Category.query.filter(
                    Category.name == t.strip()).first().id
                db_session.add(Tag(passage_id, category_id))
                db_session.commit()


if __name__ == '__main__':
    init_db()
    importPassageTool()
    print('数据库初始化完成')
