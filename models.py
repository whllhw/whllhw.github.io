from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from database import Base
import datetime


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(10), unique=True)
    password = Column(String(10))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return '<User %r>' % self.username


class Passage(Base):
    __tablename__ = 'Passage'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author_id = Column(Integer, ForeignKey('User.id'))
    context = Column(Text)
    date = Column(DateTime)

    def __init__(self, title, context, author, date=None):
        self.title = title
        self.context = context
        self.author_id = author
        self.date = date or datetime.utcnow()

    def __repr__(self):
        return '<Passage {}>'.format(self.title)

    def __str__(self):
        return self.__repr__()


class Category(Base):  # 存放标签名
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

    def __str__(self):
        return '<Category %r>' % self.name


class Tag(Base):  # 存放一对多的标签对应关系
    __tablename__ = 'Tag'
    id = Column(Integer, primary_key=True)
    passage_id = Column(Integer, ForeignKey('Passage.id'))
    category_id = Column(Integer, ForeignKey('Category.id'))

    def __init__(self, passage_id, category_id):
        self.passage_id = passage_id
        self.category_id = category_id

    def __repr__(self):
        return '<Tag %r>' % self.id

    def __str__(self):
        return '<Tag %r>' % self.id


class File(Base):  # 记录文件md5以及文件名
    __tablename__ = 'File'
    id = Column(Integer, primary_key=True)
    passage_id = Column(Integer, ForeignKey('Passage.id'))
    md5 = Column(String(32))
    fileName = Column(String(50))

    def __init__(self, passage_id, md5, fileName):
        self.md5 = md5
        self.passage_id = passage_id
        self.fileName = fileName

    def __repr__(self):
        return '<File %r>' % self.id

    def __str__(self):
        return self.__repr__()
