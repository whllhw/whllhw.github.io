from app import create_app
from flask import render_template,url_for
from database import db_session
from models import User,Passage,Category

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
    return render_template('passage.html',passages=passages)

@app.route('/edit/<id>')
def edit(id):
    """

    :param id: 文章id
    :return: 文章编辑页面
    """
    if id:
        passage = Passage.query.filter(Passage.id == id).first()
    else:
        passage = None
    return render_template('editor.html',passage=passage)

@app.route('/category/<name>')
def create(name):
    """
    :param name:标签名
    :return: 新建标签
    """
    # 填坑
    pass

@app.route('/upload')
def upload(id):
    """
    上传文章
    :return:
    """
    pass

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