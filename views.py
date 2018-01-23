from flask import render_template, request, jsonify, abort

from app import create_app
from database import db_session
from models import Passage, Category, Tag

app = create_app()


# 请求结束时自动移除数据库会话
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/passage')
def getAll():
    """
    查询出所有文章并返回
    :return: 所有文章列表
    """
    passages = Passage.query.all()
    return render_template('passage.html', passages=passages)


@app.route('/edit')
@app.route('/edit/<int:id>')
def edit(id=0):
    """
    :param id: 文章id
    :return: 文章编辑页面
    """
    if id:
        passage = Passage.query.filter(Passage.id == id).first()
    else:
        passage = None
    tags = Category.query.all()  # 查询出所有的tags
    tag = (i.category_id for i in Tag.query.filter(Tag.passage_id == id).all())  # 查询出该文章使用的标签
    return render_template('editor.html', passage=passage, tags=tags, tag=tag)


@app.route('/category/<name>')
def create(name):
    """
    :param name:标签名
    :return: 新建标签
    """
    # 填坑
    pass


@app.route('/upload', methods=['POST'])
def upload():
    """
    上传文章
    :return:
    """
    print(request.form)
    if not request.form:
        print("No form data")
        abort(405)
    # TODO：增加修改文章的逻辑
    id = request.form['id']
    passage = db_session.query(Passage).filter(Passage.id == int(id)).scalar()
    if passage:  # 修改文章,update时synchronize_session注意对象引用问题
        passage.title = request.form['title']
        passage.context = request.form['context']
        db_session.commit()
        # 删除文章的原来的标签
        Tag.query.filter(Tag.passage_id == passage.id).delete()
        db_session.commit()
    else:
        db_session.add(Passage(request.form['title'], request.form['context'], 1))  # 保存文章到数据库
        db_session.commit()
    tags = request.form.getlist('tags')  # 获取tag 列表(str)
    passage_id = int(id)  # dangerous!!
    for i in tags:
        # if not Category.query.filter(Category.id == int(i)).first():  # 无该标签则需要创建
        #     pass  # 填坑
        # 假设标签已经存在
        db_session.add(Tag(passage_id, int(i)))
        db_session.commit()

    return jsonify({'id': id,'error':0})


@app.route('/login')
def login():
    """
    登录函数
    :return:
    """
    pass


@app.route('/get/<name>')
def getName(name):
    pass


if __name__ == '__main__':
    app.run(debug=True)
