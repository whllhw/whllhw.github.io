#!/usr/bin/env python
# coding=utf-8
from flask import Flask,g,session,redirect
from flask import render_template
from flask import request,Response,url_for
import deploy,json,os
app = Flask(__name__)
import MySQLdb
app.config['SECRET_KEY']=os.urandom(24)
def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = init_db()
    return db

def init_db():
    conn = MySQLdb.connect('localhost','root','lhw520','db_game',3306,'/tmp/mysql.sock',charset='utf8')
    conn.autocommit(1)
    return conn.cursor()

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
# 主页
@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

# 登录界面
@app.route('/login/',methods=['GET','POST'])
def login():
    get_db()
    if request.method == 'POST':
        result = g.db.execute('select username,password from t_user where username="{}" and password="{}"'.format(
            request.form['username'].encode('utf-8'),request.form['password'].encode('utf-8')))
        if result:
            session['logged_in'] = True
            return redirect(url_for('editor'))
        else:
            return 'Login Failed,Please Retry!'
    else:
        if session.get('logged_in'):
            return redirect(url_for('editor'))
        else:
            return render_template('login.html')

# 编辑界面
@app.route('/edit/')
def editor():
    if session.get('logged_in'):
        return render_template('editor.html')
    else:
        return redirect(url_for('login'))
# 上传Markdown文件
@app.route('/upload/', methods=['POST','GET'])
def upload():# JQ 使用Json格式实现跨域传送，前后端JSON数据交换，$.ajax 不会自动转换数据到Json，需要手动转化JSON.stringify
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        filename = deploy.deploy(request.json['content'])
        print request.json['title']
        print request.json['tags']
        return Response(json.dumps({'filename':filename}),  mimetype='application/json')
    else:
        filename = request.args.get('filename',None)
        if filename:
            deploy.post(filename)
            return 'success'
        else:
            return 'error'
if __name__=='__main__':
    app.run(port=5000,host='0.0.0.0')
    


