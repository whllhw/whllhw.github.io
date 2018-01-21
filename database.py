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

def ImportPassage():
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
    from models import Passage,Category
    from datetime import datetime
    filePath = 'E:/博客/whllhw.github.io/'
    fileNames = [file for file in os.listdir(filePath) if not os.path.isdir(file) and file[-3:]=='.md']
    for file in fileNames:
        with open(filePath+file,encoding='utf-8') as f:
            _ = f.readline()
            title,tag,_,date,*content = (i for i in f)
            title = title.split(':')[1].strip().replace('\n','')
            tag = tag.split(':')[1].replace('\n','').replace('\'','')
            date = date.split(':',1)[1].replace('\n','')  # 注意 maxSplit = 1 最大分割次数
            content = ''.join(content)
            for t in tag.split(','):# 处理标签，对不在数据库中的进行创建
                if not Category.query.filter(Category.name == t.strip()).first():
                    db_session.add(Category(t.strip()))
                    db_session.commit()
            # 提交文章
            if not Passage.query.filter(Passage.title==title).first():
                try:
                    db_session.add(Passage(title=title,context=content,date=datetime.strptime(date.strip(),'%Y-%m-%d %H:%M:%S'),author=1))
                except ValueError:
                    print(file)
                else:
                    print('无错误')
                    db_session.commit()


if __name__ == '__main__':
    # init_db()
    ImportPassage()
    print('数据库初始化完成')