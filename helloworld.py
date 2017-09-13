#!/usr/bin/env python
# coding=utf-8
from flask import Flask 
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello/')
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


if __name__=='__main__':
    app.run(port=80,host='0.0.0.0')
    


