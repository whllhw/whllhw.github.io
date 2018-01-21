#!/usr/bin/env python
# coding=utf-8
from flask import Flask,g,session,redirect
from flask import render_template
from flask import request,Response,url_for
from flask.ext.sqlalchemy import SQLAlchemy
import deploy,json,os
import MySQLdb
from app import create_app
app = create_app()

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
        result = g.db.execute('select username,password from t_user where username=%s and password=%s',[
            request.form['username'].encode('utf-8'),request.form['password'].encode('utf-8')])
        if result:
            session['logged_in'] = True
            return redirect(url_for('editor'))
        else:
            return 'Login Failed,Please Retry!'
    else:
        # 获取到登录的 session 则重定向
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
        filename = deploy.deploy(request.json['content'], request.json['title'],request.json['tags'])
        if not request.json['title']:
            return Response(json.dumps({'filename':filename,'error':'未填写标题'}),  mimetype='application/json')
        return Response(json.dumps({'filename':filename}),  mimetype='application/json')
    else:
        filename = request.args.get('filename',None)
        if filename:
            deploy.post(filename)
            return 'success'
        else:
            return 'error'

@app.route('/get/<name>/')
def getPassage(name):
    pass

@app.route('/rm/<name>/')
def rmPassage(name):
    pass

if __name__=='__main__':
    app.run(port=6062,host='0.0.0.0',threaded=True, debug=True)
    


