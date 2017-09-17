#!/usr/bin/env python
# coding=utf-8
from flask import Flask 
from flask import render_template
from flask import request,Response
import deploy,json
app = Flask(__name__)

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
    if request.method == 'POST':
        pass
    else:
        pass
    return 'login'

# 编辑界面
@app.route('/edit/')
def editor():
    return render_template('editor.html')

# 上传Markdown文件
@app.route('/upload/', methods=['POST','GET'])
def upload():# JQ 使用Json格式实现跨域传送，前后端JSON数据交换，$.ajax 不会自动转换数据到Json，需要手动转化JSON.stringify
    if request.method == 'POST':
        filename = deploy.deploy(request.json['content'])
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
    


